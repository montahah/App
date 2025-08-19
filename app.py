import streamlit as st
from PIL import Image
from rembg import remove
import io

st.set_page_config(page_title="Background Remover", page_icon="🖼️", layout="centered")

st.title("🖼️ Background Remover")
st.write("Upload an image and remove its background instantly.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show original image
    input_image = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(input_image, use_container_width=True)

    # Process button
    if st.button("Remove Background"):
        with st.spinner("Processing..."):
            # Remove background
            output = remove(input_image)

            # Convert to bytes for download
            buf = io.BytesIO()
            output.save(buf, format="PNG")
            byte_im = buf.getvalue()

        st.subheader("Processed Image")
        st.image(output, use_container_width=True)

        # Download button
        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="output.png",
            mime="image/png"
        )
