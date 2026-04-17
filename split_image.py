"""
InstaSplitter - Split images for Instagram continuous scroll posts

Instagram single image: 1080 x 1350 (portrait/vertical)
This script splits wide images into multiple Instagram-ready slices.

Just run: python split_image.py
"""

import os
from pathlib import Path
from PIL import Image

INSTA_WIDTH = 1080
INSTA_HEIGHT = 1350


def get_image_path():
    """Ask user for image path."""
    while True:
        print("\n" + "="*50)
        print("STEP 1: Select Image")
        print("="*50)
        path = input("\nEnter the path to your image file: ").strip().strip('"')

        if not path:
            print("Please enter a path!")
            continue

        if os.path.exists(path):
            return path
        else:
            print(f"File not found: {path}")
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != 'y':
                return None


def get_output_dir():
    """Ask user for output directory."""
    print("\n" + "="*50)
    print("STEP 2: Output Location")
    print("="*50)

    default = os.path.join(os.path.expanduser("~"), "Desktop")
    print(f"\nDefault: {default}")
    path = input("Enter output folder (or press Enter for default): ").strip().strip('"')

    if not path:
        return default

    # Create if doesn't exist
    os.makedirs(path, exist_ok=True)
    return path


def analyze_and_split(image_path, output_dir):
    """Analyze image and split it."""
    print("\n" + "="*50)
    print("STEP 3: Analyze & Split")
    print("="*50)

    # Analyze
    with Image.open(image_path) as img:
        width, height = img.size
        original_format = img.format.lower() or 'png'

    slices_horizontal = width // INSTA_WIDTH
    slices_vertical = height // INSTA_HEIGHT
    total = slices_horizontal * slices_vertical

    print(f"\nImage size: {width} x {height} pixels")
    print(f"Slices: {total} ({slices_horizontal} across x {slices_vertical} down)")
    print(f"Each slice: {INSTA_WIDTH} x {INSTA_HEIGHT} pixels")
    print(f"\nOutput folder: {output_dir}")

    confirm = input("\nStart splitting? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancelled.")
        return

    # Create output folder
    input_stem = Path(image_path).stem
    slice_folder = Path(output_dir) / f"{input_stem}_slices"
    slice_folder.mkdir(parents=True, exist_ok=True)

    print(f"\nSplitting...")

    # Split
    count = 0
    with Image.open(image_path) as img:
        for row in range(slices_vertical):
            for col in range(slices_horizontal):
                left = col * INSTA_WIDTH
                top = row * INSTA_HEIGHT
                right = left + INSTA_WIDTH
                bottom = top + INSTA_HEIGHT

                slice_img = img.crop((left, top, right, bottom))

                slice_name = f"{input_stem}_slice_{row + 1}_{col + 1}.{original_format}"
                slice_path = slice_folder / slice_name

                slice_img.save(slice_path)
                count += 1

                print(f"  [{count}/{total}] {slice_name}")

    print(f"\nDone! Created {count} slices in:\n{slice_folder}")

    # Open folder
    os.startfile(slice_folder)


def main():
    print("\n" + "="*50)
    print("  InstaSplitter - Instagram Image Splitter")
    print("="*50)
    print("\nSplits wide images into 1080x1350 slices for")
    print("Instagram continuous scroll posts.")

    # Get image path
    image_path = get_image_path()
    if not image_path:
        print("\nNo image selected. Goodbye!")
        return

    # Get output directory
    output_dir = get_output_dir()

    # Analyze and split
    analyze_and_split(image_path, output_dir)


if __name__ == "__main__":
    main()
