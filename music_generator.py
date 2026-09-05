from transformers import AutoProcessor, MusicgenForConditionalGeneration
from scipy.io.wavfile import write

model_name = "facebook/musicgen-small"

processor = AutoProcessor.from_pretrained(model_name)

model = MusicgenForConditionalGeneration.from_pretrained(model_name)

print("MusicGen model loaded!")

prompt = "Generate a relaxing lo-fi instrumental music with soft piano and calm beats."

print(f"prompt: {prompt}")

inputs = processor(
    text=[prompt],
    padding=True,
    return_tensors="pt"
)

print("Prompt processed successfully!")

audio_values = model.generate(**inputs, max_new_tokens=256)

print("Music generated successfully!")

sampling_rate = model.config.audio_encoder.sampling_rate
audio = audio_values[0, 0].numpy()

write("generated_music.wav", sampling_rate, audio)

print("Music saved successfully!")