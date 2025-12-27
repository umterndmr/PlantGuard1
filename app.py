import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# 1. Sayfa Tasarımı
st.set_page_config(page_title="PlantGuard AI", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 PlantGuard: Hibrit Bitki Doktoru")
st.write("Sistem şu an **Domates, Biber ve Patates** hastalıklarını teşhis edebilir.")

# 2. Modeli ve Etiketleri Yükle
@st.cache_resource
def load_resources():
    # TFLite Modelini Yükle
    interpreter = tf.lite.Interpreter(model_path="plantguard_model.tflite")
    interpreter.allocate_tensors()
    
    # Senin verdiğin 7 sınıf
    labels = [
        "Pepper Bell - Bakteriyel Leke",
        "Pepper Bell - Sağlıklı",
        "Patates - Erken Yanıklık",
        "Patates - Sağlıklı",
        "Domates - Bakteriyel Leke",
        "Domates - Geç Yanıklık",
        "Domates - Sağlıklı"
    ]
    return interpreter, labels

interpreter, labels = load_resources()

# 3. Kullanıcıdan Resim Al
file = st.file_uploader("Yaprak fotoğrafını buraya sürükleyin veya seçin...", type=["jpg", "png", "jpeg"])

if file:
    col1, col2 = st.columns(2)
    
    img = Image.open(file).convert("RGB")
    with col1:
        st.image(img, caption="Analiz Edilen Resim", use_container_width=True)
    
    # Resmi Hazırla
    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Tahmin Mekanizması
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    idx = np.argmax(output_data)
    confidence = output_data[0][idx] * 100

    with col2:
        st.subheader("Analiz Sonucu")
        if confidence > 50:
            st.success(f"**Teşhis:** {labels[idx]}")
            st.metric(label="Güven Oranı", value=f"%{confidence:.2f}")
        else:
            st.warning("Model tam emin olamadı. Lütfen daha net bir fotoğraf yükleyin.")
            st.write(f"En yakın tahmin: {labels[idx]} (%{confidence:.2f})")