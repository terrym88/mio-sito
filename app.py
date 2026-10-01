import streamlit as st

st.title("🚀 Il mio Super Sito Web!")


st.image("https://images.unsplash.com/photo-1543466835-00a7907e9de1", caption="Un simpatico cucciolo")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.write("---")


nome = st.text_input("Come ti chiami?")
effetto = st.radio("Scegli un effetto:", ["Palloncini", "Neve"])

if st.button("Saluta!"):
    if nome:
        st.success(f"Ciao {nome}! Benvenuto!")
        if effetto == "Palloncini":
            st.balloons()
        else:
            st.snow()
    else:
        st.warning("Inserisci prima il tuo nome!")

st.write("---")


st.subheader("🧠 Quiz del giorno")
risposta = st.radio("Qual è la capitale d'Italia?", ["Milano", "Roma", "Napoli"])

if risposta == "Roma":
  
    st.success("Esatto! 🎉")
    st.balloons()  # Lancia i palloncini di festeggiamento
else:
       st.error("Risposta errata, riprova!")
st.info("💡 Suggerimento: È la città dove si trova il Colosseo!")

data = st.date_input("Quando sei nato?")

voto = st.slider("Da 1 a 10, quanto ti piace questo sito?", 1, 10, 10)
st.write(f"Grazie per il tuo voto: {voto}/10!")
