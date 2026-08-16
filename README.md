# 📝 AI Text Summarizer

An end-to-end **AI-powered Text Summarization application** built using a fine-tuned **T5-small Transformer model**, **PyTorch**, and **FastAPI**.

The application takes conversational text as input and generates a concise summary using a trained NLP model.

---

## ✨ Features

- 🤖 T5-small Transformer model
- 💬 Conversational text summarization
- 🧠 Fine-tuned on the SAMSum dialogue dataset
- 🔤 Text preprocessing and tokenization
- ⚡ FastAPI backend
- 🌐 Web-based interface
- 💾 Saved trained model and tokenizer
- 🖥️ CPU, CUDA and Apple MPS support
- 🔎 Beam-search based text generation

---

## 🧠 Project Overview

The project follows a complete machine learning workflow:

Dataset
↓
Data Preprocessing
↓
Tokenization
↓
T5-small Model
↓
Fine-tuning
↓
Saved Model
↓
FastAPI Backend
↓
Web Interface
↓
Generated Summary

The project is divided into two main parts:

### 📁 Model

The model folder contains:

- Dataset
- Data preprocessing
- Tokenization
- T5-small model
- Model training
- Checkpoints
- Training results
- Saved model and tokenizer

### 🌐 Application

The application folder contains:

- FastAPI backend
- Model loading
- Text preprocessing
- Summary generation
- Web interface

---

## 🛠️ Technologies Used

- **Python**
- **PyTorch**
- **Hugging Face Transformers**
- **T5-small**
- **Pandas**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Jinja2**
- **HTML / CSS / JavaScript**

---

## 📊 Dataset

This project uses the **SAMSum dialogue dataset**, which contains conversational dialogues paired with human-written summaries.

The dataset is used to train the model to transform conversational text into concise summaries.

---

## 🤖 Model

The project uses the:

**T5-small Transformer**

T5 treats summarization as a **text-to-text generation task**.

The input is formatted as:

summarize: <dialogue>

The model then generates:

<summary>

During training, the dialogue is used as the input sequence and the corresponding summary is used as the target sequence.

---

## ⚙️ Training Configuration

| Parameter | Value |
|-----------|-------|
| Model | T5-small |
| Input Maximum Length | 512 tokens |
| Summary Maximum Length | 150 tokens |
| Training Epochs | 6 |
| Training Batch Size | 8 |
| Evaluation Batch Size | 8 |
| Weight Decay | 0.01 |
| Warmup Steps | 500 |
| Evaluation | Every Epoch |
| Checkpoint Saving | Every Epoch |

The trained model and tokenizer are saved in:

text summarizer model/saved_summary_model/


# Text Summarizer

A text summarization application powered by a trained machine learning model and served via a FastAPI backend. This tool takes dialogue or text as input and generates a concise summary.

## Project Structure

```
text-summarizer/
│
├── text summarizer model/
│   │
│   ├── data/
│   │   ├── samsum-train.csv
│   │   └── samsum-validation.csv
│   ├── saved_summary_model/
│   │
│   └── Text_Summarizer.ipynb
│
├── textsummarizerapp/
│   │
│   ├── app.py
│   └── index.html
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 📂 Model Folder

The text summarizer model folder contains the complete machine learning workflow:

Dataset
Data preprocessing
Tokenization
T5-small model
Model training
Training checkpoints
Training results
Saved trained model and tokenizer
---

### 🌐 Application Folder

The textsummarizerapp folder contains the application:

FastAPI backend
Model loading
Text preprocessing
Summary generation
Web interface


---



## 🔄 Application Workflow



User enters conversation
          ↓
     Text Cleaning
          ↓
      Tokenization
          ↓
     T5-small Model
          ↓
    Text Generation
          ↓
   Generated Summary

The application provides:

GET  /
POST /summarize/

The / route displays the web interface, while /summarize/ processes the conversation and returns the generated summary.



---
## 💻 Example


### Input



John: Hey Sarah, did you finish the project report?


Sarah: Not yet. I completed the research section, but I still need to work on the results and conclusion.


John: I finished my part yesterday. Do you want me to help you with the results section?


Sarah: That would be great. If we finish it today, we can review the complete report tomorrow.


John: Sure. Let's work on it together this afternoon and submit the report before the deadline.
Generated Summary

---

# 🚀 Installation

1. Clone the Repository
```text
git clone [https://github.com/Akshat-singh1705/text-summarizer.git](https://github.com/Akshat-singh1705/text-summarizer.git)
cd text-summarizer
```
3. Create a Virtual Environment
Windows:
```
python -m venv venv
venv\Scripts\activate
```
macOS / Linux :
```
python3 -m venv venv
source venv/bin/activate
```
5. Install Dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Make sure the trained model exists inside:

```
text summarizer model/
└── saved_summary_model/
```

Then navigate to the application folder:
```
cd textsummarizerapp
```
Start the FastAPI server:
```
uvicorn app:app --reload
```
The application will run at:
```
http://127.0.0.1:8000
```
Open the URL in your browser.

---

### 📚 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the application, open:

***http://127.0.0.1:8000/docs***

You can test the ***/summarize/*** endpoint directly from the Swagger interface.

Example Request
```
{
    "dialogue": "John: Are you coming to the meeting? Sarah: Yes, I will be there at 3 PM."
}
```
Example Response
```
{
    "summary": "Sarah will attend the meeting at 3 PM."
}
```

---
