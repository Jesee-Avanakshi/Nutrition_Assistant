import streamlit as st

st.set_page_config(page_title="About — Healthy Diet Assistant", page_icon="ℹ️")

st.title("About Healthy Diet Assistant")
st.write("")
st.markdown("---")

st.markdown("""
## 🥗 Healthy Diet Assistant — RAG

This application is an AI-powered **Retrieval-Augmented Generation (RAG)** system designed to answer nutrition-related questions using *verified* and *trusted* health guidelines.

It retrieves information only from scientifically backed sources and generates clear, evidence-aligned answers.

---

## 🎯 Objective of the Application

The goal of this chatbot is to:

- Provide **reliable nutrition guidance** extracted from global health authorities  
- Teach users about **healthy dietary patterns**  
- Assist students, researchers, and the public with **fast, accurate answers**  
- Demonstrate the power of **RAG + LLM** systems in real-world applications  

This tool is educational and designed for learning and awareness—not for medical diagnosis.

---

## 🧠 Data Sources Used

All knowledge used by this system comes from **trusted organizations**:

### **1️⃣ World Health Organization (WHO)**
- Healthy Diet Factsheets  
- Obesity and Overweight  
- Food Safety  
- Sugar, Salt, Fat intake recommendations  

### **2️⃣ USDA — Dietary Guidelines for Americans**
- 2020–2025 Dietary Guidelines  
- MyPlate recommendations  
- USDA food grouping standards  

### **3️⃣ Harvard School of Public Health**
- Healthy Eating Plate  
- Updated dietary guidelines  
- Nutrition research summaries  

### **4️⃣ Diabetes Canada**
- Carbohydrate counting  
- Healthy eating basics  
- Sugar intake guidelines  

These PDFs and webpages were converted into a unified structured dataset and stored inside a **Chroma vector database**.

---

## 🛠️ **How It Works (Simple Explanation)**

1. **You ask a question**  
2. The system searches for the most relevant information in the vector database  
3. Retrieved context is passed into a LLM """)

