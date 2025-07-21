# 📞 Phone Call Assistant – Real-Time Voice Transcription Bot

A professional voice transcription and intent recognition assistant built for automating customer support interactions. This lightweight tool uses speech recognition and Retrieval-Augmented Generation (RAG) to identify user intent and streamline communication.

## 🚀 Features
- 🎙️ Real-time microphone input
- ✍️ Accurate speech-to-text transcription
- 🧠 Intent recognition via RAG
- 🔄 Flask-based backend API
- 🌐 Clean and minimal frontend (HTML + JS)

## 📁 Project Structure
```
Phone-call-assistant/
├── backend/
│   ├── app.py              # Flask server
│   ├── intent_rag.py       # Intent detection logic
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # UI layout
│   └── script.js           # Voice capture & API calls
```

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Suryadeep615122/Phone-call-assistant.git
cd Phone-call-assistant
```

### 2. Set Up Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 3. Launch Frontend
Open `frontend/index.html` in your browser.

## 🧠 How It Works
1. User speaks into mic.
2. Audio is transcribed using SpeechRecognition.
3. Text is passed to RAG engine to infer intent.
4. Response is generated/displayed accordingly.

## 📌 Future Enhancements
- Deploy on cloud (Render/Heroku)
- Store session transcripts
- Add multi-language support
- Integrate with CRM/Support platforms

## 👤 Author
**Suryadeep**  
GitHub: [@Suryadeep615122](https://github.com/Suryadeep615122)

## 📄 License
Licensed under the [MIT License](LICENSE).
