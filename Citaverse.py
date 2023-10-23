# Importer les bibliothèques nécessaires
import streamlit as st
import pydeck


# Configurer la page
st.set_page_config(
    page_title="Plateforme d'Engagement Citoyen",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Créer un menu latéral avec différentes pages
menu = ["Accueil", "Prédiction des Surverses",
        "Engagement Citoyen", "Visualisation", "À Propos", "Découvrir"]
choix = st.sidebar.selectbox("Choisir une page", menu)

# Créer des fonctions pour chaque page


def accueil():
    st.title("Citaverse: Plateforme d'Engagement Citoyen")
    col1, col2 = st.beta_columns(2)

    col1.image("https://github.com/PhilScalab/Citaverse/blob/main/_12bcb1a9-7d43-417f-9cf4-9a6b5c0ffdee.jpeg",
               caption="Image de présentation", use_column_width=True, output_format='JPEG')

    col2.subheader("À propos de l'outil")
    col2.success("""
    ### Bienvenue à Citaverse
    **Citaverse** est une plateforme innovante conçue pour sensibiliser et engager les citoyens à la problématique des surverses d'eaux usées. À travers une interface conviviale, notre outil offre une vue en temps réel des risques de surverse basée sur les prévisions météorologiques, et incite activement les citoyens à adopter une **consommation d'eau responsable** pendant les périodes critiques. Au-delà d'une simple plateforme d'information, Citaverse est un **appel à l'action** pour préserver nos ressources en eau et protéger notre environnement.
    Ce projet est né de la volonté d'un participant engagé dans le programme Ocean Bridge Canada 2023, un programme transformateur destiné aux jeunes Canadiens désireux de devenir des ambassadeurs des océans. Ocean Bridge vise à connecter et autonomiser la jeunesse à travers le pays pour adopter une culture de service en faveur de la conservation marine et des eaux douces. C'est dans cet esprit de sensibilisation et d'action que Citaverse a été conceptualisé, incarnant l'idéal d'une citoyenneté active et informée, prête à agir pour un futur durable.
    Au cœur de notre démarche se trouve une conviction forte : **chaque geste compte**. Et avec les bons outils et les bonnes informations, nous pouvons tous contribuer à faire la différence. Rejoignez-nous dans cette mission pour un avenir plus bleu et plus vert.
    """)
    col2.info("""
    _Les données fournies par le Partenariat Données Québec sont utilisées conformément à la licence Creative Commons Attribution 4.0 International. Les données météorologiques fournies par Environment and Climate Change Canada sont utilisées conformément au "Limited Use Software and Data Product Licence Agreement". Tout usage, distribution ou modification de ces données doit fournir une attribution appropriée._
    """)

    st.subheader("Sources de données")
    st.warning("""
    - **Ouvrages de surverse - Débordements d'eaux usées**: 
        - Type: Données
        - Taille: 11 Mo
        - Source: [Partenariat Données Québec](https://www.donneesquebec.ca/recherche/dataset/64372248-d60b-4a2b-a326-bf34c721e568/resource/54190fb7-df03-4a56-b6f3-3059c0b8f1fd/download/ouvrages-de-surverse-debordements-2023-06-20.csv)
        - Licence: [Attribution (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.fr)
        - Description des champs : Fournie dans les méta-données

    - **Prévisions météorologiques**:
        - Source: [Weatherstat basé sur les données d'Environnement et Changement climatique Canada and Climate Canada](https://www.weatherstats.ca/)
        - Licence: "Environnement et Changement climatique Canada ne garantit pas la qualité, l'exactitude ou l'exhaustivité des informations ou des données. Ces informations et données sont fournies "TELLES QUELLES" sans garantie ni condition de quelque nature que ce soit. L'utilisation de ces données est basée sur le "Limited Use Software and Data Product Licence Agreement" d'Environnement et Changement climatique Canada. Tout usage ultérieur est soumis à cette licence et nécessite une attribution appropriée : basée sur les données d'Environnement et Changement climatique Canada."
    """)


def prediction():
    st.title("Prédiction des Surverses")
    st.write("""
    Ici, nous utiliserons des modèles pour prédire les surverses basées sur les précipitations.
    """)
    st.image("Logo/Pluie-reseau.jpeg",
             caption="Prédiction selon les prévisions pluviométriques", use_column_width=True, output_format='JPEG')


def engagement():
    st.title("Engagement Citoyen")
    st.write("""
    Engagez-vous en tant que citoyen pour économiser l'eau pendant les périodes critiques.
    """)

    ville = st.selectbox("Choisir une ville", [
                         "Sélectionnez une ville", "Montréal", "Trois-Rivières", "Québec"])
    if ville != "Sélectionnez une ville":
        st.write(f"Vous avez sélectionné: {ville}")

        # Valeurs initiales
        eau_economisee = 0
        max_eau = 1000

        # Actions pour économiser l'eau
        if st.checkbox("Utiliser le lave-vaisselle de manière efficace"):
            eau_economisee += 150

        if st.checkbox("Prendre une douche courte"):
            eau_economisee += 100

        if st.checkbox("Arrêter le robinet pendant le brossage des dents"):
            eau_economisee += 10

        if st.checkbox("Utiliser une chasse d'eau à faible débit"):
            eau_economisee += 20

        if st.checkbox("Arroser le jardin tôt le matin ou tard le soir"):
            eau_economisee += 50

        # Afficher la jauge
        st.write(
            f"Eau économisée: {eau_economisee} L sur {max_eau} L possibles")
        st.progress(eau_economisee / max_eau)


def visualisation():
    st.title("Visualisation")
    st.write("""
    Visualisez la quantité d'eau économisée grâce aux engagements citoyens.
    """)

    # Coordonnées et valeurs fictives pour Montréal, Québec et Trois-Rivières
    data = [
        {"lat": 45.5017, "lon": -73.5673, "value": 15},  # Montréal
        {"lat": 46.8139, "lon": -71.2082, "value": 10},  # Québec
        {"lat": 46.3432, "lon": -72.5419, "value": 5}    # Trois-Rivières
    ]

    # Création d'une carte avec pydeck
    heatmap_layer = pydeck.Layer(
        "HeatmapLayer",
        data,
        opacity=0.9,
        get_position=["lon", "lat"],
        get_weight="value",
        threshold=0.05,
        radiusPixels=50,
    )

    view_state = pydeck.ViewState(
        latitude=46.8139, longitude=-71.2082, zoom=6, bearing=0, pitch=45
    )

    r = pydeck.Deck(
        layers=[heatmap_layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/light-v9",
    )

    st.pydeck_chart(r)


def a_propos():
    st.title("À Propos")
    st.write("""
    À propos de cette plateforme et de l'équipe qui l'a créée.
    """)


import streamlit as st
import pydeck as pdk

# Sample coordinates near Tadoussac
ANIMAL_LOCATIONS = {
    "whale": [48.1460, -69.7242],
    "seal": [48.1530, -69.7150],
    "beluga": [48.1400, -69.7300],
}

ANIMAL_DESCRIPTIONS = {
    "whale": "Whales are large marine mammals known for their impressive size and majestic presence.",
    "seal": "Seals are semi-aquatic mammals that are well-adapted to life in cold waters.",
    "beluga": "Belugas are small, white whales known for their bulbous forehead and social behavior."
}

def display_animal_map():
    map_data = [{
        "animal": animal,
        "latitude": loc[0],
        "longitude": loc[1],
        "description": ANIMAL_DESCRIPTIONS[animal]
    } for animal, loc in ANIMAL_LOCATIONS.items()]

    view_state = pdk.ViewState(
        latitude=48.1460,
        longitude=-69.7242,
        zoom=10,
        pitch=40.5,
        bearing=-27.36
    )

    layer = pdk.Layer(
        type="ScatterplotLayer",
        data=map_data,
        get_position="[longitude, latitude]",
        get_radius=200,
        get_fill_color="[255, 140, 0]",
        pickable=True
    )

    r = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[layer]
    )
    
    st.pydeck_chart(r)

    # Check if a point was clicked
    if st.session_state.get("clicked", None):
        clicked_data = st.session_state.clicked
        st.write(ANIMAL_DESCRIPTIONS.get(clicked_data["object"]["animal"], ""))
    



# Associer chaque fonction à son menu correspondant
if choix == "Accueil":
    accueil()
elif choix == "Prédiction des Surverses":
    prediction()
elif choix == "Engagement Citoyen":
    engagement()
elif choix == "Visualisation":
    visualisation()
elif choix == "À Propos":
    a_propos()
elif choix == "Découvrir":
    display_animal_map()
