🌿 PlantGuard: Hibrit Bitki Hastalığı Teşhis Sistemi
PlantGuard, tarım teknolojileri ve derin öğrenmeyi birleştiren, domates, biber ve patates yapraklarındaki hastalıkları anında tespit eden yapay zeka tabanlı bir web uygulamasıdır.

🚀 Canlı Deneyim
Uygulamayı tarayıcınızdan anında test edebilirsiniz: 👉 [(https://huggingface.co/spaces/Wholesale001/PlantGuard)]

🛠️ Teknik Özellikler
Mimari: EfficientNetB0 (Transfer Learning) kullanılarak geliştirilmiştir.

Doğruluk Payı: Model, hibrit veri seti üzerinde %99.68 val_accuracy başarısına ulaşmıştır.

Optimizasyon: Mobil ve web uyumluluğu için model TFLite formatına dönüştürülmüştür.

Arayüz: Kullanıcı dostu ve hızlı bir deneyim için Streamlit kullanılmıştır.

📊 Desteklenen Sınıflar (7 Sınıf)
Modelimiz şu an aşağıdaki bitki ve durumları yüksek güvenle teşhis edebilmektedir:

Biber: Bakteriyel Leke ve Sağlıklı Yaprak

Patates: Erken Yanıklık ve Sağlıklı Yaprak

Domates: Bakteriyel Leke, Geç Yanıklık ve Sağlıklı Yaprak

📂 Proje Yapısı
app.py: Streamlit web arayüzü kodları.

plantguard_model.tflite: Optimize edilmiş derin öğrenme modeli.

labels.txt: Sınıf etiketlerinin listesi.

requirements.txt: Gerekli Python kütüphaneleri.

🔧 Yerel Kurulum
Projeyi kendi bilgisayarınızda çalıştırmak için:

Depoyu klonlayın: git clone https://github.com/kullaniciadin/PlantGuard.git

Kütüphaneleri kurun: pip install -r requirements.txt

Uygulamayı başlatın: streamlit run app.py

💡 Geliştirici Notu
Bu proje, dengesiz veri setlerinin temizlenmesi ve hibrit modellerin optimizasyonu süreçlerini kapsayan uçtan uca bir derin öğrenme çalışmasıdır.
