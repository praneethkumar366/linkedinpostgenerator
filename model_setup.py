from transformers import pipeline

generator = pipeline("text2text-generation", model="t5-small")
text = "summarize: I completed the AWS cloud certification with excellence in the exam"
result = generator(text, max_length=80, do_sample=False)
print(result[0]['generated_text'])
