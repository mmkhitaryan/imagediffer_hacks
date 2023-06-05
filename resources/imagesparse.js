(function() {
    var _index = 0;
    var _images = [];
    var binaryString = "";
    var _iterator14 = _createForOfIteratorHelper(response), _step14;
    try {
        for (_iterator14.s(); !(_step14 = _iterator14.n()).done; ) {
            var byte = _step14.value;
            binaryString += String.fromCharCode(byte)
        }
    } catch (err) {
        _iterator14.e(err)
    } finally {
        _iterator14.f()
    }
    var _loop2 = function _loop2() {
        var index = binaryString.indexOf("\r\n");
        var sizeHex = binaryString.substr(0, index);
        var size = parseInt(sizeHex, 16);
        var content = binaryString.substr(index + 2, size);
        var image = new Image;
        var _imageIndex = _index;
        image.onerror = function() {
            image.onerror = null;
            if (!hasErrorOccured) {
                hasErrorOccured = true;
                reject("Invalid response data")
            }
        }
        ;
        image.onload = function() {
            image.onload = null;
            if (!hasErrorOccured) {
                _images[_imageIndex].width = image.width;
                _images[_imageIndex].height = image.height;
                _images[_imageIndex].loaded = true;
                var _iterator15 = _createForOfIteratorHelper(_images), _step15;
                try {
                    for (_iterator15.s(); !(_step15 = _iterator15.n()).done; ) {
                        var _image = _step15.value;
                        if (!_image.loaded) {
                            return
                        }
                    }
                } catch (err) {
                    _iterator15.e(err)
                } finally {
                    _iterator15.f()
                }
                images.push.apply(images, _images);
                resolve()
            }
        }
        ;
        image.src = "data:image/jpeg;base64,".concat(btoa(content));
        _images[_imageIndex] = {
            image: image,
            width: 0,
            height: 0,
            loaded: false
        };
        binaryString = binaryString.substr(index + 2 + size);
        _index++
    };
    while (binaryString.length && _index < count) {
        _loop2()
    }
}
)()