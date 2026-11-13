import yaml, random
import numpy as np


def load_config(path="configs/config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    # torch.manual_seed(seed)  # uncomment when using PyTorch


def main():
    cfg = load_config()
    set_seed(cfg["seed"])
    print("Config loaded:", cfg["project"])
    # TODO: build data loaders, model, training loop from cfg


if __name__ == "__main__":
    main()
