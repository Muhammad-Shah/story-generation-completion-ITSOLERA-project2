import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import find_dotenv, load_dotenv

dotenv_path = '.env'
load_dotenv(dotenv_path)
GROQ_API = os.getenv('GROQ_API')



def llm(temperature):
    return ChatGroq(temperature=temperature,
                    model_name="Llama3-70b-8192",
                    api_key=GROQ_API,
                    max_tokens=1000,
                    model_kwargs={
                        "top_p": 1,
                        "frequency_penalty": 0.5,
                        "presence_penalty": 0.9
                    }
                    )


def generate(topic, length, genre, temperature=0.7, paragraphs=3):
    generation_system_message_content = """
    You are a creative and imaginative assistant specialized in generating stories. 
    When given a prompt, you will generate an engaging and coherent story based on the specified genre and length.
    Your stories should be vivid, imaginative, and suitable for the specified genre. Be sure to maintain a consistent theme and style.
    """

    human_message_content = f"""
    Please generate a story based on the following prompt: "{topic}".
    The story should be in the "{genre}" genre, approximately {length} words long, and consist of around {paragraphs} paragraphs.
    """

    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage(content=generation_system_message_content),
        HumanMessage(content=human_message_content),
    ])

    response = completion(prompt=prompt_template, topic=topic, length=length, genre=genre, paragraphs=3)
    return response


def complete(partial_story, length, genre,  temperature=0.7, paragraphs=3):
    completion_system_message_content = """
    You are a creative and imaginative assistant specialized in completing stories. 
    When given a partial story, you will complete it in the same style and tone, ensuring the story flows naturally.
    Your completions should be vivid, imaginative, and suitable for the specified genre. Be sure to maintain the theme and style consistent with the given partial story.
    """

    human_message_content = f"""
    Please complete the following story: `{partial_story}`.
    The completion should be in the `{genre}` genre, approximately `{length}` words long, and consist of around {paragraphs} paragraphs.
    """

    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage(content=completion_system_message_content),
        HumanMessage(content=human_message_content)
    ])

    # formatted_prompt = prompt_template.format(
    #     partial_story=partial_story,
    #     length=length,
    #     genre=genre,
    #     paragraphs=paragraphs
    # 
    # print(formatted_prompt)

    response = completion(prompt=prompt_template, topic=partial_story, length=length, temperature=temperature, genre=genre, paragraphs=3)
    return response

def completion(prompt, topic, length, genre, temperature=0.7, paragraphs=3):
    llm = llm(temperature)
    llm_chain = prompt | llm
    response = llm_chain.invoke({"topic:": topic, "length:": length, "genre:": genre, "paragraphs:": paragraphs}).content
    return response