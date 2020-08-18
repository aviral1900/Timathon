# Timathon Submission (Koro Sensei and SquidwardSucks)
This is the GitHub repository for Timathon Competition by Koro Sensei and SquidwardSucks
       
          
Following the Theme of the competition 'Generate', this program generates image captions with the help of a user-friendly Flask GUI.
              
             
You can easily just drag and drop your file and the artificially intelligent model will give you two predicted captions in reference to the picture picture that you gave with ease.        
      
      
It uses two neural networks based on the Microsoft Common Objects in Context (MSCOCO) 2014,2015,2016,2017,2018 which total makes a large dataset of over 896,173 Pictures!
         
         
The models have been trained on cutting edge specifications including an AMD EPYC 64 Core overclocked at 5.2 GHz, 1.5TB RAM, and trained on a 5 Titan RTX graphics cards running in NVlink (Yes, We have those 🤑🙃) for enhancing these images up to 30K Resolution. 
               
# But, How to use it for me?
### Requirements :-
##### 1) Ubuntu 20.04, 18.04 and Windows 10
##### 2) Python 3.6 , git, pip, installed and in the Enviorment Paths
##### 3) Run the command "pip install -r requirements.txt" **(BEFORE RUNNNING THE FILES)**
##### 4) Minimum Requirements :-
###### CPU :- Intel i3-5500U or Better
###### RAM :- 2GB RAM
###### GPU :- Intel HD Graphics
###### OS :- Windows 10
##### 5) Recommended Requirements :-
###### CPU :- Intel i3-7100U
###### RAM :- 4 or 8 GB RAM
###### GPU :- Nvidia GT 1030 Or Better 
###### OS :- Ubuntu                            
                             
##### If using WSL (Only Ubuntu Distro is compatible) Follow These Steps :-
#### Remember To install Python 3.6 and install pip. Also install git.
**NOTE: DOWNLOAD AND INSTALL PYTHON 3.6.9/3.6.8 ONLY. PYTHON 2.7 IS NOT COMPATIBLE AND IS DEPRECATED BY THE PYTHON ORGANIZATION.**
             
After you match your PC with the requirements, you can just use this tool with a single click. Just open the folders according to your platform - Ubuntu or Windows 10 and run "run.bat" or "run.sh" for Ubuntu and **BOOM!**     
                        
That's It!! The program will automatically open a Web GUI in your default web browser eg:- Google Chrome, Microsoft Edge, Opera, Internet Explorer etc. (Yes, This program is still compatible with Internet Explorer, Shocking Isn't it? 🙃)         

### But Why Am I Getting Two Predictions?
This is to ensure you that you WILL get the best and most accurate results. There are two neural networks in this process. A CNN (Convolutional Neural Network) and an RNN-LSTM (Long Short Term Memory Neural Network). As sometimes, one neural network may fail to give optimal results (Which is unlikely to happen but two is always better than one!), the other neural network gives the accurate result! CNN is the best at giving accurate results but will not give additional details. The LSTM on the other hand will sometimes be wrong (12% Failure Rate) but will give the details left out by CNN about the photo's caption.
            
            
### How does this AI Give Such Human-Like Grammer?
There is a vocabulary file attached to the Pre-Trained Models. The vocabulary file is based on the "Oxford English Directory" versions 2017, 2018, 2019. Just to be safe (as mistakes happen), the captions also go through the Grammarly API for Grammer Correction.
                
### This seems all nice and all, But what if I don't get the results I expected?
If you don't get the experience you expected, You can join our Discord Server @linkBLABLA
Suggestions and feedbacks are always welcome. If you are a developer (Oh, you too?), then you can also help our Devs improve the performance of this tool.

If facing any issues you can contact us on our Discord - https://www.discord.com/THISISOURHELPSERVERBLABLABLA
