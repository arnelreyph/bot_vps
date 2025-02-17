import json

def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

def main():
    config = load_config()
    # Example usage of the config
    print(f"Setting1: {config['setting1']}")
    print(f"Setting2: {config['setting2']}")
    print(f"Subsetting1: {config['setting3']['subsetting1']}")
    print(f"Subsetting2: {config['setting3']['subsetting2']}")

if __name__ == "__main__":
    main()
