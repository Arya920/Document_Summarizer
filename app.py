# This Coding is affiliated to GeekaThon 1.0
#---------------------------------------------------IMPORTING LIBRARIES----------------------------------------------------------------------------------------------->
import streamlit as st
from PIL import Image,ImageDraw
import logging
from Functions import text_extractor, sum_pegasus, FB_BERT_LARGE_CNN, translate, text_to_speech, extract_keywords_with_keybert,fine_tuned_bart

#<----------------------------------------------------MAIN HEADER------------------------------------------------------------------------------------------------------->

st.markdown("<h1 style='text-align: center; color: #4B0082; font-family: cursive; font-size: 63px; margin-top: 0px; margin-bottom: 0px;'>InfiniSynth</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: green; font-family: cursive; font-size: 18px; margin-top: -15px;'>Endless Insights, Minimal Text</h1>", unsafe_allow_html=True)

#<-----------------------------------------------------SIDEBAR--------------------------------------------------------------------------------------------------------->
image = Image.open('logo.png')
mask = Image.new('L', image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, image.width, image.height), fill=255)
circular_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
circular_image.paste(image, mask=mask)
st.sidebar.image(circular_image, use_column_width=True)
st.sidebar.divider()

st.sidebar.write("**:black[Problem Statement]**")
st.sidebar.markdown('''**:green[Long articles and research papers contain a wealth of information, posing a challenge for readers to efficiently grasp essential details.
                    The objective is to develop an Automatic Document Summarization Model (ADSM) using NLP techniques. This model will employ advanced methods 
                    to generate succinct and meaningful summaries of lengthy textual documents.]**''')

st.sidebar.divider()
st.sidebar.markdown("## Project Members")
members = {
    "Ketan Kumar": "https://github.com/Ketan3102",
    "Arya Chakraborty": "https://github.com/Arya920",
    "Shritama Sengupta": "https://github.com/codeforever200",
    "Janvi Kumari": "https://github.com/JanviKumari01",
    "Shivam Sengupta": "https://github.com/shivamsengupta",
}

for member, github_link in members.items():
    st.sidebar.write(f"[{member}]({github_link})")

#<----------------------------------------------------Defining the Columns ------------------------------------------------------------------------------------->

col1, col2 = st.columns(2)

#<-----------------------------------------------------INPUT COLUMN-------------------------------------------------------------------------------------------------->

