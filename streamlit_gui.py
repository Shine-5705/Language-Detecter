import streamlit as st
from langdetect import detect
from langdetect import lang_detect_exception

# Mapping of language codes to their full names
LANGUAGE_NAMES = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'bg': 'Bulgarian',
    'bn': 'Bengali',
    'ca': 'Catalan',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'et': 'Estonian',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'gu': 'Gujarati',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'kn': 'Kannada',
    'ko': 'Korean',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepali',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pa': 'Punjabi',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'sq': 'Albanian',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tl': 'Tagalog',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)'
}

def detect_language(text):
    try:
        language_code = detect(text)
        language_name = LANGUAGE_NAMES.get(language_code, 'Unknown')
    except lang_detect_exception.LangDetectException as e:
        # Handle exceptions, such as when the input is too short
        print("Error during language detection:", e)
        return None
    return language_name

def main():
    st.title("Language Detection App")

    # Input text box for user input
    input_text = st.text_area("Enter text:")

    if st.button("Detect Language"):
        if not input_text:
            st.warning("Please enter some text.")
        else:
            detected_language = detect_language(input_text)
            if detected_language:
                st.success(f"Detected language: {detected_language}")
            else:
                st.error("Failed to detect language.")

if __name__ == "__main__":
    main()
