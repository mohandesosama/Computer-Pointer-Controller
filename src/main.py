from face_detection import FaceDetection
import argparse
import sys

face_model_name = 'face-detection-adas-binary-0001'
def main(args):
    face_detect_model = FaceDetection(face_model_name,device='CPU')
    face_detect_model.load_model()
    
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',required=True)
    parser.add_argument('--device',default='CPU')
    args=parser.parse_args()
    sys.exit(main(args) or 0)

