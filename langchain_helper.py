import os

from dotenv import load_dotenv
from langchain.chains import LLMChain, SequentialChain, SimpleSequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = OpenAI(temperature=0.6)


def generate_restaurant_name_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food.suggest a fancy name for it.Return only one result.",
    )

    # prompt_template_name.format(cuisine="Italian")

    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="restaurant_name"
    )
    # chain.run("American")

    prompt_template_menu = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name} and return in a comma-separated format",
    )

    # prompt_template_name.format(cuisine="Italian")

    menu_chain = LLMChain(llm=llm, prompt=prompt_template_menu, output_key="menu_items")
    # chain.run("Stateside Bistro")

    chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    response = chain({"cuisine": cuisine})

    return response
