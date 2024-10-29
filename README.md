
<p align="center"><img src="https://raw.githubusercontent.com/Oct4Pie/brain-tumor-detection/main/logo/brain.png" width="10%" style="margin: 0px; transform: translateY(-50%)">
</p>

# Brain-tumor-detection (CNN)
<img src="https://i.imgur.com/C0rTivW.png">

## About
This program is designed to facilitate the diagnosis of brain tumors from 2D MRI scan images, ensuring both accuracy and timeliness. The model is created using the TensorFlow API in Python, leveraging the high-level Keras API. The image classifier is based on a deep Convolutional Neural Network (CNN). For more information, try the [Streamlit app](https://brain-tumor-detection0.streamlit.app).

## Model Information
### Model Summary
```
Model: "sequential"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ conv2d (Conv2D)                      │ (None, 50, 50, 32)          │             896 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ max_pooling2d (MaxPooling2D)         │ (None, 25, 25, 32)          │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ conv2d_1 (Conv2D)                    │ (None, 25, 25, 64)          │          18,496 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ max_pooling2d_1 (MaxPooling2D)       │ (None, 12, 12, 64)          │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dropout (Dropout)                    │ (None, 12, 12, 64)          │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ flatten (Flatten)                    │ (None, 9216)                │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense (Dense)                        │ (None, 128)                 │       1,179,776 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_1 (Dense)                      │ (None, 1)                   │             129 │
└──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
 Total params: 3,597,893 (13.72 MB)
 Trainable params: 1,199,297 (4.57 MB)
 Non-trainable params: 0 (0.00 B)
 Optimizer params: 2,398,596 (9.15 MB)
```
### Model Report

```
              precision    recall  f1-score   support

           0       1.00      1.00      1.00       209
           1       1.00      0.99      1.00       191

    accuracy                           1.00       400
   macro avg       1.00      1.00      1.00       400
weighted avg       1.00      1.00      1.00       400
```

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Oct4Pie/brain-tumor-detection.git
    cd brain-tumor-detection
    ```

2. **Create and activate a virtual environment (Python 3.9+):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

## Usage
### Streamlit Web App
- Test out the pre-made samples or
- Upload an MRI image via the Streamlit interface.
- The app will automatically crop the image to the brain area, analyze it, and display the results, including whether a tumor is detected and the confidence of the prediction.

### Running the Model
- The model can be trained, evaluated, and used for predictions using the provided Python scripts. Make sure to adjust the file paths and parameters as needed. Please refer to [Model Details and Training Process](#more-info-model-details-and-training-process)


## File Structure
```
├── README.md
├── app.py                    # Main entry point for the Streamlit application
├── logo
│   └── brain.png          
├── model
│   ├── __init__.py        
│   ├── class_rep.py          # Script for generating classification reports
│   ├── mask.py               # Functions for cropping and classifying MRI images
│   ├── modeler.py            # Code for training the model
│   ├── plot.py               # Script for plotting model metrics
│   ├── predict.py            # Script for making predictions using the trained model
│   └── predictor.py          # Script for doing tests & predictions
├── package.json
├── pages
│   ├── __init__.py     
│   ├── _pages
│   │   ├── __init__.py    
│   │   ├── about.py          # Script for the "About" page
│   │   ├── components.py     # Script for UI templates
│   │   ├── github.py         # Script for the "GitHub" page
│   │   ├── home.py           # Script for the home page of the application
│   │   ├── try_it.py         # Script for a page where users can try out the model
│   │   └── utils.py          # Utility used across different pages
│   ├── components
│   │   ├── github_card.html  # template for displaying GitHub profile
│   │   ├── github_iframe.html  # template for embedding the repo
│   │   └── title.html        # HTML template for the main title component
│   ├── css
│   │   └── streamlit.css     # Custom CSS for Streamlit
│   └── samples     # Sample cropped MRI validation images
│       ├── cropped_gg (18).jpg 
│       ├── cropped_gg (497).jpg
│       ├── cropped_no112.jpg
│       ├── cropped_no153.jpg
│       ├── cropped_no997.jpg
│       └── cropped_y549.jpg 
├── requirements.txt          # List of Python dependencies
└── temp.png
```

## Acknowledgements
- [Brain Tumor Classification (MRI)](https://www.kaggle.com/sartajbhuvaji/brain-tumor-classification-mri) (datasets)
- [Brain MRI Images for Brain Tumor Detection](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection) (datasets)
- [MRI Based Brain Tumor Images](https://www.kaggle.com/mhantor/mri-based-brain-tumor-images) (datasets)
- [Starter: Brain MRI Images for Brain](https://www.kaggle.com/kerneler/starter-brain-mri-images-for-brain-b5be8b94-c) (datasets and inspiration)

---

## More Info: Model Details and Training Process

### Overview

This section provides a more in-depth explanation of the Convolutional Neural Network (CNN) model used for the project, detailing the model architecture, training process, and how predictions are made. I will try to explain each utility with its features, role, and why they are used.

### Model Architecture

The model is designed using TensorFlow and Keras and consists of several layers, including convolutional, pooling, dropout, and dense layers. The architecture is specifically tailored for binary classification of MRI images to detect the presence of brain tumors.

#### Layers

1. **Input Layer**
   - **Shape**: (50, 50, 3)
   - **Description**: Accepts color images resized to 50x50 pixels (best based on avaiable resolutions and reasonable memory usage).
   - **Reason**: Standardizes the input size for the model to ensure consistency across all images.

2. **First Convolutional Layer**
   - **Filters**: 32
   - **Kernel Size**: (3, 3)
   - **Activation**: ReLU
   - **Padding**: SAME
   - **Description**: Extracts features from the input image using 32 different filters.
   - **Reason**: Detects low-level features such as edges and textures (these are crucial for understanding the structure of MRI images).

3. **First Max-Pooling Layer**
   - **Pool Size**: (2, 2)
   - **Strides**: 2
   - **Description**: Reduces the spatial dimensions of the feature maps.
   - **Reason**: Reduces computational complexity and helps in making the feature detection process invariant to small translations.

4. **Second Convolutional Layer**
   - **Filters**: 64
   - **Kernel Size**: (3, 3)
   - **Activation**: ReLU
   - **Padding**: SAME
   - **Description**: Extracts more complex features from the feature maps using 64 filters.
   - **Reason**: Captures higher-level features and patterns which are very important for distinguishing between normal and abnormal brain tissues.

5. **Second Max-Pooling Layer**
   - **Pool Size**: (2, 2)
   - **Strides**: 2
   - **Description**: Further reduces the spatial dimensions of the feature maps.
   - **Reason**: Continues to reduce computational load and helps in extracting more abstract features.

6. **Dropout Layer**
   - **Rate**: 0.6
   - **Description**: Prevents overfitting by randomly setting 60% of the input units to 0 during training.
   - **Reason**: Regularizes the model by preventing it from becoming too reliant on any specific neurons to improve its generalization to new data.

7. **Flatten Layer**
   - **Description**: Flattens the 3D feature maps to a 1D vector to be fed into the dense layers.
   - **Reason**: Prepares the data for the fully connected dense layers by transforming it into a suitable format.

8. **First Dense Layer**
   - **Units**: 128
   - **Activation**: ReLU
   - **Regularization**: L2 with a factor of 0.001
   - **Description**: Learns high-level features and patterns from the flattened input.
   - **Reason**: Adds non-linearity and helps in learning complex patterns that are necessary for classification.

9. **Output Dense Layer**
   - **Units**: 1
   - **Activation**: Sigmoid
   - **Description**: Produces a probability indicating the presence of a tumor.
   - **Reason**: Outputs a probability score that helps in the binary classification decisions (tumor/no tumor).

### Training Process

#### Data Preparation

1. **Loading Data**
   - The `get_samples` function loads and shuffles image file paths for training.
   - Images are read, resized to 50x50 pixels, and labeled based on their directory ("yes" for tumor, "no" for no tumor).
   - **Reason**: Makes sure that the data is in a uniform format and that there is a balanced distribution of classes.

2. **Splitting Data**
   - Data is split into training and validation sets, with the last 400 images reserved for validation.
   - **Reason**: This allows the model to be evaluated on unseen data to help in monitoring its generalization ability.

#### Model Compilation

- **Optimizer**: AdamW (Adam with Weight Decay)
  - **Learning Rate**: 0.001
  - **Weight Decay**: 1e-5
  - **Reason**: AdamW combines the benefits of Adam (adaptive learning rates) with weight decay, and this helps in preventing overfitting.
- **Loss Function**: Binary Crossentropy
  - **Reason**: Suitable for binary classification tasks as it measures the performance of the model in terms of probability error.
- **Metrics**: Accuracy, AUC (Area Under Curve), Precision, Recall
  - **Reason**: Provides a readable and understandable evaluation of the model’s performance across various aspects.

#### Callbacks

- **Early Stopping**: Monitors validation loss, stops training if it doesn't improve for 30 epochs, and restores the best weights.
  - **Reason**: Prevents overfitting and ensures the model retains the best weights.
- **ReduceLROnPlateau**: Reduces the learning rate by a factor of 0.5 if the validation loss doesn't improve for 5 epochs.
  - **Reason**: Helps in fine-tuning the learning process and lets the model to converge better.
- **TensorBoard**: Logs training process for visualization in TensorBoard.
  - **Reason**: Shows valuable data of the training process and allows for better debugging and understanding of the model’s behavior.
- **ModelCheckpoint**: Saves the best model based on validation precision.
  - **Reason**: Makes sure the best-performing model is saved, which can be used for inference and further evaluation.

#### Training

The `train` function fits the model on the training data, using the specified callbacks to optimize the training process. The model is trained for up to 500 epochs but can stop early if the early stopping criterion is met.

#### Steps

1. **Initialization**: Model and optimizer are initialized with the specified parameters.
2. **Fitting**: Model is trained on the training data with the specified callbacks and validation data.
3. **Evaluation**: After training, the model is evaluated on the validation set to monitor its performance.

### Prediction Process

#### Loading the Model

The `get_model` function loads the trained model and evaluates its performance on a validation set to ensure it is working correctly.

#### Making Predictions

1. **Image Preprocessing**: New MRI images are preprocessed similarly to the training images (resized to 50x50 pixels).
2. **Model Prediction**: The model predicts the probability of a tumor being present.
3. **Output**: The predicted class (tumor/no tumor) and confidence level are shown.

#### Steps

1. **Loading**: The trained model is loaded.
2. **Preprocessing**: The input image is preprocessed to match the training data format.
3. **Prediction**: The model predicts the probability of a tumor.
4. **Output**: The result is displayed, indicating the presence or absence of a tumor with a confidence score.

## Code Explanation

### mask.py

#### Role
The `mask.py` script is responsible for processing MRI images to extract the brain region. It has functions for cropping the images and identifying the largest contours which represent the brain area.

#### Functions

##### get_max_contour(contours)
- **Description**: This function finds and returns the largest contour from a list of contours.
- **Parameters**: 
  - `contours`: The list of contours obtained from the image.
- **Returns**: The largest contour.

##### crop_img(gray, img, file)
- **Description**: This function crops the image to the bounding box of the largest contour found.
- **Parameters**: 
  - `gray`: Grayscale version of the image.
  - `img`: Original image.
  - `file`: Filename (currently not used in the function).
- **Returns**: Cropped image.

##### extract_brain(gray, img, buffer)
- **Description**: This function extracts the brain region from the image using morphological operations and contour detection.
- **Parameters**: 
  - `gray`: Grayscale version of the image.
  - `img`: Original image.
  - `buffer`: Padding buffer for the cropping.
- **Returns**: The extracted brain region and a boolean flag indicating success.

### modeler.py

#### Role
The `modeler.py` script is responsible for training the brain tumor detection model ("main file"). It has functions for loading and processing image data, building the CNN model, and training the model.

#### Functions

##### is_image(file_path)
- **Description**: This function checks if a file is a valid image.
- **Parameters**: 
  - `file_path`: Path to the file.
- **Returns**: Boolean indicating whether the file is an image.

##### get_samples()
- **Description**: This function retrieves and shuffles the list of image file paths for training.
- **Parameters**: None
- **Returns**: List of image file paths.

##### get_test_samples(size)
- **Description**: This function loads and processes test images.
- **Parameters**: 
  - `size`: Size to which the images should be resized.
- **Returns**: Numpy array of processed test images.

##### get_test_sample(img_name)
- **Description**: This function loads and processes a single test image by name.
- **Parameters**: 
  - `img_name`: Name of the test image file.
- **Returns**: Numpy array of the processed test image.

##### classify(img_paths, size)
- **Description**: This function loads and processes images for classification.
- **Parameters**: 
  - `img_paths`: List of image file paths.
  - `size`: Size to which the images should be resized.
- **Returns**: Tuple of Numpy arrays (images, labels).

##### train(read_images, properties)
- **Description**: This function builds and trains the CNN model using the provided images and labels.
- **Parameters**: 
  - `read_images`: Numpy array of images.
  - `properties`: Numpy array of labels.
- **Returns**: None


### predictor.py

#### Description
The `predictor.py` script is used for loading the trained model and making predictions on new MRI images.

#### Functions

##### get_test_sample(img_name, size)
- **Description**: This function loads and processes a single test image by name.
- **Parameters**: 
  - `img_name`: Name of the test image file.
  - `size`: Size to which the images should be resized.
- **Returns**: Numpy array of the processed test image.

##### get_model(num=0)
- **Description**: This function loads the trained model and evaluates its performance on the validation set.
- **Parameters**: 
  - `num`: Model version number to load.
- **Returns**: Tuple (model, metrics dictionary).

### How the Code Works

1. **Preprocessing (mask.py)**:
   - The script processes the MRI images by converting them to grayscale and then applying morphological operations to isolate the brain region.
   - The largest contour is identified and used to crop the image to focus on the brain area.

2. **Training (modeler.py)**:
   - The script loads and preprocesses the images, shuffles them, and splits them into training and validation sets.
   - The CNN model is built with multiple convolutional, pooling, dropout, and dense layers.
   - The model is trained using the training set, with early stopping and learning rate reduction callbacks to optimize the training process.
   - The trained model is saved for later use and testing.

3. **Prediction (predictor.py)**:
   - It loads the trained model and evaluates its performance on a validation set to ensure it is working correctly.
   - It takes new MRI images, preprocesses them similarly to the training images, and uses the model to predict whether a tumor is present.
   - The prediction results, including the confidence level, are printed for evluation and informational purposes.

## Resources for Further Reading and Learning

### Deep Learning and Neural Networks
1. **[Dive into Deep Learning (D2L)](https://d2l.ai/chapter_convolutional-neural-networks/index.html)**
   - An interactive deep learning book with code, math, and discussions. Free and open-source.

2. **[TensorFlow Official Documentation](https://www.tensorflow.org/tutorials/images/cnn)**
   - Official tutorials and documentation for TensorFlow with guides on building convolutional neural networks. Free and open-source.

3. **[Deep Learning with Python Notebooks by François Chollet](https://github.com/fchollet/deep-learning-with-python-notebooks)**
   - Jupyter notebooks that supplement the book "Deep Learning with Python" by François Chollet. Free and open-source.

### Image Processing and Computer Vision
4. **[Practical Python and OpenCV by Adrian Rosebrock](https://www.pyimagesearch.com/practical-python-opencv/)**
   - A practical guide to learning computer vision with Python and OpenCV. Free articles available on the blog.

5. **[ImageNet Large Scale Visual Recognition Challenge (ILSVRC)](http://www.image-net.org/challenges/LSVRC/)**
   - A large-scale image recognition challenge. Free and open-source.

### Medical Imaging
6. **[The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/)**
   - A large archive of medical images of cancer accessible for public download. Free and open-source.
