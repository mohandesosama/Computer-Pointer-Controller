'''
This is a sample class for a model. You may choose to use it as-is or make any changes to it.
This has been provided just to give you an idea of how to structure your model class.
'''
from openvino.inference_engine import IENetwork, IECore

import numpy as np
class FaceDetection:
    '''
    Class for the Face Detection Model.
    '''
    def __init__(self, model_name, device='CPU', extensions=None):
        '''
        TODO: Use this to set your instance variables.
        '''
        self.device=device
        self.extensions=extensions
        self.model_name=model_name
        self.net=None
        self.model_path="../my_models/face_detection"
        self.model_weights = self.model_path + self.model_name + '/'+ '.bin'
        self.model_structure = self.model_path + self.model_name + '/' + '.xml'

        self.model=IENetwork(self.model_structure,self.model_weights)

        self.core=IECore()
        self.model = self.core.read_network(self.model_structure, self.model_weights)

        self.input_name = next(iter(self.model.inputs))
        self.input_shape = self.model.inputs[self.input_name].shape
        self.output_name = next(iter(self.model.outputs))
        self.output_shape = self.model.outputs[self.output_name].shape

    def load_model(self):
        '''
        TODO: You will need to complete this method.
        This method is for loading the model to the device specified by the user.
        If your model requires any Plugins, this is where you can load them.
        '''
        if not self.check_model():
            print("No all layers supported in the {} model".format(self.model_name))
            self.core.add_extension(self.extensions,self.device)
        else:
            print("model {} All layers are supported".format(self.model_name))
       
        try:
            self.net=self.core.load_netowrk(netowrk=self.model,device_name=self.device,num_requests=1)
        except Exception as e:
            print("Can't load the network .... exception {} occurred ".format(e))


    def predict(self, image):
        '''
        TODO: You will need to complete this method.
        This method is meant for running predictions on the input image.
        '''
        raise NotImplementedError

    def check_model(self):
         return check_layers_supported(self.core, self.model, self.device)

    def preprocess_input(self, image):
        '''
        Before feeding the data into the model for inference,
        you might have to preprocess it. This function is where you can do that.
        '''
        raise NotImplementedError

    def preprocess_output(self, outputs):
        '''
        Before feeding the output of this model to the next model,
        you might have to preprocess the output. This function is where you can do that.
        '''
        raise NotImplementedError
