
import numpy

class daq(object):
    def __init__(self, ai, ao):
        self.ai = ai
        self.ao = ao
        pass
        
    def analog_input(self):
        ret = self.ai.input()
        return ret
    
    def analog_output(self, output, ch=None):
        self.ao.set_da_value(output, ch)
        self.ao.output()
        return
        
    def analog_output_stop(self):
        self.ao.stop_output()
        return
    
    def analog_sweep(self, output, sweep_ch=None):
        ret = []
        for out in output:
            self.analog_output(out, sweep_ch)
            ret.append(self.analog_input())
            continue
        return numpy.array(ret)
        
    """
    def digital_input(self):
        pass
        
    def digital_output(self):
        pass
    """
