import onnxruntime
import numpy as np
from datetime import datetime

print(onnxruntime.get_device())

onnx_runtime_input = np.random.rand(1, 3, 224, 224).astype(np.float32)

sess_options = onnxruntime.SessionOptions()
sess_options.intra_op_num_threads = 15
sess_options.inter_op_num_threads = 1

ort_session = onnxruntime.InferenceSession("../model/craft.onnx", sess_options=sess_options, providers= ['CPUExecutionProvider'])
ort_inputs = {ort_session.get_inputs()[0].name: onnx_runtime_input}
t1 = datetime.now()
ort_outs = ort_session.run(None, ort_inputs)
print(ort_outs[0].shape)

t2 = datetime.now()
print("Time taken for Onnx model", str(t2-t1))