with col1:
    st.markdown("<div style='text-align: center; color: #4B0082; font-size: 18px;'><h2>Input Section</h2></div>", unsafe_allow_html=True)

    option_chosen = st.selectbox('**:green[How you want to give input ?]**',('Upload a PDF/Word Doc','Copy & Paste')) # Only 2 inputs 
    
    if option_chosen == "Copy & Paste":
        main_text = st.text_input("**:green[Copy your text here]**")

    elif option_chosen == "Upload a PDF/Word Doc":
        uploaded_files = st.file_uploader("Upload your File")
        if uploaded_files is None:
            st.warning("Upload The File Before Summarizing")
        else:
            st.success('Uploaded')


    token_length = st.slider('**:green[Select the Length of the Summary]**', min_value=50, max_value=500, value=100, step=1)
    col4, col5 = st.columns(2)
      
    with col4:
        chosen_model = st.selectbox('**:green[Model LIst]**',('PEGASUS','BART','Our Fine Tuned BART'))  
    with col5:
                language_mapping = {'English':	'eng_Latn',
                                    'Acehnese (Arabic script)':	'ace_Arab',
                                    'Acehnese (Latin script)':	'ace_Latn',
                                    'Mesopotamian Arabic':	'acm_Arab',
                                    'Taizzi-Adeni Arabic':	'acq_Arab',
                                    'Tunisian Arabic':	'aeb_Arab',
                                    'Afrikaans':	'afr_Latn',
                                    'South Levantine Arabic':	'ajp_Arab',
                                    'Akan':	'aka_Latn',
                                    'Amharic'	:'amh_Ethi',
                                    'North Levantine Arabic':	'apc_Arab',
                                    'Modern Standard Arabic':	'arb_Arab',
                                    'Modern Standard Arabic (Romanized)':	'arb_Latn',
                                    'Najdi Arabic':	'ars_Arab',
                                    'Moroccan Arabic':	'ary_Arab',
                                    'Egyptian Arabic'	:'arz_Arab',
                                    'Assamese':	'asm_Beng',
                                    'Asturian' :	'ast_Latn',
                                    'Awadhi':	'awa_Deva',
                                    'Central Aymara':	'ayr_Latn',
                                    'South Azerbaijani':	'azb_Arab',
                                    'North Azerbaijani':	'azj_Latn',
                                    'Bashkir':	'bak_Cyrl',
                                    'Bambara':	'bam_Latn',
                                    'Balinese':	'ban_Latn',
                                    'Belarusian':	'bel_Cyrl',
                                    'Bemba':	'bem_Latn',
                                    'Bengali':	'ben_Beng',
                                    'Bhojpuri':	'bho_Deva',
                                    'Banjar (Arabic script)':	'bjn_Arab',
                                    'Banjar (Latin script)':	'bjn_Latn',
                                    'Standard Tibetan':	'bod_Tibt',
                                    'Bosnian':	'bos_Latn',
                                    'Buginese':	'bug_Latn',
                                    'Bulgarian':	'bul_Cyrl',
                                    'Catalan':	'cat_Latn',
                                    'Cebuano':	'ceb_Latn',
                                    'Czech':	'ces_Latn',
                                    'Chokwe':	'cjk_Latn',
                                    'Central Kurdish':	'ckb_Arab',
                                    'Crimean Tatar':	'crh_Latn',
                                    'Welsh':	'cym_Latn',
                                    'Danish':	'dan_Latn',
                                    'German':	'deu_Latn',
                                    'Southwestern Dinka':	'dik_Latn',
                                    'Dyula':	'dyu_Latn',
                                    'Dzongkha'	:'dzo_Tibt',
                                    'Greek':	'ell_Grek',
                                    'Esperanto':	'epo_Latn',
                                    'Estonian':	'est_Latn',
                                    'Basque':	'eus_Latn',
                                    'Ewe':	'ewe_Latn',
                                    'Faroese':	'fao_Latn',
                                    'Fijian':	'fij_Latn',
                                    'Finnish':	'fin_Latn',
                                    'Fon':	'fon_Latn',
                                    'French':	'fra_Latn',
                                    'Friulian':	'fur_Latn',
                                    'Nigerian Fulfulde':	'fuv_Latn',
                                    'Scottish Gaelic':	'gla_Latn',
                                    'Irish':	'gle_Latn',
                                    'Galician':	'glg_Latn',
                                    'Guarani':	'grn_Latn',
                                    'Gujarati':	'guj_Gujr',
                                    'Haitian Creole':	'hat_Latn',
                                    'Hausa':	'hau_Latn',
                                    'Hebrew':	'heb_Hebr',
                                    'Hindi':	'hin_Deva',
                                    'Chhattisgarhi':	'hne_Deva',
                                    'Croatian':	'hrv_Latn',
                                    'Hungarian':	'hun_Latn',
                                    'Armenian':	'hye_Armn',
                                    'Igbo':	'ibo_Latn',
                                    'Ilocano':	'ilo_Latn',
                                    'Indonesian':	'ind_Latn',
                                    'Icelandic':	'isl_Latn',
                                    'Italian':	'ita_Latn',
                                    'Javanese':	'jav_Latn',
                                    'Japanese':	'jpn_Jpan',
                                    'Kabyle':	'kab_Latn',
                                    'Jingpho':	'kac_Latn',
                                    'Kamba':	'kam_Latn',
                                    'Kannada':	'kan_Knda',
                                    'Kashmiri (Arabic script)':	'kas_Arab',
                                    'Kashmiri (Devanagari script)':	'kas_Deva',
                                    'Georgian':	'kat_Geor',
                                    'Central Kanuri (Arabic script)':	'knc_Arab',
                                    'Central Kanuri (Latin script)':	'knc_Latn',
                                    'Kazakh':	'kaz_Cyrl',
                                    'Kabiyè	': 'kbp_Latn',
                                    'Kabuverdianu':	'kea_Latn',
                                    'Khmer':	'khm_Khmr',
                                    'Kikuyu':	'kik_Latn',
                                    'Kinyarwanda':	'kin_Latn',
                                    'Kyrgyz':	'kir_Cyrl',
                                    'Kimbundu':	'kmb_Latn',
                                    'Northern Kurdish':	'kmr_Latn',
                                    'Kikongo':	'kon_Latn',
                                    'Korean':	'kor_Hang',
                                    'Lao':	'lao_Laoo',
                                    'Ligurian':	'lij_Latn',
                                    'Limburgish':	'lim_Latn',
                                    'Lingala':	'lin_Latn',
                                    'Lithuanian':	'lit_Latn',
                                    'Lombard':	'lmo_Latn',
                                    'Latgalian':	'ltg_Latn',
                                    'Luxembourgish':	'ltz_Latn',
                                    'Luba-Kasai':	'lua_Latn',
                                    'Ganda':	'lug_Latn',
                                    'Luo':	'luo_Latn',
                                    'Mizo':	'lus_Latn',
                                    'Standard Latvian':	'lvs_Latn',
                                    'Magahi':	'mag_Deva',
                                    'Maithili':	'mai_Deva',
                                    'Malayalam':	'mal_Mlym',
                                    'Marathi':	'mar_Deva',
                                    'Minangkabau (Arabic script)':	'min_Arab',
                                    'Minangkabau (Latin script)':	'min_Latn',
                                    'Macedonian':	'mkd_Cyrl',
                                    'Plateau Malagasy':	'plt_Latn',
                                    'Maltese':	'mlt_Latn',
                                    'Meitei (Bengali script)':	'mni_Beng',
                                    'Halh Mongolian	':'khk_Cyrl',
                                    'Mossi':	'mos_Latn',
                                    'Maori':	'mri_Latn',
                                    'Burmese':	'mya_Mymr',
                                    'Dutch':	'nld_Latn',
                                    'Norwegian Nynorsk':	'nno_Latn',
                                    'Norwegian Bokmål':	'nob_Latn',
                                    'Nepali':	'npi_Deva',
                                    'Northern Sotho':	'nso_Latn',
                                    'Nuer':	'nus_Latn',
                                    'Nyanja':	'nya_Latn',
                                    'Occitan':	'oci_Latn',
                                    'West Central Oromo':	'gaz_Latn',
                                    'Odia':	'ory_Orya',
                                    'Pangasinan':	'pag_Latn',
                                    'Eastern Panjabi':	'pan_Guru',
                                    'Papiamento':	'pap_Latn',
                                    'Western Persian':	'pes_Arab',
                                    'Polish	':'pol_Latn',
                                    'Portuguese':	'por_Latn',
                                    'Dari':	'prs_Arab',
                                    'Southern Pashto':	'pbt_Arab',
                                    'Ayacucho Quechua':	'quy_Latn',
                                    'Romanian':	'ron_Latn',
                                    'Rundi':	'run_Latn',
                                    'Russian':	'rus_Cyrl',
                                    'Sango':	'sag_Latn',
                                    'Sanskrit':	'san_Deva',
                                    'Santali':	'sat_Olck',
                                    "Sicilian":	'scn_Latn',
                                    'Shan':	'shn_Mymr',
                                    'Sinhala':	'sin_Sinh',
                                    'Slovak'	:'slk_Latn',
                                    'Slovenian':	'slv_Latn',
                                    'Samoan'	:'smo_Latn',
                                    'Shona':	'sna_Latn',
                                    'Sindhi'	:'snd_Arab',
                                    'Somali'	:'som_Latn',
                                    'Southern Sotho'	:'sot_Latn',
                                    'Spanish'	: 'spa_Latn',
                                    'Tosk Albanian'	:'als_Latn',
                                    'Sardinian'	:'srd_Latn',
                                    'Tamil' : 'tam_Taml',
                                    'Telugu' : 'tel_Telu',
                                    'Kannada' : 'kan_Knda'}
                language = st.selectbox('**:green[Choose Language]**',list(language_mapping.keys()) )

