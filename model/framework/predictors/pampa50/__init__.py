import sys
import os

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

from predictors.utilities.utilities import load_gcnn_model


pampa_model_file_url = os.path.abspath(os.path.join(root, '../../../checkpoints/gcnn_model.pt'))
pampa_model_file_path = os.path.abspath(os.path.join(root, '../../../checkpoints/gcnn_model.pt'))

print(f'Loading PAMPA graph convolutional neural network model', file=sys.stdout)
pampa_gcnn_scaler, pampa_gcnn_model = load_gcnn_model(pampa_model_file_path, pampa_model_file_url)

del pampa_model_file_url
del pampa_model_file_path

print(f'Finished loading PAMPA 5.0 models', file=sys.stdout)
