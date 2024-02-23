# Machine Learning Student Performance Indicator

**Unlocking insights into the factors that influence student test scores.**

## Overview

- **Exploring the Impact of Factors on Student Performance:** This project delves into the realm of machine learning to uncover how various factors, such as gender, ethnicity, parental education, lunch options, and test preparation courses, impact student performance in exams.
- **Data-Driven Analysis and Modeling:** It leverages a dataset of student scores and demographics to train and evaluate multiple machine learning models, aiming to identify the most effective predictor of student outcomes.
- **Key Features:**
  - Exploratory Data Analysis (EDA) to uncover patterns and relationships within the dataset.
  - Model Training and Evaluation using a diverse range of machine learning algorithms.
  - Hyperparameter Tuning to optimize model performance.
  - Docker Image for seamless reproducibility and deployment.

## Project Structure

- **data/:** Houses the raw dataset and any preprocessed data.
- **models/:** Stores trained machine learning models.
- **notebooks/:** Includes Jupyter notebooks for data exploration, model training, and analysis.
- **src/:** Contains Python scripts for data preprocessing, model training, and evaluation.
- **Dockerfile:** Provides instructions for building the Docker image.

## Getting Started

1. **Clone the Repository:**

```bash
  git clone https://github.com/jmdtanalyst/ML_Student_Performance.git
```

2. **Build the Docker Image**

```bash
docker build -t ml-student-performance .

```

3. **Run the Docker Container**

```bash
docker run -p 80:80  ml-student-performance

```

### Usage

    Explore Notebooks: Dive into detailed analysis and model development within the notebooks.
    Utilize Scripts: Use Python scripts in src/ for data preprocessing and model training.
    Experiment with Hyperparameters: Fine-tune model performance by adjusting hyperparameters.
    Deploy Docker Image: Utilize the Docker image for production use.

### Contributions

Contributions are welcome!

### License

This project is licensed under the MIT License. See the LICENSE file for details.

Let's collaborate to predict academic success and empower student achievement!
