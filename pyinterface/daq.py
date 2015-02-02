
import numpy

class daq(object):
    _series_data = []
    _series_data_num = 0
    _series_count = 0
    
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
    
    def analog_series_set(self, data):
        self._series_data = data
        self._series_data_num = len(data)
        self._series_count = 0
        return
        
    def analog_series_output_next(self):
        print(self._series_count)
        outp = self._series_data[self._series_count]
        self.analog_output(outp)
        next_count = self._series_count + 1
        if next_count >= self._series_data_num:
            next_count = 0
            pass
        self._series_count = next_count
        return
        
    """
    def digital_input(self):
        pass
        
    def digital_output(self):
        pass
    """
