# InstaSplitter

Split images into Instagram-ready slices for continuous scroll posts.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Just run the script - it will ask you questions:

```bash
python split_image.py
```

The program will:
1. Ask for your image file path
2. Ask where to save the slices (default: Desktop)
3. Show you how many slices it will make
4. Split and save them
5. Open the output folder

## How It Works

Instagram single image size: **1080 x 1350** (portrait)

This script splits a wide/panoramic image into multiple 1080x1350 slices.

### Example

If you have a 6-slide continuous scroll image:
- Input: `6480 x 1350` pixels (6 horizontal slides)
- Output: 6 images of `1080 x 1350` each

## Supported Formats

PNG, JPG, JPEG, WebP, BMP
