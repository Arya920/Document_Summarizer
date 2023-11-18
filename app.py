# This Coding is affiliated to GeekaThon 1.0
#---------------------------------------------------IMPORTING LIBRARIES----------------------------------------------------------------------------------------------->
import streamlit as st
import logging
from Functions import text_extractor, sum_pegasus

#<----------------------------------------------------MAIN HEADER------------------------------------------------------------------------------------------------------->

st.markdown("<h1 style='text-align: center; color: #4B0082; font-family: cursive;'>Document Summarizer 📄📃</h1>", unsafe_allow_html=True)

#<----------------------------------------------------Defining the Columns ------------------------------------------------------------------------------------->

col1, col2 = st.columns(2)

#<-----------------------------------------------------INPUT COLUMN-------------------------------------------------------------------------------------------------->

with col1:
    st.subheader("Input Section")
    option_chosen = st.selectbox('**:green[How you want to give input ?]**',('Upload a PDF/Word Doc','Copy & Paste')) # Only 2 inputs 
    
    if option_chosen == "Copy & Paste":
        main_text = st.text_input("**:green[Copy your text here]**")

    elif option_chosen == "Upload a PDF/Word Doc":
        uploaded_files = st.file_uploader("Upload your File")



    int_val = st.slider('**:green[Select the Length of the Summary]**', min_value=50, max_value=150, value=70, step=1)
    col4, col5 = st.columns(2)
      
    with col4:
        chosen_model = st.selectbox('**:green[Model LIst]**',('Paguses','BERT'))  
    with col5:
        language = st.selectbox('**:green[Choose Language]**',( 'English','Achinese', 'Mesopotamian Arabic',"Ta'izzi-Adeni Arabic", 'Tunisian Arabic', 'Afrikaans', 'ajp', 'Akan', 'Tosk Albanian', 'Amharic', 'Levantine Arabic', 'Arabic', 'Najdi Arabic', 'Moroccan Arabic', 
                                                               'Egyptian Arabic', 'Assamese', 'Asturian', 'Awadhi', 'Central Aymara', 'South Azerbaijani', 'North Azerbaijani', 'Bashkir', 'Bambara', 'Balinese', 'Belarusian', 'Bemba (Zambia)',
                                                                'Bengali', 'Bhojpuri', 'Banjar', 'Tibetan', 'Bosnian', 'Buginese', 'Bulgarian', 'Catalan', 'Cebuano', 'Czech', 'Chokwe', 'Central Kurdish', 'Crimean Tatar', 'Welsh', 'Danish', 'German', 'Southwestern Dinka', 'Dyula', 'Dzongkha', 'Greek', 'Esperanto', 'Estonian', 'Basque', 'Ewe', 'Faroese', 'Fijian', 'Finnish', 'Fon', 'French', 'Friulian', 'Nigerian Fulfulde', 'West Central Oromo', 'Scottish Gaelic', 'Irish', 'Galician', 'Guaraní', 'Gujarati', 'Haitian', 'Hausa', 'Hebrew', 'Hindi', 'Chhattisgarhi', 'Croatian', 'Hungarian', 'Armenian', 'Igbo', 'Iloko', 'Indonesian', 'Icelandic', 'Italian', 'Javanese', 'Japanese', 'Kabyle', 'Kachin', 'Kamba (Kenya)', 'Kannada', 'Kashmiri', 'Georgian', 'Kazakh', 'Kabiyè', 'Kabuverdianu', 'Halh Mongolian', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kyrgyz', 'Kimbundu', 'Northern Kurdish', 'Central Kanuri', 'Kongo', 'Korean', 'Lao',
                                                                'Ligurian', 'Limburgish', 'Lingala', 'Lithuanian', 'Lombard', 'Latgalian', 'Luxembourgish', 'Luba-Lulua', 'Ganda', 'Luo (Kenya and Tanzania)', 'Lushai', 'Standard Latvian', 'Magahi', 'Maithili', 'Malayalam', 'Marathi', 'Minangkabau', 'Macedonian',
                                                                'Maltese', 'Manipuri', 'Mossi', 'Māori', 'Burmese', 'Dutch', 'Norwegian Nynorsk', 'Norwegian Bokmål', 'Nepali (indiviual language)', 'Pedi',
                                                                'Nuer', 'Chichewa', 'Occitan', 'Odia', 'Pangasinan', 'Panjabi', 'Papiamento', 'Southern Pashto', 'Iranian Persian', 'Plateau Malagasy', 'Polish', 'Portuguese',
                                                                'Dari', 'Ayacucho Quechua', 'Romanian', 'Kirundi', 'Russian', 'Sango', 'Sanskrit', 'Santali', 'Sicilian',
                                                                'Shan', 'Sinhala', 'Slovak', 'Slovenian','Samoan', 'Shona', 'Sindhi', 'Somali', 'Southern Sotho', 'Spanish', 'Sardinian',
                                                                'Serbian', 'Swati', 'Sundanese', 'Swedish', 'Swahili (individual language)', 'Silesian', 'Tamil', 'Tamasheq', 'Tatar', 'Telugu', 'Tajik', 'Tagalog', 'Thai', 'Tigrinya',
                                                                'Tok Pisin', 'Tswana', 'Tsonga', 'Turkmen', 'Tumbuka', 'Turkish', 'Twi', 'Central Atlas Tamazight', 'Uyghur', 'Ukrainian', 'Umbundu', 'Urdu', 'Northern Uzbek',
                                                                'Venetian', 'Vietnamese', 'Waray (Philippines)', 'Wolof', 'Xhosa', 'Eastern Yiddish', 'Yoruba', 'Yue Chinese', 'Chinese', 'Standard Malay'
                                                                ))
# <-----------------------------------------------------GENERATE SUMMARY------------------------------------------------------------------------------------------->

summary =  st.button('**:green[Generate Summary]**')
if uploaded_files is None:
    st.warning("Upload The File Before Summarizing")
else:
    st.success('Uploaded')


#<-------------------------------------------------------OUTPUT COLUMN------------------------------------------------------------------------------------------------>
with col2:
    st.subheader("Output Section")    
    if option_chosen == 'Copy & Paste':
        if summary:
            #summarized_text = sum_pegasus(main_text)
            st.text_area('**:green[Summarized Text]**', main_text)
            st.write(f'Summarization Length: {len(main_text)} characters.')

    elif option_chosen == 'Upload a PDF/Word Doc':
        if uploaded_files is not None:
            output = text_extractor(uploaded_files)

            if summary:
                #summarized_text = sum_pegasus(output)
                st.text_area('**:green[Summarized Text]**',output )
                st.write(f'Summarization Length: {len(output)} characters.')

    



