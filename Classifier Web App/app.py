# Import Libraries
import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model

# Function to load the Keras model
def load_keras_model(model_path):
    try:
        model = load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Load Keras model
keras_model = load_keras_model('Model/classifier.h5')

# Class names
classes = ['Adenocarcinoma', 'Benign Lung Tumor', 'Squamous Cell Carcinoma']

# Function to preprocess the image
def preprocess_image(image):
    img = image.resize((80, 80)) 
    img = np.expand_dims(img, axis=0)
    return img

# Define the Streamlit app
def main():    
        st.title('Lung Cancer Detector')

        st.write("""This image classifer is designed to detect the type of lung cancer present in the 
                    histopathological image of the lung tissues. Upload the image and the deep learning model 
                    predicts the class(cancerous or malignant).""")
        
        # Upload image
        uploaded_image = st.file_uploader("")

        if uploaded_image is not None:
            # Display the uploaded image
            image = Image.open(uploaded_image)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Check if the model is loaded
            if keras_model is not None:
                img = preprocess_image(image)
                # Classify the image
                prediction = keras_model.predict(img)
                predicted_class = np.argmax(prediction)
                predicted_label = classes[predicted_class]
                confidence_percentage = np.max(prediction) * 100
                display_text = f"{predicted_label} ({confidence_percentage:.2f}%)"
                st.subheader(display_text)

                # Text based on the predicted class
                if predicted_label == 'Benign Lung Tumor':
                    st.write("""Benign is a noncancerous tumor that do not spread to other parts of the body. 
                                Although not cancerous, they may still require medical help depending on their size and location.""")
                    st.write("""Symptoms: Wheezing, persistent coughing or coughing up blood, shortness of breath and fever.""")
                    st.write("""Treatment: . If your nodule is benign, you will not need any further treatment, except to manage any underlying 
                                problems or complications related to the nodule such as pneumonia or an obstruction. 
                                If you need invasive surgery to remove a tumor, your doctor may recommend one or more tests beforehand to ensure your health. 
                                These will include blood tests, kidney, liver, and pulmonary (lung) function tests, and an ECG.""")

                elif predicted_label == 'Adenocarcinoma':
                    st.write("""Adenocarcinoma is a non-small cell lung cancer that develops in the cells lining the 
                                alveoli and can spread to other parts of the body.""")
                    st.write("""Symptoms: Wheezing, persistent coughing or coughing up blood, difficulty breathing, chest pain, 
                                unexplained weight loss, loss of appetite.""")
                    st.write("""Treatment: Surgery, radiotherapy, chemotherapy, laser therapy and specialized medications. Treatment varies with the stage of cancer.""")

                elif predicted_label == 'Squamous Cell Carcinoma':
                    st.write("""Squamous Cell Carcinoma is a non-small cell lung cancer that develops in the lining of the bronchial tubes.""")
                    st.write("""Symptoms: Cough, chest pain, shortness of breath, wheezing, hoarseness, 
                                recurring chest infections, weight loss, loss of appetite and fatigue.""")
                    st.write("""Treatment: Surgery, radiotherapy, chemotherapy, laser therapy and specialized medications. Treatment varies with the stage of cancer.""")
        
if __name__ == '__main__':
    main()


# Symptoms and treatments - [1] [2]
# [1] Lung nodules & benign lung tumors: Symptoms, causes, & treatment 2022. WebMD. [Online]. [Accessed: 28 April 2024]. Available from: https://www.webmd.com/lung/benign-lung-tumors-and-nodules 
# [2] Sabbula, B.R. 2023. Squamous cell lung cancer, StatPearls. [Online]. [Accessed: 28 April 2024]. Available from: https://www.ncbi.nlm.nih.gov/books/NBK564510/#:~:text=Reported%20symptoms%20of%20NSCLCs%20can,early%20stages%20of%20the%20disease.