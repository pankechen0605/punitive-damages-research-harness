from __future__ import annotations

from enum import Enum
from typing import TypedDict


class TargetStep(str, Enum):
    ACTIVATE_TOPIC_CONFIG = "activate_topic_config"
    RAW_COLLECTION = "raw_collection"
    DIGEST = "digest"
    FRAMEWORK_DESIGN = "framework_design"
    PILOT = "pilot"
    FRAMEWORK_LOCK = "framework_lock"
    BATCH_CASE_CARDS = "batch_case_cards"
    CROSS_CASE_COMPARISON = "cross_case_comparison"
    FINAL_SYNTHESIS = "final_synthesis"
    OUTPUT_ADAPTATION = "output_adaptation"


class ProjectStatus(TypedDict):
    has_topic_config: bool
    has_raw_layer: bool
    has_digest_layer: bool
    has_framework_layer: bool
    has_synthesis_layer: bool
    has_output_layer: bool
    available_templates: list[str]
    available_prompts: list[str]
    warnings: list[str]


class StepPrerequisites(TypedDict):
    allowed: bool
    missing_prerequisites: list[str]
    warnings: list[str]
    suggested_next_action: str


class HarnessAssets(TypedDict):
    docs: list[str]
    templates: list[str]
    prompts: list[str]
    scripts: list[str]
