from PIL import Image, ImageOps
from sklearn.decomposition import PCA
import numpy as np
import os
import matplotlib.pyplot as plt

def img_data(img_path, disp=True):
    orig_img = Image.open(img_path)
    img_size_kb = os.path.getsize(img_path) / 1024
    data = np.array(orig_img.getdata())
    orig_pixels = data.reshape(*orig_img.size, -1) # -1 means "all channels"
    img_dim = orig_pixels.shape

    if disp:
        print(f"Original image size: {img_size_kb:.2f} KB")
        print(f"Original image dimensions: {img_dim}")
        print(f"Original image shape: {orig_pixels.shape}")
        plt.imshow(orig_img, cmap='gray')
        plt.axis('off')
        plt.show()

    return {
        "orig_img": orig_img,
        "img_size_kb": img_size_kb,
        "data": data,
        "orig_pixels": orig_pixels,
        "img_dim": img_dim
    }

def pca_compose(img_path):
    img = img_data(img_path, disp=False)["orig_pixels"]
    pca_channel = {}
    img_t = np.transpose(img) # (H, W, C) -> (C, H, W)

    for i in range(img.shape[-1]):
        per_channel = img_t[i]
        channel = img_t[i].reshape(*img.shape[: -1]) # (C, H, W) -> (H, W)
        pca = PCA(random_state=42)
        fit_pca = pca.fit_transform(channel)
        pca_channel[i] = pca, fit_pca

    return pca_channel

def pca_transform(pca_channel, n_components=50):
    temp_res = []
    for channel in range(len(pca_channel)):
        pca, fit_pca = pca_channel[channel]
        pca_pixel = fit_pca[:, :n_components]
        pca_comp = pca.components_[:n_components, :]
        # projecting
        compressed_pixel = np.dot(pca_pixel, pca_comp) + pca.mean_
        # reconstructing
        temp_res.append(compressed_pixel)
    
    compressed_image = np.transpose(np.array(temp_res))
    compressed_image = np.array(compressed_image, dtype=np.uint8)
    return compressed_image

if(__name__ == "__main__"):
    img_path = "./Data/pic.png"
    img = img_data(img_path, disp=True)
    pca_channel = pca_compose(img_path)
    compressed_image = pca_transform(pca_channel, n_components=11)

    # Display the compressed image
    plt.imshow(compressed_image, cmap='gray')
    plt.axis('off')
    plt.show()
    # Save the compressed image
    compressed_img = Image.fromarray(compressed_image)
    compressed_img.save("compressed_image.png")
    compressed_img.show()