## Introduction to Computer Graphics with Python and OpenGL

* Include my individual work to complete given three assignment of the course.
* Development environment python version is 2.7.15rc1:
  ```
      Package             Version
    ------------------- -------
    numpy               1.16.2 
    pip                 19.0.3 
    pygame              1.9.5  
    PyOpenGL            3.1.0  
    PyOpenGL-accelerate 3.1.0  
    setuptools          41.0.0 
    wheel               0.33.1 

  ```
* Example usage of the program:
  ```
  python assignment3.py ecube.obj
  ```
  
  ```text

  ------------------------ KEY CONFIGURATION ------------------------
  1 -> switch mainCamera
  2 -> switch cam2
  3 -> selected camera free move
       -> w -> in
       -> s -> out
       -> a -> right
       -> d -> left
       -> e -> up
       -> r -> down
       -> up -> pitch up
       -> down -> pitch down
       -> left -> yaw left
       -> right -> yaw right
  4 -> select object
  (Not Valid)5 -> select sphere
  (Not Valid)6 -> select cylinder
  + -> increase subdivision for selected shape
  - -> decrease subidivison for selected shape
  Select a shape and move using
   Scene Space
       -> w -> up
       -> s -> down
       -> a -> left
       -> d -> right
       -> e -> in
       -> r -> out
   Local Space
       -> up
       -> down
       -> left
       -> right
  Rotation of selected shape
   -> k -> scene space use x, y, z button to rotate
   -> l -> local space use x, y, z button to rotate
  -------------------------- END ---------------------------------------
 
  ```
  
* Screenshots from development view:

  
![alt text](https://github.com/feyil/CENG487/blob/master/screenshots/fromcam2.png "Page 1")

![alt text](https://github.com/feyil/CENG487/blob/master/screenshots/multipleobject.png "Page 2")

![alt text](https://github.com/feyil/CENG487/blob/master/screenshots/opengl1.png "Page 3")

![alt text](https://github.com/feyil/CENG487/blob/master/screenshots/subdividewithrotation.png "Page 3")

  

  


