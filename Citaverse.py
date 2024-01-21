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
menu = ["Accueil", "Éducation","Prédiction des Surverses",
        "Engagement Citoyen", "Visualisation", "À Propos", "Découvrir"]
choix = st.sidebar.selectbox("Choisir une page", menu)

# Créer des fonctions pour chaque page


def accueil():
    st.title("Citaverse: Plateforme d'Engagement Citoyen")
    col1, col2 = st.beta_columns(2)

    htp="https://raw.githubusercontent.com/PhilScalab/Citaverse/blob/main/_12bcb1a9-7d43-417f-9cf4-9a6b5c0ffdee.jpeg"
    col1.image(htp, caption= 'Citaverse', width=350)


   # col1.image("",
              # caption="Image de présentation", use_column_width=True, output_format='JPEG')

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

def education():
    st.title("🌊 Comprendre le traitement des eaux usées à Montréal")

    # Introduction
    st.subheader("Comment les eaux usées de Montréal sont-elles traitées ?")
    st.info("""
    La plupart des Montréalais ignorent que Montréal possède la troisième plus grande usine de traitement des eaux usées au monde! L'usine Jean-R. Marcotte, construite en 1984 et située dans l'est de Montréal, traite presque la moitié des eaux usées du Québec. Cela représente entre 2,5 et 7,6 millions de mètres cubes d'eau traitée par jour.

    En savoir plus dans cet article de la Fondation Rivière:
    [Article de la Fondation Rivière](https://fondationrivieres.org/en/coulisses-station-depuration-eaux-usees-montreal-2/)
    """)

    # Mises à jour à venir
    st.subheader("🆕 Mises à jour à venir dans le traitement des eaux usées")
    st.warning("""
    D'ici 2025, Montréal prévoit de moderniser son processus de traitement des eaux usées en ajoutant une étape appelée "ozonation". L'ozonation consiste à injecter de l'ozone dans l'eau pendant le processus de traitement. Cela aide à éliminer les virus, les bactéries et les produits pharmaceutiques nocifs.

    Pour en savoir plus sur la mise à jour de la Ville de Montréal:
    [Mise à jour de la Ville de Montréal](https://montreal.ca/en/articles/ozone-disinfection-construction-jean-r-marcotte-water-treatment-station-27451)
    """)

    # Débordement des effluents
    st.subheader("💦 Comment cela conduit-il à un débordement des effluents ?")
    st.write("""
    Lorsque l'eau entrant dans le système dépasse sa capacité de traitement, l'excès d'eau est déversé dans la rivière Saint-Laurent. Cela se produit généralement lors de la fonte des neiges, de fortes pluies ou lors de travaux de construction.

    Pour plus d'informations détaillées:
    [Ressource Réseau Femmes Environnement](https://reseaufemmesenvironnement.org/blogue/overflow)
    """)

    # Impacts des débordements d'effluents
    st.subheader("🌱 Impacts des débordements d'effluents")
    st.write("""
    **Sur la biodiversité :** Enrichissement en nutriments entraînant une croissance indésirable des algues et l'eutrophisation des masses d'eau. Perte de biodiversité dans le fleuve Saint-Laurent, y compris les impacts sur les espèces de crustacés d'eau douce.

    **Pour les citoyens :** Risques accrus d'inondation, contamination de l'eau potable, interdiction d'activités récréatives et dégradation esthétique des espaces naturels.

    **Sur l'économie :** Perte d'attractivité touristique et diminution de la valeur des propriétés le long du fleuve.

    **Pour en savoir plus, consultez la Gestion Durable des eaux pluviales :**
    [Ressource GDEP](https://robvq.qc.ca/gdep/)
    """)

    # Réduction de la consommation d'eau
    st.subheader("💧 Que pouvons-nous faire pour réduire notre consommation d'eau et donc les débordements ?")
    st.write("""
    Réduire notre propre consommation d'eau a un impact considérable sur les débordements. En diminuant l'eau que nous utilisons dans nos foyers, nous réduisons l'eau qui en sort.

    Conseils pour réduire la consommation d'eau de la Fondation David Suzuki :
    [Conseils de la Fondation David Suzuki](https://fr.davidsuzuki.org/mode-de-vie/chaque-goutte-compte-conseils-pour-economiser-eau/)

    Recommandations d'Hydro-Québec pour une utilisation efficace de l'eau chaude :
    [Conseils d'Hydro-Québec](https://www.hydroquebec.com/residentiel/mieux-consommer/reduire-consommation-eau.html)
    """)

    # Actions de Montréal
    st.subheader("🏙️ Que fait Montréal ?")
    st.write("""
    Montréal veille à la propreté des cours d'eau autour de la ville et construit de nouveaux bassins de rétention pour limiter les débordements.

    Efforts de la Ville de Montréal :
    [Eaux de Montréal](https://montreal.ca/en/topics/water-quality-waterways)

    Article de la Montreal Gazette sur le bassin de rétention d'eau :
    [Article de la Montreal Gazette](https://montrealgazette.com/news/local-news/visit-to-montreals-largest-underground-water-retention-basin?fbclid=IwAR2JGorZzMwBqsfQncpT83GuVp8zKQ0_48-TZbAKttnJNBhZ_Si9nLJ_er4)
    """)
    
    st.title("🌊 Understanding Montreal’s Wastewater Treatment")

    # Introduction
    st.subheader("How is Montreal’s Wastewater handled?")
    st.info("""
    Most Montrealers don’t know that Montreal actually has the third largest wastewater treatment plant in the world! The Jean-R. Marcotte plant, built in 1984, and located in Eastern Montreal, treats almost half of Quebec’s wastewater. This represents between 2.5 and 7.6 million cubic meters of water treated per day.

    Read more about the process in this article from the Fondation Rivière:
    [Fondation Rivière Article](https://fondationrivieres.org/en/coulisses-station-depuration-eaux-usees-montreal-2/)
    """)

    # Upcoming Updates
    st.subheader("🆕 Upcoming Updates in Wastewater Treatment")
    st.warning("""
    By 2025, Montreal is planning to update its wastewater treatment process by adding a step called “Ozonation”. Ozonation is the process of injecting ozone gas into the water during the treatment process. This helps to remove harmful viruses, bacteria, and pharmaceutical products.

    Learn more from Ville de Montréal's update:
    [Ville de Montréal Update](https://montreal.ca/en/articles/ozone-disinfection-construction-jean-r-marcotte-water-treatment-station-27451)
    """)

    # Effluent Overflow
    st.subheader("💦 How does this lead to effluent overflow?")
    st.write("""
    At times when water entering the system exceeds its treatment capacity, the excess water is overflowed into the St. Lawrence River. This usually happens during snow melt, heavy rainfall, or construction.

    For detailed insights:
    [Reseau Femmes Environnement Resource](https://reseaufemmesenvironnement.org/blogue/overflow)
    """)

    # Impacts of Effluent Overflow
    st.subheader("🌱 Impacts of Effluent Overflow")
    st.write("""
    **Biodiversity:** Nutrient enrichment leading to undesirable algal growth and eutrophication of water bodies. Loss of biodiversity in the St. Lawrence River, including impacts on freshwater crustacean species.

    **For Citizens:** Increased risk of flooding, contamination of drinking water, prohibition of recreational activities, and aesthetic damage to natural areas.

    **On the Economy:** Loss of tourist appeal and reduced property values along the river.

    **Learn more from Gestion Durable des eaux pluviales:**
    [GDEP Resource](https://robvq.qc.ca/gdep/)
    """)

    # Reducing Water Consumption
    st.subheader("💧 What can we do to reduce our water consumption and thereby water overflow?")
    st.write("""
    Reducing our own water consumption greatly impacts water overflow. By reducing the water we take into our household, we reduce the water leaving our household.

    Tips on reducing water usage from David Suzuki Foundation:
    [David Suzuki Foundation Tips](https://davidsuzuki.org/living-green/make-every-drop-count-water-conservation-tips/?gad_source=1&gclid=CjwKCAiAjrarBhAWEiwA2qWdCHcCO8yqba8Pf2xZWIPTVhAFMK9S3-97ERQS7qQ8hAFwTsB809ztDRoCVBYQAvD_BwE)

    Hydro Quebec's recommendation on using hot water efficiently:
    [Hydro Quebec Tips](https://www.hydroquebec.com/residential/energy-wise/maximize-water-heater-use.html)
    """)

    # Montreal's Efforts
    st.subheader("🏙️ What is Montreal doing?")
    st.write("""
    Montreal ensures the waterways around the city are clean and is building new water retention basins to limit overflows.

    City of Montreal's efforts:
    [City of Montreal Waterways](https://montreal.ca/en/topics/water-quality-waterways)

    Montreal Gazette article on water retention basin:
    [Montreal Gazette Article](https://montrealgazette.com/news/local-news/visit-to-montreals-largest-underground-water-retention-basin?fbclid=IwAR2JGorZzMwBqsfQncpT83GuVp8zKQ0_48-TZbAKttnJNBhZ_Si9nLJ_er4)
    """)

    # References and Additional Resources
    st.subheader("🔗 References and Additional Resources")
    st.write("""
    Check out these links for more detailed information and additional resources on Montreal's wastewater treatment and related environmental issues.
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
import pandas as pd

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
    # Convert animal locations to a DataFrame for st.map
    df = pd.DataFrame({
        'animal': list(ANIMAL_LOCATIONS.keys()),
        'lat': [loc[0] for loc in ANIMAL_LOCATIONS.values()],
        'lon': [loc[1] for loc in ANIMAL_LOCATIONS.values()]
    })
    
    st.map(df)

    # Using a radio button for the user to select which point they clicked
    clicked_animal = st.radio("Which animal did you click on?", list(ANIMAL_LOCATIONS.keys()))
    st.write(ANIMAL_DESCRIPTIONS[clicked_animal])


# Associer chaque fonction à son menu correspondant
if choix == "Accueil":
    accueil()
elif choix == "Éducation":
    education()
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
