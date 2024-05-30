from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_pretrained("John6666/real-pony-real-anime-v4-sdxl", torch_dtype=torch.float16)
with torch.inference_mode():
    pipe = pipe.to('cuda')
    image = pipe(
        "score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, upper portrait, elf with extremely long ears, masterpiece cinematic lighting", # the prompt
        negative_prompt="worst quality, low quality, score_1, score_2, score_3", # the negative prompt
    ).images[0]
    image.save("image_of_elf_with_long_ears.jpg", quality=95)