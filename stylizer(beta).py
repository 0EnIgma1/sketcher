import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from collections.abc import Iterable
def stylizer(image1, image2):
    def convert(image):
        img = tf,io.read_file(image)
        img = tf.image.decode_image(img, channels = 3)
        img = tf.image.convert_image_dtype(img, tf.float32)
        img = tf.image.resize(img, (512,512), preserve_aspect_ratio = True)
        img = img[tf.newaxis, :]
        return img

    original_image = convert(image1)
    style_image = convert(image2)

    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)
    output = hub_module(original_image, style_image)
    out_img = output[0]
    if len(out_img.shape) > 3:
	    out_img = tf.squeeze(out_img, axis = 0)
    return out_img

def style_upload(image1):
    image1 = image1
    image2 = None
    try:
        styleFile = st.file_uploader(label="Upload your style image below", type=['jpg', 'png'])
    except:
        st.subheader("Please upload Style Image")
    if styleFile is not None:
        im2 = Image.open(styleFile)
        image2 = np.array(im2)
        stylizer(image1,image2)
