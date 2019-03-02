
from TFGeneration.GenerateTFRecord import *
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--filesize',type=int,default=100)
args=parser.parse_args()

t = GenerateTFRecord('gentables/','tfrecords/',args.filesize)
t.write_to_tf()