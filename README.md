# FLARES: FINE-GRAINED LANGUAGE-BASED RELIABILITY DETECTION IN SPANISH NEWS
This repository contains the code and resources for participating in the FLARE-Challenge, which focuses on fine-grained language-based reliability detection in Spanish news articles. The challenge consists of two subtasks:

- Subtask 1: 5W1Hs Identification
In this subtask, participants are provided with a text and are required to determine the essential content by annotating the answers to the 5W1H questions (Who, What, When, Where, Why, and How) within the document. To participate in this subtask, please use the following Kaggle link: FLARES: Subtask 1 --5W1Hs identification--.
- Subtask 2: 5W1H-based Reliability
For each 5W1H item detected in Subtask 1, participants need to determine the reliability of the language used, classifying it as "confiable" (reliable), "semiconfiable" (semi-reliable), or "no confiable" (not reliable) according to the RUN-AS guideline. To participate in this subtask, please use the following Kaggle link: FLARES: Subtask 2 --Reliability classification--.

For more information about the challenge, please visit: [FLARES-Challenge](https://www.kaggle.com/competitions/flares-subtask-1-5w1hs-identification) on Kaggle

## Usage

1. The dataset for the challenge can be found in the Flares-dataset directory (see the Dataset section below).
2. The LLama3-models folder contains the notebooks for fine-tuning and results of the Llama3-8b model.
3. The Mistral-models folder contains the notebooks for fine-tuning and results of the Mistral-7b model.
4. Flare_Data_exploration.ipynb is a notebook that performs an initial data exploration of the Flare-dataset.
5. Flare_training_set_creation.ipynb is a notebook that performs data preprocessing and prompt generation for LLM fine-tuning.
6. evaluate_subtask_1.py, evaluate_subtask_2.py, evaluation_metric_template_kaggle_subtask_1.py, and evaluation_metric_template_kaggle_subtask_2.py are the official code files used for subtask testing and evaluation.

## Dataset
The dataset used for this challenge can be found in the following GitHub repository: https://github.com/rsepulveda911112/Flares-dataset
