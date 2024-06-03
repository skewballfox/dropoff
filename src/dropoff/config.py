from pathlib import Path
from dataclasses import dataclass


@dataclass
class DropBoxConfig:
    token: str
    parent_dir: str
    
@dataclass
class Config:
    
    output_dir: Path

