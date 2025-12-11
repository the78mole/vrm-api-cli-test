"""
Victron VRM API CLI Tool
This package provides a CLI tool to retrieve State of Charge (SOC) 
for all installations from the Victron VRM API.
"""

__version__ = "0.1.0"

from .cli import main

__all__ = ["main"]
