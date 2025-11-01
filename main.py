import streamlit as st
import pyqrcode
from io import BytesIO

st.title(" QR Kod Oluşturucu")

data = st.text_input("QR verisini giriniz")
boyut = st.slider("Boyut seç", 5, 30, 10)

if st.button("Oluştur"):
    if data.strip() != "":
        # QR kodu oluştur
        qr = pyqrcode.create(data)

        # Belleğe kaydet
        buffer = BytesIO()
        qr.png(buffer, scale=boyut)
        buffer.seek(0)

        # QR'ı göster
        st.image(buffer, caption="Oluşturulan QR Kodu")

        # İndirilebilir hale getir
        st.download_button(
            label="QR Kodunu indir",
            data=buffer,
            file_name="qr.png",
            mime="image/png"
        )
    else:
        st.warning("️ Lütfen QR verisini giriniz!")
