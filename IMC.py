import streamlit as st

st.title("💪 Calcul de l'IMC (Indice de Masse Corporelle)")

st.write("Entrez votre taille et votre poids pour savoir si vous êtes en surpoids, normal, etc.")

# --- INPUTS ---
taille = st.number_input(
    "Entrez votre taille (en mètres)", 
    min_value=0.50, 
    max_value=2.50, 
    step=0.01
)

poids = st.number_input(
    "Entrez votre poids (en kg)", 
    min_value=10.0, 
    max_value=300.0, 
    step=0.1
)

# --- CALCUL ---
if st.button("Calculer l'IMC"):
    if taille > 0:
        imc = poids / (taille ** 2)
        st.write(f"### ➤ Votre IMC est : **{imc:.2f}**")

        # --- INTERPRETATION ---
        if imc < 18.5:
            st.warning("🔸 Vous êtes en insuffisance pondérale (trop maigre).")
        elif 18.5 <= imc < 25:
            st.success("✅ Votre poids est normal.")
        elif 25 <= imc < 30:
            st.info("⚠️ Vous êtes en surpoids.")
        else:
            st.error("❗ Vous êtes en obésité.")
    else:
        st.error("Veuillez entrer une taille valide.")

