"""Implements functions used for the artistic style transfer."""
import os
import functools
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def crop_center(image):
    """Return the image cropped to the center."""
    shape = image.shape
    new_shape = min(shape[1], shape[2])

    offset_y = max(shape[1] - shape[2], 0) // 2
    offset_x = max(shape[2] - shape[1], 0) // 2

    image = tf.image.crop_to_bounding_box(image, offset_y, offset_x, new_shape, new_shape)
    return image


def resize_image_to_square(image_rgb_np, image_size=(256, 256)):
    """Return the resized image (square)."""
    image_np_extra = image_rgb_np.astype(np.float32)[np.newaxis, ...]

    if image_np_extra.max() > 1.0:
        image_np_extra = image_np_extra / 255

    if len(image_np_extra.shape) == 3:
        image_np_extra = tf.stack([image_np_extra, image_np_extra, image_np_extra], axis=-1)

    image_np_extra = crop_center(image_np_extra)
    image_np_extra = tf.image.resize(image_np_extra, image_size, preserve_aspect_ratio=True)
    return image_np_extra


@functools.lru_cache(maxsize=None)
def load_image(image_url, image_size=(256, 256)):
    """Loads and returns an image from a given link."""
    image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:], image_url)
    img = plt.imread(image_path).astype(np.float32)[np.newaxis, ...]

    if img.max() > 1.0:
        img = img / 255

    if len(img.shape) == 3:
        img = tf.stack([img, img, img], axis=1)

    img = crop_center(img)
    img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
    return img
