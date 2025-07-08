import streamlit as st
import whisper
import os

def main():
    st.title("Audio Transcription with Whisper")

    # File upload
    uploaded_file = st.file_uploader("Upload an audio file (MP3)", type=["mp3"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp_audio.mp3", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Model selection
        model_option = st.selectbox(
            "Choose a Whisper model",
            ("tiny", "base", "small", "medium", "large")
        )

        if st.button("Transcribe"):
            try:
                with st.spinner(f"Transcribing with {model_option} model..."):
                    model = whisper.load_model(model_option)
                    result = model.transcribe("temp_audio.mp3")
                    transcription = result["text"]

                st.success("Transcription complete!")
                st.text_area("Transcription", transcription, height=200)

                # Download link
                st.download_button(
                    label="Download transcription as .txt",
                    data=transcription,
                    file_name="transcription.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                # Clean up the temporary file
                os.remove("temp_audio.mp3")

if __name__ == "__main__":
    main()