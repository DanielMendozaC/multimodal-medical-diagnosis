# Literature Review

This document summarizes key research that informs our multimodal approach to pneumonia detection.

## Chest X-ray Classification

1. **CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning** (Rajpurkar et al., 2017)
   - 121-layer CNN achieving radiologist-level performance
   - Established benchmark performance on the ChestX-ray14 dataset
   - Key finding: Deep learning can match specialist-level diagnosis

2. **Cardiologist-Level Arrhythmia Detection with CNNs** (Hannun et al., 2019)
   - Demonstrated superior performance of deep learning over traditional methods
   - Highlighted importance of model interpretability in clinical settings

## Clinical Text Analysis

1. **BioBERT: A Pre-trained Biomedical Language Representation Model** (Lee et al., 2019)
   - Domain-specific BERT model for biomedical text mining
   - Improved performance on biomedical NLP tasks
   - Key finding: Domain adaptation significantly improves text understanding

2. **ClinicalBERT: Modeling Clinical Notes and Predicting Hospital Readmission** (Huang et al., 2019)
   - BERT adaptation to clinical narratives
   - Demonstrated value in extracting insights from unstructured clinical notes

## Multimodal Learning in Healthcare

1. **Multimodal Deep Learning for Biomedical Data Fusion** (Xu et al., 2019)
   - Approaches for combining heterogeneous medical data
   - Comparisons of early, late, and hybrid fusion techniques
   - Challenge: Dealing with different scales and missing modalities

2. **Explainable Multimodal Classification of Radiology Exams** (Chauhan et al., 2020)
   - Integration of images and text reports
   - Attention mechanisms for cross-modal feature alignment
   - Importance of explainability for clinical adoption

## Research Gaps This Project Addresses

1. Limited work on fusion techniques specifically designed for chest X-rays and clinical text
2. Need for better explainability in multimodal medical systems
3. Lack of systematic comparison of unimodal vs. multimodal approaches for pneumonia detection
4. Insufficient attention to clinical workflow integration in existing research