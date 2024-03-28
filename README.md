# Language-Detecter
This repository contains code for a language detection model using a Bidirectional LSTM neural network. The model is built using TensorFlow and Keras, trained on a dataset containing text samples in different languages.

This repository contains code for a language detection model using a Bidirectional LSTM neural network, along with two user interfaces:

    Streamlit Web App with Langdetect:
        A Streamlit web app for language detection using the langdetect library.
        Users can input text and get the predicted language.
        This method relies on the langdetect library for language detection.

    Tkinter Desktop GUI with LSTM Model:
        A Tkinter desktop GUI for language detection using the LSTM model.
        Users can input text and get the predicted language.
        This method utilizes the trained Bidirectional LSTM model for language prediction.

Overview:

    The LSTM model is built using TensorFlow and Keras, trained on a dataset of multilingual text samples.
    The langdetect method provides an alternative approach for language detection without training a model.
    Both interfaces offer easy ways for users to input text and receive the predicted language.

Contents:

    streamlit_gui.py: Streamlit web app for language detection using langdetect.
    tkinter_gui.py: Tkinter desktop GUI for language detection using the LSTM model.
    langdetect_model.py: Python script for language detection using the langdetect library.
    LSTM_model.py :Python script for language detection using the LSTM model is built using TensorFlow and Keras, trained on a dataset of multilingual text samples
    Language Detection.csv: Sample dataset containing text samples and their corresponding language labels.
    requirements.txt: With that you can install all teh required libraries
    README.md: You are reading it now!

Usage:

    Clone the Repository:

    bash

git clone https://github.com/your_username/language-detection.git
cd language-detection

Install Dependencies:

    Ensure you have the required libraries installed:

    bash

    pip install numpy pandas tensorflow scikit-learn langdetect streamlit

Run the Streamlit Web App:

    Start the Streamlit web app for language detection with langdetect:

    bash

    streamlit run streamlit_gui.py

        This opens a web interface where users can input text and get the predicted language.

Run the Tkinter Desktop GUI with LSTM Model:

    Start the Tkinter desktop GUI for language detection using the LSTM model:

    bash

    python tkinter_gui.py

        This opens a desktop window where users can input text and get the predicted language.

Alternative Language Detection with Langdetect:

    To use the langdetect library directly for language detection, you can run:

    bash

        python langdetect_model.py

            This script provides language detection without the need for model training.

Additional Notes:

    Both the Streamlit app and Tkinter GUI use the LANGUAGE_NAMES dictionary to provide readable language names for predictions.
    The langdetect library offers quick and efficient language detection based on statistical methods.
    Feel free to explore, modify, and improve upon these scripts to suit your needs.

Credits:

    The LSTM model implementation is inspired by Deep Learning Course by Coursera.
    Streamlit web app and Tkinter GUI development references various online resources and tutorials.
    The langdetect library provides language detection functionality based on text statistics.
