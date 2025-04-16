# System Architecture

## Overview

This project implements a multimodal architecture for pneumonia detection with separate encoders for images and text, followed by a fusion module and classifier.

## Components

### 1. Image Processing Pipeline

- Preprocessing: Resize to 224×224, normalization, data augmentation
- Feature Extraction: DenseNet121/ResNet50 pretrained on medical images
- Output: 1024-dimensional feature vector representing radiological patterns

### 2. Text Processing Pipeline

- Preprocessing: Clinical text cleaning, tokenization, stopword removal
- Feature Extraction: Clinical BERT embeddings 
- Output: 768-dimensional feature vector capturing clinical information

### 3. Multimodal Fusion Module

Multiple approaches being investigated:
1. **Simple Concatenation**: Baseline approach combining feature vectors
2. **Cross-Modal Attention**: Allowing text features to highlight relevant image regions
3. **Gated Fusion**: Learned weighting of modality importance

### 4. Diagnosis Module

- Binary classification (pneumonia present/absent)
- Confidence scoring for clinical relevance
- Explainability components (Grad-CAM for images, attention visualization for text)

## Experimental Setup

The system is being evaluated through a rigorous experimental protocol:
1. Train/validate/test split with stratification by diagnosis
2. Separate evaluation of each modality independently
3. Comparative analysis of fusion strategies
4. Ablation studies to isolate component contributions