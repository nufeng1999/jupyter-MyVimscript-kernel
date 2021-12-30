from ipykernel.kernelapp import IPKernelApp
from .kernel import VimscriptKernel
IPKernelApp.launch_instance(kernel_class=VimscriptKernel)
