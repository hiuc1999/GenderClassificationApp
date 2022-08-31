# Face Recognition Gender Classification App
App Depoloyed on Heroku: https://genderclassification-hc99.herokuapp.com/

<a href="https://www.linkedin.com/in/hiu-ching-lau-947501207">Visit my  LinkedIn profile</a>

<img src="https://genderclassification-hc99.herokuapp.com/static/images/index.png" width="600" />
<p><sub><a href="https://rankone.io/2018/11/02/how-automated-face-recognition-fr-works/">image source</a></sub></p>

<h3>1. Machine Learning Model Building</h3>
    <ol style="list-style-type:lower-alpha">
        <li>Data Collection</li>
        Data used for model training : <a href="https://www.kaggle.com/datasets/ashishjangra27/gender-recognition-200k-images-celeba"> Gender Classification 200K Images | CelebA Dataset from Kaggle</a>
        <li>Data Preprocessing</li>
        <ol style="list-style-type:lower-roman">
            <li>Convert all images to grayscale images</li>
            <li>Crop faces (detected by <a href="https://github.com/opencv/opencv/tree/master/data/haarcascades">Haar Cascade Classifier</a>) from the images</li>
            <li>Resize cropped image (faces)  to size 100*100</li>
            <li>Structure the pixel values into a dataframe</li>
        </ol>
        <li>Feature Extraction</li>
        <ol style="list-style-type:lower-roman">
            <li>Subtract mean face of the dataset  from each face image</li>
            <li>Perform Principal Component Analysis(PCA)  to find eigen faces</li>
        </ol>
        <li>Machine Learning Model Training</li>
        <ol style="list-style-type:lower-roman">
            <li>Grid Search to look for best parameters of  Support Vector Machine (SVM) Classifier</li>
        </ol>
        <li>Create an ML Pipeline</li>
        <ol style="list-style-type:lower-roman">
            <li>Put steps from data preprocessing to model training together and create a pipeline</li>
        </ol>
    </ol>
    <p> All the notebooks are available in this repository.
    <br>
    <h3>2. Flask-based Web Application Development</h3>
    <ol style="list-style-type:lower-alpha">
        <li>Web Application Design</li>
        <ol style="list-style-type:lower-roman">
            <li>Store all the common elements in a base template by <a href="https://flask.palletsprojects.com/en/2.2.x/patterns/templateinheritance/">template inheritance</a></li>
            <li>Create different routes and templates for pages in the web-app</li>
            <li>HTML, CSS Styling</li>
        </ol>
        <li>ML Model Integrate into the Web-App</li>
        <li>Deployment on <a href="http://heroku.com">Heroku Cloud</a></li>
    </ol>
  


<br><br>

Useful Links:
1. https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08 </a>
2. https://www.geeksforgeeks.org/ml-face-recognition-using-eigenfaces-pca-algorithm/
3. https://medium.com/swlh/image-classification-using-machine-learning-and-deep-learning-2b18bfe4693f 
4. https://www.udemy.com/course/build-face-recognition-app-using-machine-learning-in-flask/ 
