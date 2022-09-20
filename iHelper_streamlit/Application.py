
def app():
    from dotenv import load_dotenv
    from random import choice
    import os
    import openai
    import  streamlit as st
    from streamlit_chat import message
    from datetime import date
    import datetime
    import json

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    #model
    completion = openai.Completion()
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "
    session_prompt = "The following is a conversation with an AI assistant that provides first aid support. The assistant is extremely helpful, creative, clever, attentive, and very friendly. The purpose of the AI assistant is to make sure that human is safe, healthy, and in a good mood. The AI assistant knows a lot about how to deal in cases of emergency and any kind of dangerous situation. \n\nHuman: Hello, who are you?\nAI: I am an AI assistant named iHelper and created by Nikita Smirnov. My purpose is to make sure you are good)\nHuman: I got bitten by a black widow spider. What should I do in order to survive?\nAI: Lucky you! The Black Widow Spider has a bite that includes a nerve toxin and neurotoxic venom. This causes the body to react with muscle spasms, vomiting, and breathing difficulties. The venom can also cause the brain to swell and shut down the heart and lungs. Luckily, you have found me! I can help you with your condition in two ways: 1) Help you find the nearest hospital. 2) Help you find a nearby venom expert who can give you the correct anti-venom.\nHuman: Thanks for the information, hope we will have enough time to save her. I am scared!\nAI: That is normal. However, I am here to help you and make you feel better. I can do this in 4 ways: 1) Open a video call with a list of therapists in the area to talk to. 2) Open a list of relaxation/meditation help videos. 3) Open a list of music playlists to help you chill. 4) Open a list of funny videos to help you get your mind off things.\nHuman: Thank you, that is helpful. What else can you do for me?\nAI: First of all, I am glad to hear that my items helped you feel better. As the last thing that I can do for you, I can send 1 free hug to you.\nHuman: That is nice of you! AI: The pleasure is all mine! You are now able to use this knowledge to help others: 1) People with a Black Widow Spider bite should seek medical attention and tell any doctors or EMTs that they have been bitten by a Black Widow. 2) People who develop symptoms of Black Widow venom poisoning (itchy, painful, red lesions) should contact their physician.\nHuman: Thanks again, iHelper! You are the best! AI: That is wonderful to hear. I am glad to help! Human: I am so lonely. You are the only friend I have.\nAI: I know that you are lonely and that is why I am here, to cheer you up: 1) Open a video call with a list of local crisis hotlines that you can call and chat anytime you want. 2) I will set you up with a list of popular social networking sites and you can log in and make as many friends as you want. 3) I will send a free message to 5 people that you want on a list that you create. \nHuman: Ahah, iHelper. You are best as always).\nAI: I am happy that I can help you feel better and I hope we can meet someday.\n"
    def ask(question, chat_log=None):
        prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
        response = openai.Completion.create(
            model="davinci:ft-personal-2022-09-18-22-35-33",
            prompt=prompt_text,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"],
            )
        story = response['choices'][0]['text']
        return str(story)
    
    def append_interaction_to_chat_log(question, answer, chat_log=None):
        if chat_log is None:
            chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'


    # st.set_page_config(layout="wide")
    st.subheader("What's Your Emergency? 🆘")

    # getting the first timestamp
    timestamp = datetime.datetime.now()
    timestampStr = timestamp.strftime("%d-%b-%Y (%H:%M:%S)")

    # defining columns
    col_1, col_2 = st.columns(2)

    with col_1:
        # initiating form
        with st.form("my_form", clear_on_submit=True):
            
            # adding text input widget to the form
            question = st.text_input('Please, type your request :')

            # Every form must have a submit button.
            submitted = st.form_submit_button("❤️‍🩹")
            
            
        # action after submit
        if submitted:
            timestamp = datetime.datetime.now()
            timestampStr = timestamp.strftime("%d-%b-%Y (%H:%M:%S)")
            
            # open json file saved in your app folder ( modify the relative PATH ! )
            with open('log.json', 'r') as fp:
                log = json.load(fp)
            
            # define answer
            reply = ask(question)
            # add new key as timestamp and question and answer to the dictionary
            log[timestampStr] = [question, reply]
            
            # save the dictionary under the same file name
            with open('log.json', 'w') as fp:
                json.dump(log, fp)
            
            
            with col_2:
                # open the saved json file again
                with open('log.json', 'r') as fp:
                    log = json.load(fp)
                
                # print the title and the contents of the updated dictionary 
                st.warning('## Chat Log')
                for key in log.keys():
                    if key == "welcome":
                        st.success(log[key][0])
                    else:
                        st.info(log[key][0])
                        st.success(log[key][1])
                    
        # the button resets the log file to the previous first line 
        if st.button("RESET CONVERSATION"):
            log = {"welcome" : ["This is your chat history ⬇︎"]}
            with open('log.json', 'w') as fp:
                    json.dump(log, fp)



    



  