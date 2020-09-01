## Timathon Submission of I'm Batman 2 and Koro Sensei

Just navigate to the website ( http://52.91.153.72 ) and test out our project.
### Check out the `example_0.png` file above, to view a sample run.

Few model files were to big to upload on github so we have provided the link to the files along with the locations they reside.

Since running the project locally is kinda cumbersome, since you have to download 500MB size of this repo and along with Huge dependencies, we recommend trying out the project on the link above instead, but if you want to run this project locally:

### We recommend downloading this repo in the link below because it contains the Complete project.
https://www.dropbox.com/sh/1dtvlbeis8zdkpp/AACPehGVTaPmp2XWWM5NlkHsa?dl=0

> Create a folder named ubuntu in your home directory like this.

>   `~/ubuntu/` and move the Timathon folder at this location

Path should look like `~/ubuntu/Timathon` 
Now follow these exaxt steps:
* Install the dependencies from the requirements.txt.
* Inside app.py change all the paths you find to the respective path of those files on your local machine:
  e.g. `"python3 ./AI/image_captioning/sample.py --image" + "{PUT RESPECTIVE PATH TO UPLOADS FOLDER HERE} + filename"`
* Now go to AI/image_captioning/sample.py and change the paths to all the files under `if __name__` code block:
  e.g. `/home/ubuntu/Timathon/AI/image_captioning/models` just change paths like these to the path that are on your machine


Have fun :)
