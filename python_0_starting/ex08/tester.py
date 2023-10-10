from time import sleep
from tqdm import tqdm
from colorama import Fore
from Loading import ft_tqdm

print(Fore.BLUE)
for elem in ft_tqdm(range(3)):
    sleep(0.005)
print(Fore.LIGHTMAGENTA_EX)
for elem in tqdm(range(3)):
    sleep(0.005)
print(Fore.BLUE)
for elem in ft_tqdm(range(33)):
    sleep(0.005)
print(Fore.LIGHTMAGENTA_EX)

for elem in tqdm(range(33)):
    sleep(0.005)
print(Fore.BLUE)
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print(Fore.LIGHTMAGENTA_EX)
for elem in tqdm(range(333)):
    sleep(0.005)
print(Fore.RESET)
