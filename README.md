# SI-GuidedProject-611637-1700368667
## **Website Name - Agrosafe.ai**
### **Project Name - Safeguarding Agriculture: AI-Enabled Prognostication of Farm Insect Threats**
# **Team Members**
- [@saptarshi11 ](https://github.com/saptarshi11)
- [@Aakash-777](https://github.com/Aakash-777)
- [@subhradip-bo](https://github.com/subhradip-bo)
- [@Supratik5620](https://github.com/Supratik5620)

# Project Design
![WhatsApp Image 2023-11-21 at 20 51 20_4e34397a](https://github.com/smartinternz02/SI-GuidedProject-611637-1700368667/assets/96284263/2904d4d7-77d4-4af8-958f-93540f4973dc)


# **Feature 1**
![WhatsApp Image 2023-11-22 at 16 50 13_e06278db](https://github.com/smartinternz02/SI-GuidedProject-611637-1700368667/assets/96284263/ebb80f97-114c-425e-8f4d-ea205cbb4bc5)


We are storing the path of the image in the “image_path” variable. Then we are passing the
image to the pre-trained YOLOv8 model to make predictions which is getting stored in
“result” variable.Then the name of the predicted insect is fetched from the “result” variable
using “names_dict = results[0].names” which is getting stored in ‘names_dict” variable. Then,
we are storing the input image in the “testImage” variable. At last we are outputting the
image along with the predicted name of the insect.

# **Feature 2**
![WhatsApp Image 2023-11-22 at 16 45 51_c09dccd9](https://github.com/smartinternz02/SI-GuidedProject-611637-1700368667/assets/96284263/8d82651d-b27e-42a3-8e28-310b34bf53ca)
The model predicts the insect and gives additional information that would be helpful to the
user to effectively tackle their issues.

# Performance Testing
- Accuracy Training Accuracy = 0.958
- Validation Accuracy = 0.806


# Required software
Need to set up a development environment with the required software.

## Python:
- Install Python on your machine. You can download it from the official Python website. Make sure to add Python to your system's PATH during the installation.
## Ultralytics YOLOv8:
- Clone the YOLOv8 repository from the Ultralytics GitHub repository:

```
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -U -r requirements.txt
```
##HTML, CSS, JS:

- For web development, you don't need to install HTML, CSS, or JavaScript explicitly. These are interpreted by web browsers. Create HTML, CSS, and JS files as needed.
Flask:

Install Flask, a Python web framework, using pip:
```
pip install Flask
```
## Fetch API/AJAX:

- These are client-side technologies, so you don't need to install anything explicitly. You'll use them in your JavaScript code to make asynchronous requests to your Flask server.
## Code Editor:
- Choose a code editor or an integrated development environment (IDE) for your development work. Popular choices include Visual Studio Code, Atom, PyCharm, etc.
## Additional Libraries:
Depending on your specific project requirements, you might need additional Python libraries or JavaScript packages. For example, you might need a library like OpenCV for image processing in Python. 

# Source Code : 
https://github.com/smartinternz02/SI-GuidedProject-611637-1700368667

# Demonstration Link :  
https://drive.google.com/file/d/1lmKA9Ove_yYsgW3XuwBIC58aICoNpXJY/view?usp=drive_link

# Screenshot
- 1.[Webpage screenshot](https://github.com/smartinternz02/SI-GuidedProject-611637-1700368667/assets/96284263/7994feb0-50b7-4279-93d8-0abf0e6602f0)
- 2.[Uploading image for the detection of the insect](https://github.com/smartinternz02/SI-GuidedProject-611637-1700368667/assets/96284263/09d6f6d9-9d4a-4682-9adc-af770b37c66a)
- 3.[The prediction and the recommendation](https://github.com/smartinternz02/SI-GuidedProject-611637-1700368667/assets/96284263/3715a954-4647-43ea-97e1-97ce958fd246)





