# data_generation/model_execution.py
# model_execution/model_execution.py
import torch

def execute_model(model, input_data):
    # Execute model on input data
    output = model(input_data)

    # Return output
    return output

# Example usage
input_data = torch.randn(1, 10)  # dummy input data
model = torch.nn.Linear(10, 10)  # dummy model
output = execute_model(model, input_data)
print(output)
print(output)
