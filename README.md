# image-kernels-heroku

This is an app I built with streamlit, and the Open Source Computer Vision Library (OpenCV) in Python to display the effects of image kernels on uploaded images.
I also included the option for a user to input their own custom kernel and observe its filtered effect on the image in real time.

Here is a link to the deployed app on [Heroku](https://image-kernel-app.herokuapp.com/).

PS: due to Heroku's dyno delay on loading deployed app, I have moved this app to be deployed on [Streamlit Cloud Share](https://bwhiz-image-kernels-heroku-filter-app-6oct32.streamlit.app/).

Below is a snapshot for a demo of the app :

![alt text](https://github.com/Bwhiz/image-kernels-heroku/blob/main/image_kernel_sc.png)

## Running locally

Follow the instructions below to run this app locally.

### Create a virtual environment (optional)
If you want to use a virtual environment, you can create one using the command below:

```bash
python3 -m venv ./venv
```

After creating the virtual environment, you need to activate it. Use the command below to do that:

```bash
python -m venv ./venv
```

If you need do deactivate the virtual environment, you can do that using the command below:

```bash
deactivate
```

### Install requirements

To install requirements, run the command below:

```bash
pip install -r requirements.txt
```

### Running the app

You can run the app using the command below:

```bash
streamlit run filter_app.py
```

Note that streamlit is installed as a CLI tool after you install requirements. If you created a virtual environment, Streamlit will be scoped to your current directory which means it won't be available globally on your machine.


