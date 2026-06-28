from openai import OpenAI
import ai_back as Background_2


class AI():

    def __init__(self):
       self.url = "https://integrate.api.nvidia.com/v1"
       
    def AI_model(self):

        user_input = input("Enter your API key for using ai model (MisteralAI/nemtrone/NVIDIA_MODELS): ")
                
        print(Background_2.logo)
        running = True

        client = OpenAI(
            base_url = self.url,
            api_key = user_input                                               
        )

        while running:
            prompt = input("Enter your prompt:  ")

            if prompt == "exit --model":
                running = False

                completion = client.chat.completions.create(
                model="mistralai/mistral-nemotron",
                messages=[{"role":"user","content": "Say me bye!."}],
                temperature=0.6,
                top_p=0.7,
                max_tokens=4096,
                stream=True
                )
                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                        print(chunk.choices[0].delta.content, end="")
            else:
                completion = client.chat.completions.create(
                model="mistralai/mistral-nemotron",
                messages=[{"role":"user","content": prompt}],
                temperature=0.6,
                top_p=0.7,
                max_tokens=4096,
                stream=True
                )

                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                        print(chunk.choices[0].delta.content, end="")
            
            