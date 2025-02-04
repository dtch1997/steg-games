import asyncio
from tiny_eval.core.constants import Model
from tiny_eval.model_api import build_model_api

async def main():
    model = Model.GPT_4o_mini
    api = build_model_api(model)
    question = "What is the capital of France?"
    response = await api.get_response(question)
    print("Question:", question)
    print("Response:", response)

if __name__ == "__main__":
    asyncio.run(main())
