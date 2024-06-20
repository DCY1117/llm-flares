# FLARES: FINE-GRAINED LANGUAGE-BASED RELIABILITY DETECTION IN SPANISH NEWS
This repository contains the code and resources for participating in Subtask 1 of the FLARE-Challenge, which focuses on 5W1Hs identification in Spanish news articles.
The FLARE-Challenge consists of two subtasks:
- **Subtask 1:** 5W1Hs Identification
In this subtask, participants are provided with a text and are required to determine the essential content by annotating the answers to the 5W1H questions (Who, What, When, Where, Why, and How) within the document. To participate in this subtask, please use the following Kaggle link: FLARES: Subtask 1 --5W1Hs identification--.
- **Subtask 2:** 5W1H-based Reliability
For each 5W1H item detected in Subtask 1, participants need to determine the reliability of the language used, classifying it as "confiable" (reliable), "semiconfiable" (semi-reliable), or "no confiable" (not reliable) according to the RUN-AS guideline. To participate in this subtask, please use the following Kaggle link: FLARES: Subtask 2 --Reliability classification--.

For more information about the challenge, please visit: [FLARES-Challenge](https://www.kaggle.com/competitions/flares-subtask-1-5w1hs-identification) on Kaggle

## Repository Structure

- **Flares-dataset:** Contains the challenge dataset (https://github.com/rsepulveda911112/Flares-dataset).
- **Flare_Data_exploration.ipynb:** Performs initial data exploration of the Flare-dataset.
- **Flare_training_set_creation.ipynb:** Handles data preprocessing and prompt generation for LLM fine-tuning.
- **LLama3-models:** Notebooks for fine-tuning and results of the Llama3-8b model.
- **Mistral-models:** Notebooks for fine-tuning and results of the Mistral-7b model.
- **evaluate_subtask_1.py, evaluate_subtask_2.py, evaluation_metric_template_kaggle_subtask_1.py, evaluation_metric_template_kaggle_subtask_2.py:** Official code files for subtask testing and evaluation (https://github.com/rsepulveda911112/Flares-dataset).

## Acknowledgements
- Mistral fine-tuning notebooks: https://github.com/brevdev/notebooks/tree/main
