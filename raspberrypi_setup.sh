#!/usr/bin/env bash

# Colors
GREEN="\e[32m"
YELLOW="\e[33m"
NC="\e[0m" # No Color

# Spinner function
spinner() {
    local pid=$!
    local delay=0.1
    local spin='|/-\'
    while ps -p $pid > /dev/null; do
        printf "\r${YELLOW}Installing... ${spin:0:1}${NC}"
        spin=${spin:1}${spin:0:1}
        sleep $delay
    done
    printf "\r${GREEN}✔ Done!${NC}\n"
}

echo -e "${GREEN}==== Raspberry Pi Setup Script ====${NC}"

sleep 1

echo -e "\n${YELLOW}>> Enabling I2C...${NC}"
sudo raspi-config nonint do_i2c 0
echo -e "${GREEN}✔ I2C Enabled${NC}"

echo -e "\n${YELLOW}>> Updating system packages...${NC}"
sudo apt update & spinner
sudo apt upgrade -y & spinner

echo -e "\n${YELLOW}>> Installing Python & tools...${NC}"
sudo apt install -y python3 python3-pip python3-venv git libatlas-base-dev & spinner

echo -e "\n${GREEN}✔ Python environment ready${NC}"

# Create virtual environment
echo -e "\n${YELLOW}>> Creating virtual environment 'ai-env'...${NC}"
python3 -m venv ~/ai-env
source ~/ai-env/bin/activate

echo -e "${GREEN}✔ Virtual environment activated${NC}"

echo -e "\n${YELLOW}>> Installing NumPy & OpenCV...${NC}"
pip install --upgrade pip & spinner
pip install numpy opencv-python & spinner

echo -e "${GREEN}✔ NumPy & OpenCV installed${NC}"

echo -e "\n${YELLOW}>> Installing Coral TPU Runtime & PyCoral...${NC}"
# TPU Runtime
echo -e "${YELLOW}Downloading Edge TPU runtime...${NC}"
wget https://packages.cloud.google.com/apt/doc/apt-key.gpg & spinner
sudo apt-key add apt-key.gpg
sudo add-apt-repository "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" -y
sudo apt update & spinner
sudo apt install -y libedgetpu1-std python3-tflite-runtime & spinner

# PyCoral
pip install pycoral & spinner

echo -e "\n${GREEN}✔ Coral Accelerator support installed${NC}"

echo -e "\n${GREEN}==== Setup Completed Successfully! ====${NC}"
echo -e "To activate your environment later, run:\n"
echo -e "${YELLOW}source ~/ai-env/bin/activate${NC}\n"