# <-----------------------------------------------------GENERATE SUMMARY------------------------------------------------------------------------------------------->

summary =  st.button('**:green[Generate Summary]**')
def tok_word(csv_text):

  # Tokenize using split with a comma as the delimiter
  tokens = csv_text.split(' ')
  length = len(tokens )
  return length
#<-------------------------------------------------------OUTPUT COLUMN------------------------------------------------------------------------------------------------>
with col2:
    st.markdown("<div style='text-align: center; color: #4B0082;'><h2>Output Section</h2></div>", unsafe_allow_html=True)


    #----------------------------------------------------OPTION 1 = Copy & Paste---------------------------------------------------------    
    if option_chosen == 'Copy & Paste':
        if summary:
            #-------------------------------------------------------------------Fine Tuned BART MODEL-----------------------------------------------
            if chosen_model== 'Our Fine Tuned BART':
                summarized_text = fine_tuned_bart(main_text,token_length)
                l = tok_word(summarized_text)
                if language == "English":
                    st.text_area('**:green[Summarized Text]**', summarized_text)

                    st.write(f'Keywords : ')
                    st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                    st.write(f'Summarization Length: {l} words.')

                    text_to_speech(summarized_text,language)
                    audio_file = open('saved_audio.wav', 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/ogg')

                else:
                    translated_text = translate(summarized_text,language,l)
                    st.text_area('**:green[Summarized Text]**', translated_text)
                    
                    st.write(f'Keywords : ')
                    st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                    st.write(f'Summarization Length: {l} words.')

                    text_to_speech(translated_text,language)
                    audio_file = open('saved_audio.wav', 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/ogg')

            #-------------------------------------------------------------------BART MODEL-----------------------------------------------
            if chosen_model== 'BART':
                summarized_text = FB_BERT_LARGE_CNN(main_text,token_length)
                l = tok_word(summarized_text)
                if language == "English":
                    st.text_area('**:green[Summarized Text]**', summarized_text)

                    st.write(f'Keywords : ')
                    st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                    st.write(f'Summarization Length: {l} words.')

                    text_to_speech(summarized_text,language)
                    audio_file = open('saved_audio.wav', 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/ogg')

                else:
                    translated_text = translate(summarized_text,language,l)
                    st.text_area('**:green[Summarized Text]**', translated_text)
                    
                    st.write(f'Keywords : ')
                    st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                    st.write(f'Summarization Length: {l}  words.')

                    text_to_speech(translated_text,language)
                    audio_file = open('saved_audio.wav', 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/ogg')
            
            # --------------------------------------------------------------------PEGASUS MODEL------------------------------------------
            elif chosen_model == 'PEGASUS':
                summarized_text = sum_pegasus(main_text,token_length)
                l = tok_word(summarized_text)
                if language == "English":
                    st.text_area('**:green[Summarized Text]**', summarized_text)

                    st.write(f'Keywords : ')
                    st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                    st.write(f'Summarization Length: {l} words.')

                    text_to_speech(summarized_text,language)
                    audio_file = open('saved_audio.wav', 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/ogg')

                    

                else:
                    translated_text = translate(summarized_text,language,l)
                    st.text_area('**:green[Summarized Text]**', translated_text)
                    
                    st.write(f'Keywords : ')
                    st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                    st.write(f'Summarization Length: {l} words.')

                    text_to_speech(translated_text,language)
                    audio_file = open('saved_audio.wav', 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/ogg')



    #----------------------------------------------------------------------------OPTION 2 = PDF/DOC File-----------------------------------
    elif option_chosen == 'Upload a PDF/Word Doc':
        if uploaded_files is not None:
            output = text_extractor(uploaded_files)

            if summary:
                #-----------------------------------------------------------------------Fine Tuned BART MODEL----------------------------------------
                if chosen_model== 'Our Fine Tuned BART':
                    summarized_text = fine_tuned_bart(output,token_length)
                    l = tok_word(summarized_text)
                    if language == 'English':
                        st.text_area('**:green[Summarized Text]**', summarized_text)

                        st.write(f'Keywords : ')
                        st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                        st.write(f'Summarization Length: {l} Words.')

                        text_to_speech(summarized_text,language)
                        audio_file = open('saved_audio.wav', 'rb')
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format='audio/ogg')

                    else:
                        translated_text = translate(summarized_text,language,l)
                        st.text_area('**:green[Summarized Text]**', translated_text)

                        st.write(f'Keywords : ')
                        st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')


                        st.write(f'Summarization Length: {l} words.')

                        text_to_speech(translated_text,language)
                        audio_file = open('saved_audio.wav', 'rb')
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format='audio/ogg')
                #-----------------------------------------------------------------------BART MODEL----------------------------------------
                if chosen_model== 'BART':
                    summarized_text = FB_BERT_LARGE_CNN(output,token_length)
                    l = tok_word(summarized_text)
                    if language == 'English':
                        st.text_area('**:green[Summarized Text]**', summarized_text)

                        st.write(f'Keywords : ')
                        st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')


                        st.write(f'Summarization Length: {l} Words.')

                        text_to_speech(summarized_text,language)
                        audio_file = open('saved_audio.wav', 'rb')
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format='audio/ogg')

                    else:
                        translated_text = translate(summarized_text,language,l)
                        st.text_area('**:green[Summarized Text]**', translated_text)

                        st.write(f'Keywords : ')
                        st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')


                        st.write(f'Summarization Length: {l} words.')

                        text_to_speech(translated_text,language)
                        audio_file = open('saved_audio.wav', 'rb')
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format='audio/ogg')

                
                #-----------------------------------------------------------------------PEGASUS MODEL--------------------------------------
                elif chosen_model == 'PEGASUS':
                    summarized_text = sum_pegasus(output,token_length)
                    l = tok_word(summarized_text)
                    if language == 'English':
                        st.text_area('**:green[Summarized Text]**', summarized_text)

                        st.write(f'Keywords : ')
                        st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                        st.write(f'Summarization Length: {l} Words.')

                        text_to_speech(summarized_text,language)
                        audio_file = open('saved_audio.wav', 'rb')
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format='audio/ogg')
                    else:
                        translated_text = translate(summarized_text,language,l)
                        st.text_area('**:green[Summarized Text]**', translated_text)

                        st.write(f'Keywords : ')
                        st.markdown(f'**:green[{extract_keywords_with_keybert(summarized_text,top_n=5, diversity=0.5)}]**')

                        st.write(f'Summarization Length: {l} words.')

                        text_to_speech(translated_text,language)
                        audio_file = open('saved_audio.wav', 'rb')
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format='audio/ogg')


    



