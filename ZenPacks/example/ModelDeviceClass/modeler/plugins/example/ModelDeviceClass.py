'''
An example plugin that illustrates how to move a device to a different device
class through modeling.
'''

# This example requires the monkeypatched Device.setDeviceClassName method in
# this ZenPack's __init__.py.

from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin


class ModelDeviceClass(PythonPlugin):
    def collect(self, device, log):
        return True

    def process(self, device, results, log):
        return self.objectMap({
            'setDeviceClassName': '/Discovered',
            })
