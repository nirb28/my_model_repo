# Utility Scripts

This directory contains various utility scripts for the my_model_repo project.

## GitHub Repository Downloader

The `github_downloader.py` script allows you to download any GitHub repository as a zip file and extract it to a destination location.

### Usage

```bash
python github_downloader.py --repo owner/repo --branch branch_name --dest destination_folder
```

### Command-line Options

- `--repo` or `-r`: GitHub repository URL or owner/repo format (required)
- `--branch` or `-b`: Branch, tag, or commit reference to download (default: main)
- `--dest` or `-d`: Destination directory to extract files to (default: current directory)
- `--keep-zip` or `-k`: Keep the downloaded zip file after extraction

### Examples

```bash
# Basic usage (downloads main branch to current directory)
python github_downloader.py --repo username/repository

# Specify branch and destination
python github_downloader.py --repo https://github.com/username/repository --branch develop --dest ./downloads

# Keep the zip file after extraction
python utils/github_downloader.py --repo username/repository --keep-zip --dest 
```

### Full Path Example

If you're running from the project root:

```bash
python utils/github_downloader.py --repo username/repository --dest ./downloaded_repos
```
