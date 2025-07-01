from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load once globally
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def summarize_text(text, max_input_len=512, max_output_len=100):
    # Prepend prefix as expected by T5
    input_text = "summarize: " + text.strip().replace("\n", " ")
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=max_input_len, truncation=True)

    summary_ids = model.generate(
        input_ids,
        max_length=max_output_len,
        min_length=30,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
