import pyautogui as p
import time
import math
import random


VIDEOS = [
    # travel
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A1_MINUS_VOCABULARY_COMMENT_VOYAGER/activity/FR_FR_A1_MINUS_VOCABULARY_COMMENT_VOYAGER_VIDEO_ANIMATION_LECON_2_JE_VAIS_EN_TRAIN_EN_BUS/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A1_MINUS_VOCABULARY_CONTROLE_DES_PASSEPORTS/activity/FR_FR_A1_MINUS_VOCABULARY_CONTROLE_DES_PASSEPORTS_VIDEO_ANIMATION_LECON_4_A_L_AEROPORT/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A1_MINUS_VOCABULARY_TYPES_DE_TRANSPORT/activity/FR_FR_A1_MINUS_VOCABULARY_TYPES_DE_TRANSPORT_VIDEO_ANIMATION_LECON_1_LES_TRANSPORTS/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A1_VOCABULARY_PARLER_DE_PROBLEMES_DE_TRANSPORTS_ET_DE_VOYAGES/activity/FR_FR_A1_VOCABULARY_PARLER_DE_PROBLEMES_DE_TRANSPORTS_ET_DE_VOYAGES_VIDEO_ANIMATION_CEDRIC_REND_VISI/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A1_VOCABULARY_PARLER_DE_SES_PROJETS_DE_VACANCES/activity/FR_FR_A1_VOCABULARY_PARLER_DE_SES_PROJETS_DE_VACANCES_VIDEO_ANIMATION_LES_PROCHAINES_VACANCES_DE_CED/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A2_VOCABULARY_CIRCULER_EN_VILLE_PARTIE_1/activity/FR_FR_A2_VOCABULARY_CIRCULER_EN_VILLE_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A2_VOCABULARY_PARLER_D_UN_VOYAGE_PARTIE_1/activity/FR_FR_A2_VOCABULARY_PARLER_D_UN_VOYAGE_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A2_VOCABULARY_RACONTER_SES_VACANCES_PARTIE_1/activity/FR_FR_A2_VOCABULARY_RACONTER_SES_VACANCES_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_A2_VOCABULARY_SE_DEPLACER_EN_VILLE_PARTIE_1/activity/FR_FR_A2_VOCABULARY_SE_DEPLACER_EN_VILLE_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_B1_VOCABULARY_EN_VOYAGE_CHOISIR_UN_MOYEN_DE_TRANSPORT/activity/FR_FR_B1_VOCABULARY_EN_VOYAGE_CHOISIR_UN_MOYEN_DE_TRANSPORT_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_B1_VOCABULARY_LOGER_A_L_HOTEL/activity/FR_FR_B1_VOCABULARY_LOGER_A_L_HOTEL_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_B1_VOCABULARY_PRENDRE_L_AVION_DANS_LE_TERMINAL/activity/FR_FR_B1_VOCABULARY_PRENDRE_L_AVION_DANS_LE_TERMINAL_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_B1_VOCABULARY_PRENDRE_L_AVION_A_L_ENREGISTREMENT/activity/FR_FR_B1_VOCABULARY_PRENDRE_L_AVION_A_L_ENREGISTREMENT_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/TRANSPORT_TRAVEL/lesson/FR_FR_C1_VOCABULARY_VOYAGER_AVEC_DES_DENREES_ALIMENTAIRES/activity/FR_FR_C1_VOCABULARY_VOYAGER_AVEC_DES_DENREES_ALIMENTAIRES_VIDEO/video",
    # Hospital.
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_A2_VOCABULARY_ALLER_A_L_HOPITAL_PARTIE_1/activity/FR_FR_A2_VOCABULARY_ALLER_A_L_HOPITAL_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_A2_VOCABULARY_SE_RENDRE_CHEZ_LE_DOCTEUR_PARTIE_1/activity/FR_FR_A2_VOCABULARY_SE_RENDRE_CHEZ_LE_DOCTEUR_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_LES_ACCIDENTS_DOMESTIQUES/activity/FR_FR_B1_VOCABULARY_LES_ACCIDENTS_DOMESTIQUES_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_PRENDRE_RENDEZ_VOUS_CHEZ_LE_MEDECIN/activity/FR_FR_B1_VOCABULARY_PRENDRE_RENDEZ_VOUS_CHEZ_LE_MEDECIN_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_QUELQUES_GESTES_HABITUELS/activity/FR_FR_B1_VOCABULARY_QUELQUES_GESTES_HABITUELS_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_RESTER_EN_FORME/activity/FR_FR_B1_VOCABULARY_RESTER_EN_FORME_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_SE_SENTIR_MAL/activity/FR_FR_B1_VOCABULARY_SE_SENTIR_MAL_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_SYMPTOMES_ET_DIAGNOSTICS/activity/FR_FR_B1_VOCABULARY_SYMPTOMES_ET_DIAGNOSTICS_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_UN_ACCIDENT_DE_LA_ROUTE/activity/FR_FR_B1_VOCABULARY_UN_ACCIDENT_DE_LA_ROUTE_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_B1_VOCABULARY_ETRE_MALADE/activity/FR_FR_B1_VOCABULARY_ETRE_MALADE_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_C1_VOCABULARY_IDENTIFIER_LES_INEGALITES_DE_SOINS_DE_SANTE/activity/FR_FR_C1_VOCABULARY_IDENTIFIER_LES_INEGALITES_DE_SOINS_DE_SANTE_VIDEO/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HEALTH_BODY_CARE/lesson/FR_FR_C1_VOCABULARY_OFFRIR_DES_SOINS_DE_SANTE_TRANSFRONTALIERS/activity/FR_FR_C1_VOCABULARY_OFFRIR_DES_SOINS_DE_SANTE_TRANSFRONTALIERS_VIDEO/video",
    # Relations
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_MINUS_VOCABULARY_DECRIRE_LES_MEMBRES_DE_LA_FAMILLE/activity/FR_FR_A1_MINUS_VOCABULARY_DECRIRE_LES_MEMBRES_DE_LA_FAMILLE_VIDEO_ANIMATION_LECON_4_MA_FAMILLE/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_MINUS_VOCABULARY_LES_MEMBRES_DE_LA_FAMILLE/activity/FR_FR_A1_MINUS_VOCABULARY_LES_MEMBRES_DE_LA_FAMILLE_VIDEO_ANIMATION_LECON_3_LES_MEMBRES_DE_LA_FAMILL/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_MINUS_VOCABULARY_PRESENTER_QUELQU_UN/activity/FR_FR_A1_MINUS_VOCABULARY_PRESENTER_QUELQU_UN_VIDEO_ANIMATION_LECON_4_PRESENTATIONS_2EME_PARTIE/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_MINUS_VOCABULARY_RENCONTRER_QUELQU_UN/activity/FR_FR_A1_MINUS_VOCABULARY_RENCONTRER_QUELQU_UN_VIDEO_ANIMATION_LECON_2_RENCONTRER_DES_PERSONNES/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_VOCABULARY_DECRIRE_LE_CARACTERE_DE_QUELQU_UN/activity/FR_FR_A1_VOCABULARY_DECRIRE_LE_CARACTERE_DE_QUELQU_UN_VIDEO_ANIMATION_CEDRIC_DECRIT_LE_CARACTERE_DE_/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_VOCABULARY_DECRIRE_L_APPARENCE_DE_QUELQU_UN/activity/FR_FR_A1_VOCABULARY_DECRIRE_L_APPARENCE_DE_QUELQU_UN_VIDEO_ANIMATION_CEDRIC_DECRIT_MOIRA_PHYSIQUEMEN/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_VOCABULARY_PARLER_DE_SA_FAMILLE/activity/FR_FR_A1_VOCABULARY_PARLER_DE_SA_FAMILLE_VIDEO_ANIMATION_CEDRIC_ET_SA_VOISINE_PARLENT_DE_LEUR_FAMILL/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A1_VOCABULARY_RENCONTRER_QUELQU_UN_DE_NOUVEAU_UN_E_INCONNU_E/activity/FR_FR_A1_VOCABULARY_RENCONTRER_QUELQU_UN_DE_NOUVEAU_UN_E_INCONNU_E_VIDEO_ANIMATION_CEDRIC_RENCONTRE_/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/RELATIONS_WITH_OTHER_PEOPLE/lesson/FR_FR_A2_VOCABULARY_PARLER_DE_SA_FAMILLE_PARTIE_1/activity/FR_FR_A2_VOCABULARY_PARLER_DE_SA_FAMILLE_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    # Shopping.
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/SHOPPING_RETAIL/lesson/FR_FR_A1_VOCABULARY_ACHETER_DES_VETEMENTS/activity/FR_FR_A1_VOCABULARY_ACHETER_DES_VETEMENTS_VIDEO_ANIMATION_CEDRIC_ET_MOIRA_A_LA_BOUTIQUE_DE_VETEMENTS/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/SHOPPING_RETAIL/lesson/FR_FR_A1_VOCABULARY_PARLER_A_UN_ASSISTANT_COMMERCIAL/activity/FR_FR_A1_VOCABULARY_PARLER_A_UN_ASSISTANT_COMMERCIAL_VIDEO_ANIMATION_CEDRIC_ACHETE_DES_CHAUSSURES/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/SHOPPING_RETAIL/lesson/FR_FR_A2_VOCABULARY_FAIRE_DU_SHOPPING_PARTIE_1/activity/FR_FR_A2_VOCABULARY_FAIRE_DU_SHOPPING_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/SHOPPING_RETAIL/lesson/FR_FR_B1_VOCABULARY_TRAVAILLER_DANS_UN_MAGASIN/activity/FR_FR_B1_VOCABULARY_TRAVAILLER_DANS_UN_MAGASIN_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/SHOPPING_RETAIL/lesson/FR_FR_B1_VOCABULARY_TRAVAILLER_DANS_UN_MAGASIN/activity/FR_FR_B1_VOCABULARY_TRAVAILLER_DANS_UN_MAGASIN_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/SHOPPING_RETAIL/lesson/FR_FR_B1_VOCABULARY_A_LA_BOUTIQUE_DE_VETEMENTS/activity/FR_FR_B1_VOCABULARY_A_LA_BOUTIQUE_DE_VETEMENTS_VIDEO_PARTIE_1_ANIMATION/video",
    # Homes
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_A1_VOCABULARY_ACHETER_DES_MEUBLES_POUR_VOTRE_DOMICILE/activity/FR_FR_A1_VOCABULARY_ACHETER_DES_MEUBLES_POUR_VOTRE_DOMICILE_VIDEO_ANIMATION_CEDRIC_ET_SON_FRERE_AU_G/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_A1_VOCABULARY_FAIRE_VISITER_VOTRE_DOMICILE/activity/FR_FR_A1_VOCABULARY_FAIRE_VISITER_VOTRE_DOMICILE_VIDEO_ANIMATION_CEDRIC_FAIT_VISITER_SON_APPARTEMENT/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_A2_VOCABULARY_CHERCHER_UN_APPARTEMENT_PARTIE_1/activity/FR_FR_A2_VOCABULARY_CHERCHER_UN_APPARTEMENT_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_A2_VOCABULARY_DECRIRE_UNE_MAISON_PARTIE_1/activity/FR_FR_A2_VOCABULARY_DECRIRE_UNE_MAISON_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_B1_VOCABULARY_ACHETER_UNE_MAISON_AVEC_UNE_AGENCE_IMMOBILIERE/activity/FR_FR_B1_VOCABULARY_ACHETER_UNE_MAISON_AVEC_UNE_AGENCE_IMMOBILIERE_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_B1_VOCABULARY_CHERCHER_UN_APPARTEMENT_A_LOUER/activity/FR_FR_B1_VOCABULARY_CHERCHER_UN_APPARTEMENT_A_LOUER_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_B1_VOCABULARY_VISITER_UN_APPARTEMENT_A_LOUER/activity/FR_FR_B1_VOCABULARY_VISITER_UN_APPARTEMENT_A_LOUER_VIDEO_PARTIE_1_ANIMATION/video",
    # Free Time.
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A1_MINUS_VOCABULARY_PARLER_DES_LOISIRS_CE_QUE_J_AIME_ET_N_AIME_PAS/activity/FR_FR_A1_MINUS_VOCABULARY_PARLER_DES_LOISIRS_CE_QUE_J_AIME_ET_N_AIME_PAS_VIDEO_ANIMATION_LECON_4_LES/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A1_VOCABULARY_DECRIRE_VOTRE_DERNIERE_SORTIE_DU_WEEKEND/activity/FR_FR_A1_VOCABULARY_DECRIRE_VOTRE_DERNIERE_SORTIE_DU_WEEKEND_VIDEO_ANIMATION_CEDRIC_RENTRE_D_UN_WEEK/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A1_VOCABULARY_PARLER_DE_SES_PROJETS_POUR_LA_JOURNEE/activity/FR_FR_A1_VOCABULARY_PARLER_DE_SES_PROJETS_POUR_LA_JOURNEE_VIDEO_ANIMATION_CEDRIC_ORGANISE_UNE_JOURNE/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A1_VOCABULARY_PARLER_DE_SON_WEEK_END/activity/FR_FR_A1_VOCABULARY_PARLER_DE_SON_WEEK_END_VIDEO_ANIMATION_CEDRIC_PARLE_DE_SES_LOISIRS_AVEC_AURELIE/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A1_VOCABULARY_PARLER_DES_LOISIRS/activity/FR_FR_A1_VOCABULARY_PARLER_DES_LOISIRS_VIDEO_ANIMATION_CEDRIC_DISCUTE_SPORTS_ET_HOBBIES_AVEC_DES_COL/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A1_VOCABULARY_PARLER_D_HIER_SOIR/activity/FR_FR_A1_VOCABULARY_PARLER_D_HIER_SOIR_VIDEO_ANIMATION_UNE_SOIREE_CINEMA/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A2_VOCABULARY_FAIRE_DU_SPORT_PARTIE_1/activity/FR_FR_A2_VOCABULARY_FAIRE_DU_SPORT_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/FREE_TIME_ENTERTAINMENT/lesson/FR_FR_A2_VOCABULARY_FAIRE_DU_SPORT_PARTIE_1/activity/FR_FR_A2_VOCABULARY_FAIRE_DU_SPORT_PARTIE_1_VIDEO_PARTIE_1_ANIMATION/video",
    # Food And Drinks.
]

