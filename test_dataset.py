import nibabel as nib
import matplotlib.pyplot as plt

# Load CT scan
ct_scan = nib.load("/Users/veer/Downloads/archive (1)/volume_pt1/volume-0.nii")

# Load segmentation mask
mask = nib.load("/Users/veer/Downloads/archive (1)/segmentations/segmentation-0.nii")

# Convert to numpy arrays
ct_data = ct_scan.get_fdata()
mask_data = mask.get_fdata()

print("CT Shape:", ct_data.shape)
print("Mask Shape:", mask_data.shape)

# Show one slice
slice_index = 55

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(ct_data[:,:,slice_index], cmap='gray')
plt.title("CT Scan")

plt.subplot(1,2,2)
plt.imshow(mask_data[:,:,slice_index], cmap='gray')
plt.title("Tumor Mask")

plt.show()