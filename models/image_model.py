"""
Image classifier module for pneumonia detection from chest X-rays
"""

import torch
import torch.nn as nn
import torchvision.models as models

class ChestXrayClassifier(nn.Module):
    """
    Transfer learning-based classifier for chest X-rays
    
    Args:
        pretrained (bool): Whether to use pretrained weights
        num_classes (int): Number of output classes
    """
    def __init__(self, pretrained=True, num_classes=2):
        super(ChestXrayClassifier, self).__init__()
        # Initialize with pretrained DenseNet121
        self.backbone = models.densenet121(pretrained=pretrained)
        
        # Replace final classification layer
        in_features = self.backbone.classifier.in_features
        self.backbone.classifier = nn.Sequential(
            nn.Linear(in_features, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, num_classes)
        )
        
    def forward(self, x):
        """Forward pass"""
        return self.backbone(x)
    
    def get_features(self, x):
        """Extract features without classification"""
        # Remove the classifier to get features
        original_classifier = self.backbone.classifier
        self.backbone.classifier = nn.Identity()
        
        # Get features
        features = self.backbone(x)
        
        # Restore the classifier
        self.backbone.classifier = original_classifier
        
        return features


def create_image_model(pretrained=True):
    """
    Factory function to create the image model
    
    Args:
        pretrained (bool): Whether to use pretrained weights
        
    Returns:
        model: Initialized model
    """
    model = ChestXrayClassifier(pretrained=pretrained)
    return model