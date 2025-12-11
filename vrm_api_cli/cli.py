"""
Victron VRM API CLI Tool
This script retrieves the State of Charge (SOC) for all installations
from the Victron VRM API.
"""

import os
import sys
import requests
from dotenv import load_dotenv


# VRM API Base URL
VRM_API_BASE = "https://vrmapi.victronenergy.com/v2"


def load_token():
    """Load VRM token from .env file"""
    load_dotenv()
    token = os.getenv('VRM_TOKEN')
    
    if not token:
        print("Error: VRM_TOKEN not found in .env file")
        print("Please copy env.tmpl to .env and add your VRM token")
        sys.exit(1)
    
    return token


def get_installations(token):
    """Fetch all installations from VRM API"""
    url = f"{VRM_API_BASE}/users/installations"
    headers = {
        "X-Authorization": f"Token {token}"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get('records', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching installations: {e}")
        sys.exit(1)


def get_installation_soc(token, installation_id):
    """Get SOC for a specific installation"""
    url = f"{VRM_API_BASE}/installations/{installation_id}/stats"
    headers = {
        "X-Authorization": f"Token {token}"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Try to find SOC in the stats
        records = data.get('records', {})
        
        # SOC is typically in the 'totals' section
        totals = records.get('totals', {})
        soc = totals.get('battery_soc')
        
        return soc
    except requests.exceptions.RequestException as e:
        print(f"Error fetching SOC for installation {installation_id}: {e}")
        return None


def main():
    """Main function to display SOC for all installations"""
    print("=" * 60)
    print("Victron VRM API - State of Charge (SOC) Report")
    print("=" * 60)
    print()
    
    # Load token
    token = load_token()
    
    # Get all installations
    print("Fetching installations...")
    installations = get_installations(token)
    
    if not installations:
        print("No installations found")
        return
    
    print(f"Found {len(installations)} installation(s)")
    print()
    
    # Display SOC for each installation
    for installation in installations:
        installation_id = installation.get('idSite')
        name = installation.get('name', 'Unnamed')
        
        print(f"Installation: {name} (ID: {installation_id})")
        
        # Get SOC
        soc = get_installation_soc(token, installation_id)
        
        if soc is not None:
            print(f"  SOC: {soc}%")
        else:
            print(f"  SOC: Not available")
        
        print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()