SCREEN_SIZE = p.size()


def getRandomVideo():
    return random.choice(VIDEOS)


def main():
    # Script Start.
    print(
        "Make sure you have PYAUTOGUI installed, and running this script as recommended. \n"
    )
    print(
        "Make sure you are already logged in with your account, this script does not handle authentication for security reasons. \n"
    )
    print(
        "You may want to mute the video before running the script if you haven't already \n"
    )
    input(
        "Press Enter to start executing, from now on don't touch your mouse and keyboard. \n"
    )

    for i in range(3, 0, -1):
        time.sleep(1)
        print(f"Script starts in: {i}")
    print(" \n")

    # Open Firefox.
    print("Opening Firefox.")
    p.hotkey("win")
    time.sleep(5)
    p.typewrite(("firefox"))
    time.sleep(5)
    p.press("enter")

    time.sleep(15)

    # FullScreen.
    p.press("f11")

    # Open Video URL.
    print("Opening Video URL.")
    p.hotkey("ctrl", "t")
    p.typewrite(getRandomVideo())
    p.press("enter")

    time.sleep(15)

    # Play the Video.
    print("Playing the Video.")
    p.moveTo(math.floor(math.floor(SCREEN_SIZE[0] / 2)), math.floor(SCREEN_SIZE[1] / 3))
    p.click()

    iter = 0
    # 10 mins.
    resetCounter = 30
    while True:

        timePassed = format((iter * 10) / 60, ".2f")
        resetCounter -= 1

        time.sleep(10)
        p.press("left")

        print(f"Iteration number: {iter}; Time: {timePassed}mins.")
        iter += 1

        if resetCounter <= 0:
            resetCounter = 30

            print("Switching to another video")

            # Open another video URL.
            p.hotkey("ctrl", "l")
            time.sleep(3)
            p.typewrite(getRandomVideo())
            time.sleep(3)
            p.press("enter")
            time.sleep(3)
            p.hotkey("ctrl", "r")

            time.sleep(5)

            # Play the Video.
            print("Playing the Video.")
            p.moveTo(
                math.floor(math.floor(SCREEN_SIZE[0] / 2)),
                math.floor(SCREEN_SIZE[1] / 3),
            )

            p.click()


if __name__ == "__main__":
    main()
