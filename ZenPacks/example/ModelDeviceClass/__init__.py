from Products.ZenUtils.Utils import monkeypatch


@monkeypatch('Products.ZenModel.Device.Device')
def setDeviceClassName(self, name):
    '''
    Move device to device class specified by name.
    '''
    if self.getDeviceClassName() != name:
        self.changeDeviceClass(name)
