"""

Custom nodes for SDXL in ComfyUI

MIT License

Copyright (c) 2023 Searge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from .data_utils import retrieve_parameter
from .names import Names
from .ui import UI


# ====================================================================================================
# Outputs for SDXL Sampler
# ====================================================================================================

class SeargeSDXLSamplerV4Outputs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
            "optional": {
                "data": ("SRG_DATA_STREAM",),
                "sampler_output": ("SRG_DATA_STREAM",),
            },
        }

    RETURN_TYPES = ("SRG_DATA_STREAM", "LATENT",)
    RETURN_NAMES = ("data", "latent",)
    FUNCTION = "output"

    CATEGORY = UI.CATEGORY_SAMPLING

    @staticmethod
    def get_data(data=None, sampler_output=None):
        if sampler_output is None:
            sampler_output = retrieve_parameter(Names.SAMPLER_OUTPUT, data)

        if sampler_output is None:
            return (False, None,)

        return (True, {
            Names.LATENT_IMAGE: sampler_output,
        })

    def output(self, data=None, sampler_output=None):
        (has_data, output) = self.get_data(data, sampler_output)
        if not has_data:
            return (data, None,)

        return (data, output[Names.LATENT_IMAGE],)