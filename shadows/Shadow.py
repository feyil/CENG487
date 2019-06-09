from OpenGL.GL import *
from OpenGL.GLUT import *

from OpenGL.GLU import *

from cameras import Camera
from scenes import Scene

class Shadow(object):

    def __init__(self):
        self.__depthMapFBO = None      
        self.__depthMapTexture = None
 
        self.__bufferWidth = None
        self.__bufferHeight = None

        # reference to Camera object, we can obtain lookAt
        self.__lightView = None
        self.__lightNum = None

        # to remember
        self.__activeCamName = None

    def createFrameBufferObject(self, numFBO=1):
        self.__depthMapFBO = glGenFramebuffers(numFBO)
        self.__numFBO = numFBO
        return self.__depthMapFBO

    def getFBO(self):
        return self.__depthMapFBO

    def create2DTexture(self, textureNum=1):
        self.__depthMapTexture  = glGenTextures(textureNum)
        self.__textureNum = textureNum
        return self.__depthMapTexture

    def getDepthMapTexture(self):
        return self.__depthMapTexture

    def configureTexture(self, width=800, height=600):
        self.__bufferWidth = width
        self.__bufferHeight = height

        glBindTexture(GL_TEXTURE_2D, self.__depthMapTexture)
        
        glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, width, height, 0, GL_DEPTH_COMPONENT, GL_FLOAT, None)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        
        #glBindTexture(GL_TEXTURE_2D, 0)
    
    def getBufferWxH(self):
        return [self.__bufferWidth, self.__bufferHeight]

    def attachFrameBufferDepthBuffer(self):
        glBindFramebuffer(GL_FRAMEBUFFER, self.__depthMapFBO)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, self.__depthMapTexture, 0)
        glDrawBuffer(GL_NONE)
        glReadBuffer(GL_NONE)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)  

    def createLightView(self, lightNum, lightPos, directionFront, upVector):
        self.__lightNum = lightNum

        cam = Camera()
        cam.setCameraFront(*directionFront)
        cam.setCameraPosition(*lightPos)
        cam.setWorldUp(*upVector)
        #cam.linearMove(CamMovement.FORWARD, 0.001) # little trick to focus the target point
        cam.updateCamera()

        self.__lightView = cam
        return self.__lightView

    def updateSceneWithLightView(self, scene):
        if(self.__lightView != None):
            # scene.lightsON(False)
            # scene.lightON(self.__lightNum, False)

            self.__activeCamName = scene.getActiveCameraName()

            scene.addCamera("lightView", self.__lightView)
            scene.selectCamera("lightView")
        else:
          #  print("Light View None")
          pass

    def recoverSceneView(self, scene):
        if(self.__activeCamName != None):
            scene.selectCamera(self.__activeCamName)
            # scene.lightON(self.__lightNum, True)
            # scene.lightsON(True)
            

    def renderDepthMap(self, scene):
        #glViewport(0, 0, width, height)
        glBindFramebuffer(GL_FRAMEBUFFER, self.__depthMapFBO)
        glClear(GL_DEPTH_BUFFER_BIT)
        
        # Render scene
        self.updateSceneWithLightView(scene)
        scene.draw()

        #self.recoverSceneView(scene)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)

        

        return self.__depthMapTexture
    
    def bindFBO(self, logic=True):
        if(logic):
            glBindFramebuffer(GL_FRAMEBUFFER, self.__depthMapFBO)
        else:
            glBindFramebuffer(GL_FRAMEBUFFER, 0)

    def initializeShadowComponents(self):
        self.__depthMapFBO = self.createFrameBufferObject()
        
        self.__depthMapTexture = self.create2DTexture()
        self.configureTexture()

        self.attachFrameBufferDepthBuffer()
        
