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
    # Try to load from current directory first, then from home directory
    load_dotenv()  # Current directory
    load_dotenv(os.path.expanduser('~/.env'))  # Home directory
    
    token = os.getenv('VRM_TOKEN')
    
    if not token:
        print("Error: VRM_TOKEN not found in .env file")
        print("Please create .env file in your home directory (~/.env) or current directory")
        print("with: VRM_TOKEN=your_token_here")
        sys.exit(1)
    
    return token


def get_user_id(token):
    """Get the user ID from VRM API"""
    url = f"{VRM_API_BASE}/users/me"
    headers = {
        "X-Authorization": f"Token {token}"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get('user', {}).get('id')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user info: {e}")
        sys.exit(1)


def get_installations(token, user_id):
    """Fetch all installations from VRM API"""
    url = f"{VRM_API_BASE}/users/{user_id}/installations"
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
        
        # SOC is in records.bs array - last element contains current SOC
        records = data.get('records', {})
        bs_data = records.get('bs', [])
        
        if bs_data and len(bs_data) > 0:
            # Last entry in array: [timestamp, avg, min, max]
            last_entry = bs_data[-1]
            if len(last_entry) >= 2:
                # Return the average SOC value (index 1)
                return round(last_entry[1], 1)
        
        return None
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
    
    # Get user ID
    user_id = get_user_id(token)
    
    # Get all installations
    print("Fetching installations...")
    installations = get_installations(token, user_id)
    
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
            print("  SOC: Not available")
        
        print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()
