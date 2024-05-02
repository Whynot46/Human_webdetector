#pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/cu118/torch_stable.html
import torch

torch.zeros(1).cuda()
print(torch.cuda.is_available())
print(torch.cuda.device_count())