# Automatic Document Summarization Model

Unlock the power of Natural Language Processing (NLP) with our Automatic Document Summarization Model (ADSM), designed to effortlessly distill the essence of lengthy articles and research papers. Tired of drowning in information overload? Let our ADSM be your guide, providing crisp and coherent summaries, saving you valuable time and effort.

## Problem Statemet

Long articles and research papers contain a wealth of information, posing a challenge for readers to efficiently grasp essential details. The objective is to develop an Automatic Document Summarization Model (ADSM) using NLP techniques. This model will employ advanced methods to generate succinct and meaningful summaries of lengthy textual documents.

## Features 

### 1. Frontend 

- **Text Input:** Users can input documents through typing or copy-pasting.
- **Summary Length Selection:** Option for users to choose the desired length of the summary.
- **Model Selection:** Users can choose from various summarization models.
- **Language Selection:** Support for over 150 languages.
- **Keyword Generation:** Automatic extraction of key words based on the document.
- **Text-to-Speech:** Option to listen to the summarized document.

### 2. Models 

- **Fine-tuned BART:** Created a fine-tuned BART model (uploaded to HuggingFace). [link to our model](https://huggingface.co/datasets/scientific_papers?row=0)
- **Pegasus:** Used a powerful pre-trained model for abstractive summarization.
- **BART:** Leveraged a pre-trained Bidirectional and Auto-Regressive Transformers for text generation.
- **LSTM:** Created a Long Short-Term Memory networks for sequence-to-sequence learning

### 3. Dive into the Data

Scientific papers datasets from ArXiv and PubMed OpenAccess repositories. The datasets include:

- **article:** The document body, presented in paragraphs.
- **abstract:** The summary of the document.
- **section_names:** Clearly defined titles of document sections.

[Explore Datasets](https://huggingface.co/datasets/scientific_papers?row=0)

## Seamless User Experience

1. **Input:** Type or paste your document.
2. **Customize:** Choose your preferred summary length and model.
3. **Diversity:** Select from a multitude of languages.
4. **Discover:** Automatically generated keywords provide extra insights.
5. **Listen:** Transform your document into an auditory experience with text-to-speech.

## Important components in Action


