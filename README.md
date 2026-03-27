# 🚀 News Signal Monitoring System

## 📌 Overview
This project automatically detects important business signals from news articles using RSS feeds and keyword-based classification.

## ❗ Problem
Tracking business events like funding, hiring, and acquisitions manually is inefficient.

## 💡 Solution
A Python-based system that:
- Fetches news from RSS feeds
- Detects important signals using keywords
- Classifies events into categories
- Stores structured data for analysis

## ⚙️ Workflow
1. Fetch news using RSS feeds  
2. Parse articles  
3. Detect signals using keywords  
4. Filter meaningful events  
5. Store data in CSV  
6. Remove duplicates automatically  

## 🛠️ Tech Stack
- Python
- Pandas
- Feedparser

## 📊 Signal Categories
- Funding
- Acquisition
- Partnership
- Launch
- Hiring
- Leadership

## 📈 Output
Structured dataset with:
- Title
- Signal Type
- Link
- Published Date
- Captured Date

## 🚀 How to Run

```bash
pip install -r requirements.txt
python news_signal_monitor.py
```

## 🔐 Note
This project uses publicly available RSS feeds. No private data is used.