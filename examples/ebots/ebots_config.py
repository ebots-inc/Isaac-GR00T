import os

from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)


ebots_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=["cam_high", "cam_left_wrist", "cam_right_wrist"],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "arm_l",
            "arm_l_finger",
            "arm_r",
            "arm_r_finger",
            "stage",
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(0, 16)),
        modality_keys=[
            "arm_l",
            "arm_l_finger",
            "arm_r",
            "arm_r_finger",
            "stage",
        ],
        action_configs=[
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
        ],
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["annotation.human.task_description"],
    ),
}

ebots_left_arm_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=["cam_high", "cam_left_wrist", "cam_side"],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "arm_l",
            "arm_l_finger",
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(0, 16)),
        modality_keys=[
            "arm_l",
            "arm_l_finger",
        ],
        action_configs=[
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
        ],
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["annotation.human.task_description"],
    ),
}

ebots_left_arm_eef_rotvec_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=["cam_high", "cam_left_wrist", "cam_side"],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "arm_l",
            "arm_l_finger",
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(0, 16)),
        modality_keys=[
            "arm_l",
            "arm_l_finger",
        ],
        action_configs=[
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.EEF,
                format=ActionFormat.XYZ_ROTVEC,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
        ],
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["annotation.human.task_description"],
    ),
}

ebots_right_arm_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=["cam_high", "cam_right_wrist"],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "arm_r",
            "arm_r_finger",
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(0, 16)),
        modality_keys=[
            "arm_r",
            "arm_r_finger",
        ],
        action_configs=[
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
        ],
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["annotation.human.task_description"],
    ),
}


_VARIANT_TO_CONFIG = {
    "bimanual": ebots_config,
    "left_arm": ebots_left_arm_config,
    "left_arm_eef_rotvec": ebots_left_arm_eef_rotvec_config,
    "right_arm": ebots_right_arm_config,
}

variant = os.environ.get("EBOTS_CONFIG_VARIANT", "bimanual").strip().lower()
if variant not in _VARIANT_TO_CONFIG:
    raise ValueError(
        f"Unknown EBOTS_CONFIG_VARIANT={variant!r}. Valid options: {sorted(_VARIANT_TO_CONFIG.keys())}"
    )

register_modality_config(_VARIANT_TO_CONFIG[variant], embodiment_tag=EmbodimentTag.NEW_EMBODIMENT)
