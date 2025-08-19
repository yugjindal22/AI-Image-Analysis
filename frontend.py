import streamlit as st
import os
from main import generate_with_image, generate_text_only
from PIL import Image
import io


def main():
    st.set_page_config(
        page_title="AI Image Analysis Chat",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 AI Image Analysis Chat")
    st.markdown("Upload an image and chat with AI about it using Google Gemini!")
    
    # Check if API key is set
    if not os.environ.get("GEMINI_API_KEY"):
        st.error("⚠️ GEMINI_API_KEY environment variable is not set. Please set it to use this app.")
        st.stop()
    
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize flag to control image display
    if "show_image" not in st.session_state:
        st.session_state.show_image = True
    
    # Sidebar for image upload
    with st.sidebar:
        st.header("📸 Image Upload")
        
        # Use a key that changes when we want to reset the uploader
        uploader_key = f"file_uploader_{st.session_state.get('uploader_reset_count', 0)}"
        
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'],
            help="Upload an image to analyze with AI",
            key=uploader_key
        )
        
        if uploaded_file is not None and st.session_state.show_image:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Store image info in session state
            st.session_state.uploaded_image = uploaded_file.getvalue()
            st.session_state.image_mime_type = uploaded_file.type
            st.session_state.image_name = uploaded_file.name
            
            st.success(f"✅ Image uploaded: {uploaded_file.name}")
        elif uploaded_file is None:
            # Clear image from session state when file is removed
            if hasattr(st.session_state, 'uploaded_image'):
                del st.session_state.uploaded_image
                del st.session_state.image_mime_type
                del st.session_state.image_name
            st.session_state.show_image = True
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
    
    # Main chat interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.header("💬 Chat")
        
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if "image_name" in message:
                    st.caption(f"🖼️ Image: {message['image_name']}")
    
    # Accept user input - MOVED TO THE BOTTOM
    if prompt := st.chat_input("Ask something about the image or just chat..."):
        # Check if we have an image before processing
        has_image = hasattr(st.session_state, 'uploaded_image')
        current_image = None
        current_mime_type = None
        current_image_name = None
        
        if has_image:
            current_image = st.session_state.uploaded_image
            current_mime_type = st.session_state.image_mime_type
            current_image_name = st.session_state.image_name
        
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt}
        if has_image:
            user_message["image_name"] = current_image_name
        st.session_state.messages.append(user_message)
        
        # Display user message in chat message container - INSIDE col1
        with col1:
            with st.chat_message("user"):
                st.markdown(prompt)
                if has_image:
                    st.caption(f"🖼️ Image: {current_image_name}")
            
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                with st.spinner("🤔 AI is thinking..."):
                    try:
                        # Prepare chat history (exclude the current message)
                        chat_history = st.session_state.messages[:-1]
                        
                        if has_image:
                            # Generate response with image and chat history
                            response = generate_with_image(
                                current_image,
                                prompt,
                                current_mime_type,
                                chat_history
                            )
                            
                            # Clear image from context after using it
                            del st.session_state.uploaded_image
                            del st.session_state.image_mime_type
                            del st.session_state.image_name
                            
                            # Hide the image and reset the uploader
                            st.session_state.show_image = False
                            st.session_state.uploader_reset_count = st.session_state.get('uploader_reset_count', 0) + 1
                        else:
                            # Generate text-only response with chat history
                            response = generate_text_only(prompt, chat_history)
                        
                        st.markdown(response)
                        
                    except Exception as e:
                        response = f"❌ Error: {str(e)}"
                        st.error(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    with col2:
        st.header("ℹ️ Info")
        
        if hasattr(st.session_state, 'uploaded_image'):
            st.success("🖼️ Image loaded")
            st.write(f"**Name:** {st.session_state.image_name}")
            st.write(f"**Type:** {st.session_state.image_mime_type}")
            st.write(f"**Size:** {len(st.session_state.uploaded_image):,} bytes")
        else:
            st.info("📋 Upload an image to analyze it with AI")
        
        st.markdown("---")
        st.markdown("""
        **How to use:**
        1. Upload an image using the sidebar
        2. Type your question about the image
        3. AI will analyze and respond
        4. Continue chatting with context!
        
        **Tips:**
        - You can ask about objects, colors, text, emotions, etc.
        - Try questions like "What do you see?" or "Describe this image"
        - Ask follow-up questions like "What did I ask before?"
        - AI remembers your conversation history
        - Upload a new image anytime to change context
        """)

        st.markdown("---")
        st.markdown("**Examples:**")
        st.markdown("""
        - "What do you see in this image?"
        - "What did I say before this?"
        - "Can you elaborate on your previous answer?"
        - "Compare this to what we discussed earlier"
        """)


if __name__ == "__main__":
    main()
