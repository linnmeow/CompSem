# Semantic Tagging with XLM-RoBERTa

This repository contains a PyTorch implementation for semantic tagging using XLM-RoBERTa. The model predicts fine-grained semantic tags for tokens in English text, achieving >97% validation accuracy after 5 epochs.

## Features
- **Semantic Tagging**: Predicts 72 unique semantic tags (e.g., `ORG`, `PER`, `GEO`).
- **Subword Handling**: Aligns labels with tokenizer subwords using `-100` masking.
- **Learning Rate Scheduling**: Uses `ReduceLROnPlateau` for dynamic learning rate adjustment.
- **Evaluation Metrics**: Tracks training/validation loss and accuracy.

## Dataset
- **Format**: `en_gold.txt` with TSV-formatted tokens and tags:
  ```
  Token₁	TAG₁
  Token₂	TAG₂
  ...

- **Tags**: 72 unique semantic tags (e.g., `ORG`, `PER`, `GEO`, `NOW`).

## Model Architecture
```python
class SemanticTaggingModel(nn.Module):
    def __init__(self, num_pos_tags):
        super().__init__()
        self.roberta = XLMRobertaModel.from_pretrained("xlm-roberta-base")
        self.linear = nn.Linear(768, num_pos_tags)  # 72 output classes
```

## Training Configuration
- **Optimizer**: Adam (`lr=1e-5`)
- **Loss Function**: Cross-Entropy (ignoring `-100` padded tokens)
- **Batch Size**: 16
- **Epochs**: 5
- **LR Scheduler**: `ReduceLROnPlateau(factor=0.1, patience=2)`

## Requirements
```bash
pip install torch pandas datasets transformers matplotlib sklearn
```

## Usage
1. **Prepare Data**: Place `en_gold.txt` in the working directory.
2. **Train Model**:
   ```python
   from train import train_model
   model = train_model(num_epochs=5, batch_size=16)
   ```
3. **Inference** (Example):
   ```python
   from inference import predict
   sentence = ["A", "wolf", "chases", "a", "rabbit", "."]
   tags = predict(model, tokenizer, sentence)  # e.g., ['ART', 'ANIMAL', 'ACTION', 'ART', 'ANIMAL', 'PUNCT']
   ```

## Future Improvements
- Add support for multi-lingual tagging
- Implement class weighting for imbalanced tags
- Integrate Hugging Face `Trainer` for distributed training
