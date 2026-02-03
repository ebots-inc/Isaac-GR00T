set -x -e

export NUM_GPUS=1
export CUDA_VISIBLE_DEVICES=0

# Select which ebots modality config is registered by examples/ebots/ebots_config.py:
#   left_arm (default), bimanual, right_arm
export EBOTS_CONFIG_VARIANT=${EBOTS_CONFIG_VARIANT:-left_arm}

# master_port: pick any unused TCP port (commonly 29501–29600). 
# If running one job, 29500 is usually fine.
# Check if free: ss -ltn | grep ':29500 '
# torchrun --nproc_per_node=$NUM_GPUS --master_port=29500 \
python \
    gr00t/experiment/launch_finetune.py \
    --base_model_path nvidia/GR00T-N1.6-3B \
    --dataset_path  /root/.cache/huggingface/lerobot/EbotsVLA/set_1 \
    --modality_config_path examples/ebots/ebots_config.py \
    --embodiment_tag NEW_EMBODIMENT \
    --num_gpus $NUM_GPUS \
    --output_dir /root/.cache/huggingface/lerobot/EbotsVLA/checkpoints/run_001 \
    --save_steps 1000 \
    --save_total_limit 5 \
    --max_steps 10000 \
    --warmup_ratio 0.05 \
    --weight_decay 1e-5 \
    --learning_rate 1e-4 \
    --use_wandb \
    --global_batch_size 32 \
    --color_jitter_params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
    --random_rotation_angle 2 \
    --dataloader_num_workers 4
