import execjs

ctx = execjs.compile(r"""
function hash(_0x3394b8) {
    var _0x144b89 = {};
    var _0x30678a = _0x144b89;
    var _0xe1fd73 = 0x8;
    var _0x556503 = 0x0;
    function _0x5d9571(_0x1d08f9, _0x4e7e95) {
        var _0x132aed = (_0x1d08f9 & 0xffff) + (_0x4e7e95 & 0xffff);
        var _0x3e4e4b = ((_0x1d08f9 >> 0x10) + (_0x4e7e95 >> 0x10)) +(_0x132aed >> 0x10);
        return _0x3e4e4b << 0x10 | _0x132aed & 0xffff;
    }
    function _0x4a4fe8(_0x98d0ee, _0x40bf34) {
        return (_0x98d0ee >>> _0x40bf34) | (_0x98d0ee << (0x20 - _0x40bf34));
    }
    function _0x4d427f(_0x34bdbf, _0x4821ba, _0x1612f5) {
        return (_0x34bdbf & _0x4821ba) ^ ((~_0x34bdbf) & _0x1612f5);
    }
    function _0x1a6f48(_0x5a96ed, _0x11fadc, _0x4c3a79) {
        return _0x5a96ed & _0x11fadc ^ _0x5a96ed & _0x4c3a79 ^ _0x11fadc & _0x4c3a79;
    }
    function _0x562759(_0x169f4c) {
        return _0x4a4fe8(_0x169f4c, 0x2) ^ _0x4a4fe8(_0x169f4c, 0xd) ^ _0x4a4fe8(_0x169f4c, 0x16);
    }
    function _0x33c6da(_0x316e57) {
        return _0x4a4fe8(_0x316e57, 0x6) ^ _0x4a4fe8(_0x316e57, 0xb) ^ _0x4a4fe8(_0x316e57, 0x19);
    }
    function _0x3654cd(_0x1e3ddd) {
        return _0x4a4fe8(_0x1e3ddd, 0x7) ^ _0x4a4fe8(_0x1e3ddd, 0x12) ^ (_0x1e3ddd >>> 0x3);
    }
    function _0xb52e31(_0x213644) {
        return _0x4a4fe8(_0x213644, 0x11) ^ _0x4a4fe8(_0x213644, 0x13) ^ (_0x213644 >>> 0xa);
    }
    function _0x458117(_0x36ecac, _0x58331a) {
        if ('NDNKC' === 'NDNKC') {
            var _0x3447ef = ('7|3|2|6|0|8|5|4|1')['split']('|');
            var _0x3676e3 = 0x0;
            while (!![]) {
                switch (_0x3447ef[_0x3676e3++]) {
                case '0':
                    var _0x10c297, _0x154b53;
                    continue;
                case '1':
                    return _0x4152a1;
                case '2':
                    var _0xce2673 = new Array(0x40);
                    continue;
                case '3':
                    var _0x4152a1 = new Array(0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19);
                    continue;
                case '4':
                    for (var _0x55f6a5 = 0x0; _0x55f6a5 < _0x36ecac['length']; _0x55f6a5 += 0x10) {
                        var _0x2e0c65 = ('16|1|5|6|3|8|7|12|0|4|9|11|13|2|15|10|14')['split']('|');
                        var _0x42de3e = 0x0;
                        while (!![]) {
                            switch (_0x2e0c65[_0x42de3e++]) {
                            case '0':
                                for (var _0x1215e8 = 0x0; _0x1215e8 < 0x40; _0x1215e8++) {
                                    if ((_0x1215e8 < 0x10))
                                        _0xce2673[_0x1215e8] = _0x36ecac[(_0x1215e8 + _0x55f6a5)];
                                    else
                                        _0xce2673[_0x1215e8] = _0x5d9571(_0x5d9571(_0x5d9571(_0xb52e31(_0xce2673[_0x1215e8 - 0x2]), _0xce2673[_0x1215e8 - 0x7]), _0x3654cd(_0xce2673[_0x1215e8 - 0xf])), _0xce2673[_0x1215e8 - 0x10]);
                                    _0x10c297 = _0x5d9571(_0x5d9571(_0x5d9571(_0x5d9571(_0x3e866d, _0x33c6da(_0x432592)), _0x4d427f(_0x432592, _0x29b3ff, _0x5428e8)), _0x531cb3[_0x1215e8]), _0xce2673[_0x1215e8]);
                                    _0x154b53 = _0x5d9571(_0x562759(_0x1de767), _0x1a6f48(_0x1de767, _0x2f0e71, _0x251857));
                                    _0x3e866d = _0x5428e8;
                                    _0x5428e8 = _0x29b3ff;
                                    _0x29b3ff = _0x432592;
                                    _0x432592 = _0x5d9571(_0x47a1bd, _0x10c297);
                                    _0x47a1bd = _0x251857;
                                    _0x251857 = _0x2f0e71;
                                    _0x2f0e71 = _0x1de767;
                                    _0x1de767 = _0x5d9571(_0x10c297, _0x154b53);
                                }
                                continue;
                            case '1':
                                _0x2f0e71 = _0x4152a1[0x1];
                                continue;
                            case '2':
                                _0x4152a1[0x4] = _0x5d9571(_0x432592, _0x4152a1[0x4]);
                                continue;
                            case '3':
                                _0x432592 = _0x4152a1[0x4];
                                continue;
                            case '4':
                                _0x4152a1[0x0] = _0x5d9571(_0x1de767, _0x4152a1[0x0]);
                                continue;
                            case '5':
                                _0x251857 = _0x4152a1[0x2];
                                continue;
                            case '6':
                                _0x47a1bd = _0x4152a1[0x3];
                                continue;
                            case '7':
                                _0x5428e8 = _0x4152a1[0x6];
                                continue;
                            case '8':
                                _0x29b3ff = _0x4152a1[0x5];
                                continue;
                            case '9':
                                _0x4152a1[0x1] = _0x5d9571(_0x2f0e71, _0x4152a1[0x1]);
                                continue;
                            case '10':
                                _0x4152a1[0x6] = _0x5d9571(_0x5428e8, _0x4152a1[0x6]);
                                continue;
                            case '11':
                                _0x4152a1[0x2] = _0x5d9571(_0x251857, _0x4152a1[0x2]);
                                continue;
                            case '12':
                                _0x3e866d = _0x4152a1[0x7];
                                continue;
                            case '13':
                                _0x4152a1[0x3] = _0x5d9571(_0x47a1bd, _0x4152a1[0x3]);
                                continue;
                            case '14':
                                _0x4152a1[0x7] = _0x5d9571(_0x3e866d, _0x4152a1[0x7]);
                                continue;
                            case '15':
                                _0x4152a1[0x5] = _0x5d9571(_0x29b3ff, _0x4152a1[0x5]);
                                continue;
                            case '16':
                                _0x1de767 = _0x4152a1[0x0];
                                continue;
                            }
                            break;
                        }
                    }
                    continue;
                case '5':
                    _0x36ecac[((_0x58331a + 0x40 >> 0x9) << 0x4) + 0xf] = _0x58331a;
                    continue;
                case '6':
                    var _0x1de767, _0x2f0e71, _0x251857, _0x47a1bd, _0x432592, _0x29b3ff, _0x5428e8, _0x3e866d, _0x55f6a5, _0x1215e8;
                    continue;
                case '7':
                    var _0x531cb3 = new Array(0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0xfc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x6ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2);
                    continue;
                case '8':
                    _0x36ecac[_0x58331a >> 0x5] |= 0x80 << 0x18 - _0x58331a % 0x20;
                    continue;
                }
                break;
            }
        } else {
            document['cookie'] = ((data['tn'] + '=' + ret[0x0] + ';Max-age=' + data['vt']) + '; pa' + 'th =\x20/');
            location['href'] = (location['pathname'] + location['search']);
        }
    }
    function _0x2af9a5(_0x27d189) {
        var _0x5941b1 = Array();
        var _0x34fba7 = ((0x1 << _0xe1fd73) -  0x1);
        for (var _0x2655dc = 0x0; _0x2655dc < (_0x27d189['length'] * _0xe1fd73); _0x2655dc += _0xe1fd73) {
            _0x5941b1[_0x2655dc >> 0x5] |= (_0x27d189['charCodeAt']((_0x2655dc / _0xe1fd73)) & _0x34fba7) << ((0x18 - (_0x2655dc % 0x20)));
        }
        return _0x5941b1;
    }
    // function _0xba3635(_0x517e83) {
    //     var _0x2da76b = new RegExp('\x0a','g');
    //     _0x517e83 = _0x517e83['replace'](_0x2da76b, '\x0a');
    //     var _0x2f6bf8 = '';
    //     for (var _0x4b32fe = 0x0; _0x4b32fe < _0x517e83['length']; _0x4b32fe++) {
    //         var _0x5d4df9 = _0x517e83['charCodeAt'](_0x4b32fe);
    //         if (_0x5d4df9 < 0x80) {
    //             _0x2f6bf8 += String['fromCharCode'](_0x5d4df9);
    //         } else if ((_0x5d4df9 > 0x7f) && (_0x5d4df9 < 0x800)) {
    //             _0x2f6bf8 += String['fromCharCode'](_0x5d4df9 >> 0x6 | 0xc0);
    //             _0x2f6bf8 += String['fromCharCode'](_0x5d4df9 & 0x3f | 0x80);
    //         } else {
    //             _0x2f6bf8 += String['fromCharCode']((_0x5d4df9 >> 0xc) | 0xe0);
    //             _0x2f6bf8 += String['fromCharCode']((_0x5d4df9 >> 0x6) & 0x3f | 0x80);
    //             _0x2f6bf8 += String['fromCharCode']((_0x5d4df9 & 0x3f) | 0x80);
    //         }
    //     }
    //     return _0x2f6bf8;
    // }
    function _0x3ebf08(_0x5dce8b) {
        var _0x51d7fd = _0x556503 ? '0123456789ABCDEF' : '0123456789abcdef';
        var _0x53c13b = '';
        for (var _0x40830d = 0x0; _0x40830d < (_0x5dce8b['length'] * 0x4); _0x40830d++) {
            _0x53c13b += _0x51d7fd['charAt'](((_0x5dce8b[(_0x40830d >> 0x2)] >> ((0x3 - _0x40830d % 0x4) * 0x8 + 0x4)) & 0xf)) + _0x51d7fd['charAt']((_0x5dce8b[_0x40830d >> 0x2] >> ((0x3 - (_0x40830d % 0x4)) * 0x8)) & 0xf);
        }
        return _0x53c13b;
    }
    // _0x3394b8 = _0xba3635(_0x3394b8);
    return _0x3ebf08(_0x458117(_0x2af9a5(_0x3394b8), _0x3394b8['length'] * 8));
}""")


def gethash(abc):
    tt = ctx.call("hash", abc)
    # print(tt)
    return tt
