from diffusers import AutoPipelineForText2Image
import torch

def img_gen(prompt,prompt1,prompt2):
    pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
    pipe.to("cuda")

    image1 = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
    image1.save(r"D:\intelhack\okay\src\images\new1.png")
    image2 = pipe(prompt=prompt1, num_inference_steps=1, guidance_scale=0.0).images[0]
    image2.save(r"D:\intelhack\okay\src\images\new2.png")
    image3 = pipe(prompt=prompt2, num_inference_steps=1, guidance_scale=0.0).images[0]
    image3.save(r"D:\intelhack\okay\src\images\new3.png")
    #D:\intelhack\okay\public\videos