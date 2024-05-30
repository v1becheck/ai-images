** Work in progress

Install: https://github.com/conda-forge/miniforge

If you are not setting miniforge into PATH you can use Miniforge Prompt app

- For nVidia GPUs run: mamba create -n <yourEnvName> python=3.11 pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
- run: mamba activate <yourEnvName>
- run: python -m pip install diffusers transformers tokenizers accelerate peft datasets loguru requests devtools einops

Got to your project folder.
- check the CUDA version your GPU is using
- run: pip install torch --user --extra-index-url https://download.pytorch.org/whl/cu117
