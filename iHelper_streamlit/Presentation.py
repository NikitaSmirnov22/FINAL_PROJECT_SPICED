def app():
    import streamlit as st
    html = '<div class="header"><h1>iHelper ❤️‍🩹</h1></div>'
    st.title("PROJECT WORKFLOW 👨🏻‍💻")
    
    tab1, tab2, tab3, tab4, tab6 = st.tabs(["DEMO","DATA PREPARATION","FINE-TUNING","MODEL","WHAT`S NEXT?"])

    with tab1:
        import streamlit as st
        st.info("""My project workflow is consist of **four stages :**
        \n 1. **Data preprocessing** - creating a dataset from scratch(regex, web-scraping) based on the Red Cross data source 
        \n 2. **Fine-tuning** - playing with hyper parameters and injecting the raw data to the model
        \n 3. **Model application** - using the GPT-3 engine (davinci model) as a base line model
        \n 4. **Deployment on Streamlit**""")
        
        st.image("101.png", caption="App architecture")

    with tab2:
        st.info("Converting **training data** to **json** format ⚙️")

        code = '''
        {"prompt": "<prompt text>", "completion": "<ideal generated text>"}\n{"prompt": "<prompt text>", "completion": "<ideal generated text>"}\n{"prompt": "<prompt text>", "completion": "<ideal generated text>"}\n...'''
        st.code(code, language='json')
        st.success("**Final output** 🎉")
        code = '''{"prompt": "Care for Life-Threatening External Bleeding", "completion": "1. Expose the wound. 2. Apply firm and direct pressure to the wound. 3. While maintaining direct pressure, apply a dressing and bandage, and then secure them in place. 4. Reassess the wound to see if the pressure has stopped the bleeding. If not, consider using a tourniquet if the wound is on a limb."}\n{"prompt": "Using Hemostatic Dressings", "completion": "A hemostatic dressing is a dressing treated with a substance that speeds clot formation. As is the case with tourniquets, hemostatic dressings are used in cases of life-threatening bleeding where standard first aid procedures fail or are not practical. Typically, hemostatic dressings are used on parts of the body where a tourniquet cannot be applied, such as the neck or torso. A hemostatic dressing can also be used to control bleeding from an open wound on an arm or a leg if a tourniquet is ineffective. The hemostatic dressing is applied at the site of the bleeding (possibly inside the wound) and is used along with direct pressure."}\n{"prompt": "Mouth-to-Stoma Breathing", "completion": "Some people have had an operation to remove part of the trachea. They breathe through an opening called a stoma in the front of the neck. Because air passes directly into the trachea through the stoma instead of through the mouth and nose, you should give rescue breaths into the stoma. Block the person’s mouth and nose with your hand to stop air from escaping."}\n{"prompt": "What to do in case of Hyperventilation?", "completion": "1. Encourage the person to take controlled breaths by breathing in slowly, holding his or her breath for a few seconds, and then gradually exhaling. Myth: If a person is hyperventilating, you should have him or her breathe into a paper bag. This practice is unsafe and not recommended as a way to care for a hyperventilating person. The best way to treat hyperventilation is to encourage the person to take slow, controlled breaths."}\n'''
        st.code(code, language='json')
        
        with open('final_raw_data.csv') as f:
            st.download_button(' PRESS ❤️‍🩹 TO DOWNLOAD TRAINING DATA', f)
    

    with tab3:
        st.info("""💡 Fine-tuning improves on few-shot learning by training on many more examples than can fit in the prompt, letting you achieve better results on a wide number of tasks. Once a model has been fine-tuned, you won't need to provide examples in the prompt anymore. This saves costs and enables lower-latency requests. 
        \n**Hyperparameters used for tuning the model:**\n- **model:** The name of the base model to fine-tune. You can select one of "ada", "babbage", "curie", or "davinci". 
        \n- **n_epochs** -  corresponds to number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.  Applied number of epochs is 4. 
        \n- **batch_size** - The batch size is the number of training examples used to train a single forward and backward pass. A picked number of batch size is ~0.2% of the number of examples in the training set. 
        \n- **compute_classification_metrics** - defaults to False. If True, for fine-tuning for classification tasks, computes classification-specific metrics (accuracy, F-1 score, etc) on the validation set at the end of every epoch. """)

    with tab4:
        st.info("""🦾 The OpenAI API can be applied to virtually any task that involves understanding or generating natural language or code.
        \n**Key concepts:**
        \n- **Prompts and completions :** The completions endpoint is at the center of our API. It provides a simple interface to our models that is extremely flexible and powerful. You input some text as a prompt, and the model will generate a text completion that attempts to match whatever context or pattern you gave it. 
        \n- **Tokens :** Tokens can be words or just chunks of characters. For example, the word “hamburger” gets broken up into the tokens “ham”, “bur” and “ger”, while a short and common word like “pear” is a single token. Many tokens start with a whitespace, for example “ hello” and “ bye”.""")

    with tab6:
        st.image("200.png", caption="Final product")
        