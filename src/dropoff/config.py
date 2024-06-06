from pathlib import Path
from dataclasses import dataclass, field
from typing import List, ClassVar, Optional
import json

@dataclass
class DropAuth:
    token: str
    APP_KEY: ClassVar[str] = 'your_app_key'
    
    
@dataclass
class Config:
    local_output_dir: Path
    """The local directory to drop files into."""
    dropbox_parent_dir: str
    """The dropbox parent directory to check for files."""
    naming_schema: List[str] = field(default_factory=list)
    """ The naming schema for the directories to check. should be derivable from a datetime object."""
    def __post_init__(self):
        if not self.naming_schema:
            self.naming_schema = ['%YYYY-MM', '%YYYY-%MM-%DD']
    
config_paths = [ Path('~/.config/dropoff/config.json').expanduser(), Path('/etc/dropoff/config.json')]

def get_config(config_path_override: Optional[Path] = None):
    # if a config path is provided, use it
    # otherwise check for config along paths per xdg spec
    if config_path := config_path_override or next(
        (p for p in config_paths if p.exists()), None
    ):
        with open(config_path) as f:
            return Config(**json.load(f))
    else:
        raise FileNotFoundError("No config file found.")

