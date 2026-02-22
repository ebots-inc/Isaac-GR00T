set -euxo pipefail

export NUM_GPUS=1
export CUDA_VISIBLE_DEVICES=0

# Select which ebots modality config is registered by examples/ebots/ebots_config.py:
#   left_arm (default), bimanual, right_arm
export EBOTS_CONFIG_VARIANT=${EBOTS_CONFIG_VARIANT:-left_arm}

# masking
# --mask-right-wrist-until-episode 548 \

# finetuning
# --warmup-ratio 0.1 \ 
# --learning-rate 5e-6 \
# --state_dropout_prob 0.15 \

# high res
# --global-batch-size 16 \
# --gradient-accumulation-steps 2 \
# --dataloader-num-workers 4 \

# master_port: pick any unused TCP port (commonly 29501–29600). 
# If running one job, 29500 is usually fine.
# Check if free: ss -ltn | grep ':29500 '
# torchrun --nproc-per-node=$NUM_GPUS --master_port=29500 \
python \
    gr00t/experiment/launch_finetune.py \
    --base-model-path nvidia/GR00T-N1.6-3B \
    --dataset-path $HOME/.cache/huggingface/lerobot/EbotsVLA/set_1 \
    --modality-config-path examples/ebots/ebots_config.py \
    --embodiment-tag NEW_EMBODIMENT \
    --num-gpus "$NUM_GPUS" \
    --output-dir $HOME/.cache/huggingface/lerobot/EbotsVLA/checkpoints/run_001 \
    --save-steps 5000 \
    --save-total-limit 5 \
    --max-steps 30000 \
    --warmup-ratio 0.05 \
    --weight-decay 1e-5 \
    --learning-rate 1e-4 \
    --use-wandb \
    --global-batch-size 32 \
    --color-jitter-params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
    --random-rotation-angle 2 \
    --dataloader-num-workers 8
