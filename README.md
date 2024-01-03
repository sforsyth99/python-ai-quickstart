# Get started with AI in Python
This project demonstrates how easy it is to get up and running with AI in Python. 
The first sample shows how to use the Stable Diffusion API to generate images from
a text prompt using 8 lines of code. The second sample shows how to use the 
zephyr-7b-alpha LLM to generate text from a prompt using 9 lines of code.

If you're new to Python, you'll want to install a program like PyCharm or Jupyter Notebooks 
so you can run the code. You can even run these samples from the Python command 
line.

There are some Python libraries you'll need to install to use these samples. Add them to your 
project in PyCharm, or install them with pip:
* transformers
* diffusers
* torch
* matplotlib (to view images if you aren't using Jupyter Notebooks)

## Hello-diffusers.py
This sample generates images from a simple text prompt using the StableDiffusion v5.1 API.
Play around with the text prompt to generate different images. 

Some things to note about running this sample: 
* Running the script requires internet access.
* It can take a minute or two to generate the image.
* You may need to change the "mps" parameter to something else depending on your hardware.

## Hello-transformers.py
This sample shows how to use a Chat-GPT-like LLM to generate responses from a prompt. 
You can ask it almost anything - tell me a joke, write code, answer geography questions, etc.

The first time you run this sample it will download about 18GB of data 
to your computer (on a mac it is cached in /Users/username/.cache/huggingface)
After that, you don't require internet access to use the model - it's like
downloading the entire internet on to your computer. It's really quite impressive.

Generating answers can take a few minutes, and the longer the response the more time it takes.
You can tweak the length of the response - I recommend starting off with a lower number like
100 tokens and then increasing it as you play around. On my computer, generating a
response of 1000 tokens takes about 6 minutes. Your mileage may vary.






