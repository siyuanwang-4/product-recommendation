from zai import ZhipuAiClient
import os

def agent(products, user_like):
    
    prompt = """Based on all product names and the products the user likes, infer what other products the user might be interested in:
    Product names: {{products}}, User's liked products: {{user_like}}
    Please directly output the product names, do not output other content."""
    

    # Call ZhipuAI's chat.completions.create method to get response
    # client = ZhipuAiClient(api_key=os.getenv("ZAI_API_KEY"))
    client = ZhipuAiClient(api_key="your api key")
    response = client.chat.completions.create(
        model="GLM-4.5-Flash",
        messages=[
            {
                "role": "user", 
                "content": prompt.replace("{{products}}", str(products)).replace("{{user_like}}", str(user_like))
            }
        ],
        thinking={
            "type": "disabled",    # Do not enable deep thinking mode
        },
        stream=True,
    )
    for chunk in response:
        # Streaming return
        yield chunk.choices[0].delta.content

        
    
if __name__ == "__main__":
    products = ["men's T-shirt", "casual shorts", "sports shoes", "floral dress"]
    user_like = "men's suit"
    for i in agent(products, user_like):
        print(i, end="")