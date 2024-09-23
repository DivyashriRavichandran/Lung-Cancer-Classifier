## About the Project


This project demonstrates the potential of the **DCGAN (Deep Convolutional Generative Adversarial Network)** augmented model in improving the accuracy and reliability of lung cancer diagnosis. 

### 🚀 **Key Features:**
- **Data Augmentation:** Utilizes synthetic image generation to expand datasets where resources are limited.
- **Enhanced CNN Model:** Classifies histopathological images of lung tissues to detect various types of lung cancer.
- **Accuracy:** Achieves a 93% accuracy rate.

## Running the Web Application

To run the Lung Cancer Detector Web Application, make sure you have Docker Desktop installed.

### Instructions:

1. Download the files from this GitHub.
   
2. Open a terminal and go to Classifier Web App folder.

3. Build the Docker image for the Streamlit app:

    ```bash
    docker build -t classifier_app .
    ```

4. Run the Docker container locally:

    ```bash
    docker run -p 8502:8501 classifier_app
    ```

5. Access the web application by navigating to [http://localhost:8502](http://localhost:8502).

<br>

### User Interface of the Application:
![User Interface of the Application](Classifier%20Web%20App/web%20UI.png)


