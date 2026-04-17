# InstaSplitter

Split images into Instagram-ready slices for continuous scroll posts.

## Setup

```bash
pip install -r requirements.txt
```

## Usage - GUI (Recommended)

The GUI provides a step-by-step interface:

```bash
python insta_splitter_gui.py
```

### GUI Steps:
1. **Step 1**: Select your wide/panoramic image
2. **Step 2**: Choose where to save the slices
3. **Step 3**: Click "Analyze" to preview, then "Split & Save"

## Usage - Command Line

```bash
python split_image.py your_image.png
```

### With Custom Output Directory

```bash
# Using -o flag
python split_image.py your_image.jpg -o C:\Users\you\Desktop\slices

# Using --output flag
python split_image.py your_image.jpg --output "D:\Photos\Instagram"

# As second positional argument
python split_image.py your_image.jpg D:\MyPhotos
```

## How It Works

Instagram single image size: **1080 x 1350** (portrait)

This script splits a wide/panoramic image into multiple 1080x1350 slices.

### Example

If you have a 6-slide continuous scroll image:
- Input: `6480 x 1350` pixels (6 horizontal slides)
- Output: 6 images of `1080 x 1350` each
  - `your_image_slice_1_1.png`
  - `your_image_slice_1_2.png`
  - `your_image_slice_1_3.png`
  - `your_image_slice_1_4.png`
  - `your_image_slice_1_5.png`
  - `your_image_slice_1_6.png`

## Supported Formats

PNG, JPG, JPEG, WebP, BMP, GIF

## Troubleshooting

**pip not working?**
```bash
python -m pip install -r requirements.txt
```

If that fails, try reinstalling Python and check "Add to PATH" during installation.
