from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_post(text, tone="professional"):
    prompt = f"Write a {tone} LinkedIn post about this achievement: {text}\nInclude relevant hashtags at the end."
    output = generator(prompt, max_length=120, do_sample=True, top_k=50, temperature=0.8)
    return output[0]["generated_text"].strip()
def generate_post(achievement):
    hashtags = "#Java #Certification #CodeTantra #LearningNeverStops #CareerGrowth #Tech"
    return f"""🚀 I'm thrilled to share a new achievement:

✅ {achievement.capitalize()}

I'm proud to continue expanding my skillset and staying updated in the tech world. Grateful for the opportunity and support!

{hashtags}
"""
