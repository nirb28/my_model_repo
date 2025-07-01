#!/usr/bin/env python3
"""
GitHub Repository Downloader

This script downloads a GitHub repository as a zip file and extracts it to a destination location.
Parameters are defined via command line arguments.
"""

import argparse
import os
import requests
import shutil
import sys
import zipfile
from pathlib import Path
from urllib.parse import urlparse


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Download a GitHub repository as a zip file and extract it."
    )
    
    parser.add_argument(
        "--repo", "-r",
        required=True,
        help="GitHub repository URL or owner/repo format (e.g. 'https://github.com/owner/repo' or 'owner/repo')"
    )
    
    parser.add_argument(
        "--branch", "-b",
        default="main",
        help="Branch, tag, or commit reference to download (default: main)"
    )
    
    parser.add_argument(
        "--dest", "-d",
        default=".",
        help="Destination directory to extract files to (default: current directory)"
    )
    
    parser.add_argument(
        "--keep-zip", "-k",
        action="store_true",
        help="Keep the downloaded zip file after extraction"
    )
    
    return parser.parse_args()


def normalize_repo_url(repo_url):
    """Normalize repository URL to standard GitHub format."""
    if not repo_url.startswith("http"):
        # Assume format is owner/repo
        if "/" not in repo_url:
            raise ValueError("Repository format should be 'owner/repo' or a complete GitHub URL")
        return f"https://github.com/{repo_url}"
    
    # Check if it's a valid GitHub URL
    parsed = urlparse(repo_url)
    if parsed.netloc != "github.com":
        raise ValueError("URL must be from github.com")
    
    return repo_url


def download_github_repo(repo_url, branch, dest_dir, keep_zip=False):
    """
    Download a GitHub repository as a zip file and extract it.
    
    Args:
        repo_url: GitHub repository URL
        branch: Branch, tag, or commit reference
        dest_dir: Destination directory to extract files to
        keep_zip: Whether to keep the zip file after extraction
    """
    # Normalize the repository URL
    repo_url = normalize_repo_url(repo_url)
    
    # Extract owner and repo name from URL
    path_parts = urlparse(repo_url).path.strip("/").split("/")
    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub repository URL")
    
    owner, repo = path_parts[0], path_parts[1]
    
    # Create download URL for the zip file
    zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip"
    if not branch.startswith(("heads/", "tags/")):
        # Try alternate URL format
        zip_url = f"https://github.com/{owner}/{repo}/archive/{branch}.zip"
    
    # Create destination directory if it doesn't exist
    dest_path = Path(dest_dir).resolve()
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # Temporary zip file path
    zip_path = dest_path / f"{repo}-{branch}.zip"
    
    print(f"Downloading {owner}/{repo} ({branch}) from GitHub...")
    
    try:
        # Download the zip file
        response = requests.get(zip_url, stream=True)
        response.raise_for_status()
        
        # Save the zip file
        with open(zip_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Download complete. Saved to {zip_path}")
        
        # Extract the zip file
        print(f"Extracting to {dest_path}...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(dest_path)
        
        print(f"Extraction complete.")
        
        # Remove the zip file if not keeping it
        if not keep_zip:
            print(f"Removing temporary zip file...")
            os.remove(zip_path)
    
    except requests.RequestException as e:
        print(f"Error downloading repository: {str(e)}", file=sys.stderr)
        if zip_path.exists():
            os.remove(zip_path)
        return False
    
    except zipfile.BadZipFile:
        print(f"Error: Downloaded file is not a valid zip file.", file=sys.stderr)
        if zip_path.exists():
            os.remove(zip_path)
        return False
    
    return True


def main():
    args = parse_arguments()
    
    try:
        success = download_github_repo(
            args.repo,
            args.branch,
            args.dest,
            args.keep_zip
        )
        
        if success:
            print("Repository download and extraction completed successfully.")
        else:
            print("Repository download or extraction failed.", file=sys.stderr)
            sys.exit(1)
    
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
