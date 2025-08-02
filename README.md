# 👁️ Retinopathy of Prematurity (ROP) Stage Classifier

This project builds an AI model to classify retinal fundus images into 3 clinical stages of **Retinopathy of Prematurity (ROP)**—**No ROP**, **Mild ROP**, and **Severe ROP**—using deep learning with **DenseNet121**. A web-based UI is included using **Streamlit** for easy interaction.

---

##  Dataset Description

The dataset is a custom collection curated from:

- `images_stack_without_captions` from the Kaggle ROP dataset archive.
- Metadata Excel: `infant_retinal_database_info.xlsx`.
- Manually added images to boost underrepresented classes (especially Mild ROP).

###  Final Class Distribution:

| Class       | Count  |
|-------------|--------|
| No ROP      | 2,893  |
| Mild ROP    | 334    |
| Severe ROP  | 3,297  |

###  Folder Structure:
organized_dataset/
├── No_ROP/
├── Mild_ROP/
└── Severe_ROP/

---

##  Model

- ✅ Base Model: `DenseNet121` (ImageNet pretrained)
- 🔁 Fine-tuned: last 30 layers using Low LR (1e-5)
- 🎯 Output: 3-class softmax
- 🧮 Optimizer: Adam
- 👁️ Input size: 224x224 RGB
- 💡 Augmentation:
  - Mild ROP: heavy (flip, contrast, brightness)
  - No/Severe ROP: moderate

---

##  Clinical Stage Mapping

| Stage      | Interpretation                                                                                      |
|------------|-----------------------------------------------------------------------------------------------------|
| No ROP     | No evidence of retinopathy. No treatment required.                                                  |
| Mild ROP   | May self-resolve or progress. Needs monitoring. Some cases need treatment to prevent complications. |
| Severe ROP | Urgent care needed to prevent retinal detachment or permanent vision loss.                          |

---

## 🌐 Web App (Streamlit)

A lightweight, browser-based app where users can upload fundus images and get predicted ROP stages with medical interpretation.
<img width="1440" height="777" alt="Screenshot 2025-08-03 at 12 06 08 AM" src="https://github.com/user-attachments/assets/dc3abbaa-37c9-4080-98d7-8aef54d2b12e" />
<img width="1440" height="775" alt="Screenshot 2025-08-03 at 12 05 48 AM" src="https://github.com/user-attachments/assets/85fab297-802b-4fd7-85e6-a80003ca066d" />
<img width="1440" height="900" alt="Screenshot 2025-08-03 at 12 06 45 AM" src="https://github.com/user-attachments/assets/66ef3d62-de81-4156-bfbd-b2a06a367210" />

### 🧾 Features


- Upload image
- Predict class & show probability
- Display clinical message

  

### ▶️ Run locally:

```bash
streamlit run app.py

