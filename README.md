# Multimodal Approach to Pneumonia Detection

*Research project investigating the integration of medical imaging and clinical text for improved pneumonia diagnosis*

## Research Objective

This research explores whether combining chest X-ray images with clinical text data can improve pneumonia detection accuracy while maintaining clinical interpretability. The project focuses on:

1. Comparative analysis of unimodal vs. multimodal approaches
2. Novel fusion architectures for heterogeneous medical data
3. Explainability techniques for clinical decision support

## Methodology

### Data Sources
- **Chest X-ray Images**: NIH Chest X-ray Dataset & Pneumonia-specific chest X-ray collections
- **Clinical Text**: MTSamples medical transcription dataset filtered for pneumonia-related content

### Experimental Design
The project follows a systematic research methodology:
1. Independent modality evaluation (establish baselines)
2. Multiple fusion strategy comparison
3. Performance analysis across diagnostic conditions

### Technical Approach
- **Image Analysis**: Transfer learning with DenseNet121/ResNet50
- **Text Analysis**: Clinical BERT for medical terminology understanding
- **Multimodal Integration**: Feature-level fusion with explainable components

## Current Progress

The project is currently in the data preparation and exploratory analysis phase:

- [x] Dataset acquisition and preprocessing pipeline development
- [x] Filtering of relevant medical text samples (1,293 pneumonia-related samples identified)
- [x] Exploratory data analysis of imaging and text datasets
- [ ] Baseline unimodal model implementation
- [ ] Multimodal fusion architecture design

## Research Challenges

A key research challenge being addressed is the non-linked nature of the available datasets. Rather than assuming artificial relationships between unrelated X-ray and text data, this project explores a more scientifically sound approach that:

1. Builds strong individual classifiers for each modality
2. Extracts meaningful patterns from each data type
3. Demonstrates how complementary information could enhance diagnostic confidence

## References

* Wang, X., et al. (2017). "ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases"
* Irvin, J., et al. (2019). "CheXpert: A Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison"
* Alsentzer, E., et al. (2019). "Publicly Available Clinical BERT Embeddings"