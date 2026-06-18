import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load CT scan
ct_scan = nib.load("archive (1)/volume_pt1/volume-0.nii")

# Load segmentation mask
mask = nib.load("archive (1)/segmentations/segmentation-0.nii")

# Convert to numpy arrays
ct_data = ct_scan.get_fdata()
mask_data = mask.get_fdata()

# Select slice
slice_index = 55

# Extract slice
ct_slice = ct_data[:, :, slice_index]
mask_slice = mask_data[:, :, slice_index]

# Normalize CT image
ct_slice = cv2.normalize(
    ct_slice,
    None,
    0,
    255,
    cv2.NORM_MINMAX
).astype(np.uint8)

# Convert grayscale to color
ct_color = cv2.cvtColor(ct_slice, cv2.COLOR_GRAY2BGR)

# Convert mask to binary
mask_uint8 = (mask_slice > 0).astype(np.uint8)

# Find contours
contours, _ = cv2.findContours(
    mask_uint8,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Variables for tumor contour
largest_area = 0
tumor_contour = None

# Ignore huge liver contour
for cnt in contours:

    area = cv2.contourArea(cnt)

    # Small contour = tumor
    if area < 5000 and area > largest_area:

        largest_area = area
        tumor_contour = cnt

# Draw red circle only around tumor
if tumor_contour is not None:

    (x, y), radius = cv2.minEnclosingCircle(tumor_contour)

    center = (int(x), int(y))
    radius = int(radius)

    cv2.circle(
        ct_color,
        center,
        radius,
        (0, 0, 255),
        3
    )

# Display image
plt.figure(figsize=(8,8))

plt.imshow(cv2.cvtColor(ct_color, cv2.COLOR_BGR2RGB))

plt.title("Tumor Detection")

plt.axis("off")

plt.show()