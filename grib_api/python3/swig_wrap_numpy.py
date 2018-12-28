# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_gribapi_swig')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_gribapi_swig')
    _gribapi_swig = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gribapi_swig', [dirname(__file__)])
        except ImportError:
            import _gribapi_swig
            return _gribapi_swig
        try:
            _mod = imp.load_module('_gribapi_swig', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _gribapi_swig = swig_import_helper()
    del swig_import_helper
else:
    import _gribapi_swig
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def cdata(ptr: 'void *', nelements: 'size_t'=1) -> "SWIGCDATA":
    return _gribapi_swig.cdata(ptr, nelements)
cdata = _gribapi_swig.cdata

def memmove(data: 'void *', indata: 'void const *') -> "void":
    return _gribapi_swig.memmove(data, indata)
memmove = _gribapi_swig.memmove
GRIB_SUCCESS = _gribapi_swig.GRIB_SUCCESS
GRIB_END_OF_FILE = _gribapi_swig.GRIB_END_OF_FILE
GRIB_INTERNAL_ERROR = _gribapi_swig.GRIB_INTERNAL_ERROR
GRIB_BUFFER_TOO_SMALL = _gribapi_swig.GRIB_BUFFER_TOO_SMALL
GRIB_NOT_IMPLEMENTED = _gribapi_swig.GRIB_NOT_IMPLEMENTED
GRIB_7777_NOT_FOUND = _gribapi_swig.GRIB_7777_NOT_FOUND
GRIB_ARRAY_TOO_SMALL = _gribapi_swig.GRIB_ARRAY_TOO_SMALL
GRIB_FILE_NOT_FOUND = _gribapi_swig.GRIB_FILE_NOT_FOUND
GRIB_CODE_NOT_FOUND_IN_TABLE = _gribapi_swig.GRIB_CODE_NOT_FOUND_IN_TABLE
GRIB_WRONG_ARRAY_SIZE = _gribapi_swig.GRIB_WRONG_ARRAY_SIZE
GRIB_NOT_FOUND = _gribapi_swig.GRIB_NOT_FOUND
GRIB_IO_PROBLEM = _gribapi_swig.GRIB_IO_PROBLEM
GRIB_INVALID_MESSAGE = _gribapi_swig.GRIB_INVALID_MESSAGE
GRIB_DECODING_ERROR = _gribapi_swig.GRIB_DECODING_ERROR
GRIB_ENCODING_ERROR = _gribapi_swig.GRIB_ENCODING_ERROR
GRIB_NO_MORE_IN_SET = _gribapi_swig.GRIB_NO_MORE_IN_SET
GRIB_GEOCALCULUS_PROBLEM = _gribapi_swig.GRIB_GEOCALCULUS_PROBLEM
GRIB_OUT_OF_MEMORY = _gribapi_swig.GRIB_OUT_OF_MEMORY
GRIB_READ_ONLY = _gribapi_swig.GRIB_READ_ONLY
GRIB_INVALID_ARGUMENT = _gribapi_swig.GRIB_INVALID_ARGUMENT
GRIB_NULL_HANDLE = _gribapi_swig.GRIB_NULL_HANDLE
GRIB_INVALID_SECTION_NUMBER = _gribapi_swig.GRIB_INVALID_SECTION_NUMBER
GRIB_VALUE_CANNOT_BE_MISSING = _gribapi_swig.GRIB_VALUE_CANNOT_BE_MISSING
GRIB_WRONG_LENGTH = _gribapi_swig.GRIB_WRONG_LENGTH
GRIB_INVALID_TYPE = _gribapi_swig.GRIB_INVALID_TYPE
GRIB_WRONG_STEP = _gribapi_swig.GRIB_WRONG_STEP
GRIB_WRONG_STEP_UNIT = _gribapi_swig.GRIB_WRONG_STEP_UNIT
GRIB_INVALID_FILE = _gribapi_swig.GRIB_INVALID_FILE
GRIB_INVALID_GRIB = _gribapi_swig.GRIB_INVALID_GRIB
GRIB_INVALID_INDEX = _gribapi_swig.GRIB_INVALID_INDEX
GRIB_INVALID_ITERATOR = _gribapi_swig.GRIB_INVALID_ITERATOR
GRIB_INVALID_KEYS_ITERATOR = _gribapi_swig.GRIB_INVALID_KEYS_ITERATOR
GRIB_INVALID_NEAREST = _gribapi_swig.GRIB_INVALID_NEAREST
GRIB_INVALID_ORDERBY = _gribapi_swig.GRIB_INVALID_ORDERBY
GRIB_MISSING_KEY = _gribapi_swig.GRIB_MISSING_KEY
GRIB_OUT_OF_AREA = _gribapi_swig.GRIB_OUT_OF_AREA
GRIB_CONCEPT_NO_MATCH = _gribapi_swig.GRIB_CONCEPT_NO_MATCH
GRIB_HASH_ARRAY_NO_MATCH = _gribapi_swig.GRIB_HASH_ARRAY_NO_MATCH
GRIB_NO_DEFINITIONS = _gribapi_swig.GRIB_NO_DEFINITIONS
GRIB_WRONG_TYPE = _gribapi_swig.GRIB_WRONG_TYPE
GRIB_END = _gribapi_swig.GRIB_END
GRIB_NO_VALUES = _gribapi_swig.GRIB_NO_VALUES
GRIB_WRONG_GRID = _gribapi_swig.GRIB_WRONG_GRID
GRIB_END_OF_INDEX = _gribapi_swig.GRIB_END_OF_INDEX
GRIB_NULL_INDEX = _gribapi_swig.GRIB_NULL_INDEX
GRIB_PREMATURE_END_OF_FILE = _gribapi_swig.GRIB_PREMATURE_END_OF_FILE
GRIB_INTERNAL_ARRAY_TOO_SMALL = _gribapi_swig.GRIB_INTERNAL_ARRAY_TOO_SMALL
GRIB_MESSAGE_TOO_LARGE = _gribapi_swig.GRIB_MESSAGE_TOO_LARGE
GRIB_CONSTANT_FIELD = _gribapi_swig.GRIB_CONSTANT_FIELD
GRIB_SWITCH_NO_MATCH = _gribapi_swig.GRIB_SWITCH_NO_MATCH
GRIB_UNDERFLOW = _gribapi_swig.GRIB_UNDERFLOW
GRIB_MESSAGE_MALFORMED = _gribapi_swig.GRIB_MESSAGE_MALFORMED
GRIB_CORRUPTED_INDEX = _gribapi_swig.GRIB_CORRUPTED_INDEX
GRIB_INVALID_BPV = _gribapi_swig.GRIB_INVALID_BPV
GRIB_DIFFERENT_EDITION = _gribapi_swig.GRIB_DIFFERENT_EDITION
GRIB_VALUE_DIFFERENT = _gribapi_swig.GRIB_VALUE_DIFFERENT
GRIB_INVALID_KEY_VALUE = _gribapi_swig.GRIB_INVALID_KEY_VALUE
GRIB_STRING_TOO_SMALL = _gribapi_swig.GRIB_STRING_TOO_SMALL
GRIB_WRONG_CONVERSION = _gribapi_swig.GRIB_WRONG_CONVERSION
GRIB_MISSING_BUFR_ENTRY = _gribapi_swig.GRIB_MISSING_BUFR_ENTRY
GRIB_NULL_POINTER = _gribapi_swig.GRIB_NULL_POINTER
GRIB_ATTRIBUTE_CLASH = _gribapi_swig.GRIB_ATTRIBUTE_CLASH
GRIB_TOO_MANY_ATTRIBUTES = _gribapi_swig.GRIB_TOO_MANY_ATTRIBUTES
GRIB_ATTRIBUTE_NOT_FOUND = _gribapi_swig.GRIB_ATTRIBUTE_NOT_FOUND
GRIB_UNSUPPORTED_EDITION = _gribapi_swig.GRIB_UNSUPPORTED_EDITION
GRIB_OUT_OF_RANGE = _gribapi_swig.GRIB_OUT_OF_RANGE
GRIB_WRONG_BITMAP_SIZE = _gribapi_swig.GRIB_WRONG_BITMAP_SIZE
class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _gribapi_swig.new_intp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gribapi_swig.delete_intp
    __del__ = lambda self: None

    def assign(self, value: 'int') -> "void":
        return _gribapi_swig.intp_assign(self, value)

    def value(self) -> "int":
        return _gribapi_swig.intp_value(self)

    def cast(self) -> "int *":
        return _gribapi_swig.intp_cast(self)
    if _newclass:
        frompointer = staticmethod(_gribapi_swig.intp_frompointer)
    else:
        frompointer = _gribapi_swig.intp_frompointer
intp_swigregister = _gribapi_swig.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(t: 'int *') -> "intp *":
    return _gribapi_swig.intp_frompointer(t)
intp_frompointer = _gribapi_swig.intp_frompointer

class sizetp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sizetp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sizetp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _gribapi_swig.new_sizetp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gribapi_swig.delete_sizetp
    __del__ = lambda self: None

    def assign(self, value: 'size_t') -> "void":
        return _gribapi_swig.sizetp_assign(self, value)

    def value(self) -> "size_t":
        return _gribapi_swig.sizetp_value(self)

    def cast(self) -> "size_t *":
        return _gribapi_swig.sizetp_cast(self)
    if _newclass:
        frompointer = staticmethod(_gribapi_swig.sizetp_frompointer)
    else:
        frompointer = _gribapi_swig.sizetp_frompointer
sizetp_swigregister = _gribapi_swig.sizetp_swigregister
sizetp_swigregister(sizetp)

def sizetp_frompointer(t: 'size_t *') -> "sizetp *":
    return _gribapi_swig.sizetp_frompointer(t)
sizetp_frompointer = _gribapi_swig.sizetp_frompointer

class longp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, longp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, longp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _gribapi_swig.new_longp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gribapi_swig.delete_longp
    __del__ = lambda self: None

    def assign(self, value: 'long') -> "void":
        return _gribapi_swig.longp_assign(self, value)

    def value(self) -> "long":
        return _gribapi_swig.longp_value(self)

    def cast(self) -> "long *":
        return _gribapi_swig.longp_cast(self)
    if _newclass:
        frompointer = staticmethod(_gribapi_swig.longp_frompointer)
    else:
        frompointer = _gribapi_swig.longp_frompointer
longp_swigregister = _gribapi_swig.longp_swigregister
longp_swigregister(longp)

def longp_frompointer(t: 'long *') -> "longp *":
    return _gribapi_swig.longp_frompointer(t)
longp_frompointer = _gribapi_swig.longp_frompointer

class doublep(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doublep, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doublep, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _gribapi_swig.new_doublep()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gribapi_swig.delete_doublep
    __del__ = lambda self: None

    def assign(self, value: 'double') -> "void":
        return _gribapi_swig.doublep_assign(self, value)

    def value(self) -> "double":
        return _gribapi_swig.doublep_value(self)

    def cast(self) -> "double *":
        return _gribapi_swig.doublep_cast(self)
    if _newclass:
        frompointer = staticmethod(_gribapi_swig.doublep_frompointer)
    else:
        frompointer = _gribapi_swig.doublep_frompointer
doublep_swigregister = _gribapi_swig.doublep_swigregister
doublep_swigregister(doublep)

def doublep_frompointer(t: 'double *') -> "doublep *":
    return _gribapi_swig.doublep_frompointer(t)
doublep_frompointer = _gribapi_swig.doublep_frompointer


def new_doubleArray(nelements: 'size_t') -> "double *":
    return _gribapi_swig.new_doubleArray(nelements)
new_doubleArray = _gribapi_swig.new_doubleArray

def delete_doubleArray(ary: 'double *') -> "void":
    return _gribapi_swig.delete_doubleArray(ary)
delete_doubleArray = _gribapi_swig.delete_doubleArray

def doubleArray_getitem(ary: 'double *', index: 'size_t') -> "double":
    return _gribapi_swig.doubleArray_getitem(ary, index)
doubleArray_getitem = _gribapi_swig.doubleArray_getitem

def doubleArray_setitem(ary: 'double *', index: 'size_t', value: 'double') -> "void":
    return _gribapi_swig.doubleArray_setitem(ary, index, value)
doubleArray_setitem = _gribapi_swig.doubleArray_setitem

def new_longArray(nelements: 'size_t') -> "long *":
    return _gribapi_swig.new_longArray(nelements)
new_longArray = _gribapi_swig.new_longArray

def delete_longArray(ary: 'long *') -> "void":
    return _gribapi_swig.delete_longArray(ary)
delete_longArray = _gribapi_swig.delete_longArray

def longArray_getitem(ary: 'long *', index: 'size_t') -> "long":
    return _gribapi_swig.longArray_getitem(ary, index)
longArray_getitem = _gribapi_swig.longArray_getitem

def longArray_setitem(ary: 'long *', index: 'size_t', value: 'long') -> "void":
    return _gribapi_swig.longArray_setitem(ary, index, value)
longArray_setitem = _gribapi_swig.longArray_setitem

def new_intArray(nelements: 'size_t') -> "int *":
    return _gribapi_swig.new_intArray(nelements)
new_intArray = _gribapi_swig.new_intArray

def delete_intArray(ary: 'int *') -> "void":
    return _gribapi_swig.delete_intArray(ary)
delete_intArray = _gribapi_swig.delete_intArray

def intArray_getitem(ary: 'int *', index: 'size_t') -> "int":
    return _gribapi_swig.intArray_getitem(ary, index)
intArray_getitem = _gribapi_swig.intArray_getitem

def intArray_setitem(ary: 'int *', index: 'size_t', value: 'int') -> "void":
    return _gribapi_swig.intArray_setitem(ary, index, value)
intArray_setitem = _gribapi_swig.intArray_setitem

def new_stringArray(nelements: 'size_t') -> "char **":
    return _gribapi_swig.new_stringArray(nelements)
new_stringArray = _gribapi_swig.new_stringArray

def delete_stringArray(ary: 'char **') -> "void":
    return _gribapi_swig.delete_stringArray(ary)
delete_stringArray = _gribapi_swig.delete_stringArray

def stringArray_getitem(ary: 'char **', index: 'size_t') -> "char *":
    return _gribapi_swig.stringArray_getitem(ary, index)
stringArray_getitem = _gribapi_swig.stringArray_getitem

def stringArray_setitem(ary: 'char **', index: 'size_t', value: 'char *') -> "void":
    return _gribapi_swig.stringArray_setitem(ary, index, value)
stringArray_setitem = _gribapi_swig.stringArray_setitem

def grib_c_new_from_file(f: 'FILE *', fd: 'int', fname: 'char *', INOUT: 'int *', headers_only: 'int') -> "int *":
    return _gribapi_swig.grib_c_new_from_file(f, fd, fname, INOUT, headers_only)
grib_c_new_from_file = _gribapi_swig.grib_c_new_from_file

def grib_c_new_any_from_file(f: 'FILE *', fd: 'int', fname: 'char *', headers_only: 'int', INOUT: 'int *') -> "int *":
    return _gribapi_swig.grib_c_new_any_from_file(f, fd, fname, headers_only, INOUT)
grib_c_new_any_from_file = _gribapi_swig.grib_c_new_any_from_file

def grib_c_new_bufr_from_file(f: 'FILE *', fd: 'int', fname: 'char *', headers_only: 'int', INOUT: 'int *') -> "int *":
    return _gribapi_swig.grib_c_new_bufr_from_file(f, fd, fname, headers_only, INOUT)
grib_c_new_bufr_from_file = _gribapi_swig.grib_c_new_bufr_from_file

def grib_c_new_gts_from_file(f: 'FILE *', headers_only: 'int', INOUT: 'int *') -> "int *":
    return _gribapi_swig.grib_c_new_gts_from_file(f, headers_only, INOUT)
grib_c_new_gts_from_file = _gribapi_swig.grib_c_new_gts_from_file

def grib_c_new_metar_from_file(f: 'FILE *', headers_only: 'int', INOUT: 'int *') -> "int *":
    return _gribapi_swig.grib_c_new_metar_from_file(f, headers_only, INOUT)
grib_c_new_metar_from_file = _gribapi_swig.grib_c_new_metar_from_file

def grib_c_iterator_new(arg1: 'int *', arg3: 'int *') -> "int *":
    return _gribapi_swig.grib_c_iterator_new(arg1, arg3)
grib_c_iterator_new = _gribapi_swig.grib_c_iterator_new

def grib_c_keys_iterator_new(INPUT: 'int *', name_space: 'char *') -> "int *":
    return _gribapi_swig.grib_c_keys_iterator_new(INPUT, name_space)
grib_c_keys_iterator_new = _gribapi_swig.grib_c_keys_iterator_new

def codes_c_bufr_keys_iterator_new(INPUT: 'int *') -> "int *":
    return _gribapi_swig.codes_c_bufr_keys_iterator_new(INPUT)
codes_c_bufr_keys_iterator_new = _gribapi_swig.codes_c_bufr_keys_iterator_new

def grib_c_grib_new_from_samples(INOUT: 'int *', name: 'char *') -> "int *":
    return _gribapi_swig.grib_c_grib_new_from_samples(INOUT, name)
grib_c_grib_new_from_samples = _gribapi_swig.grib_c_grib_new_from_samples

def grib_c_bufr_new_from_samples(INOUT: 'int *', name: 'char *') -> "int *":
    return _gribapi_swig.grib_c_bufr_new_from_samples(INOUT, name)
grib_c_bufr_new_from_samples = _gribapi_swig.grib_c_bufr_new_from_samples

def grib_c_index_new_from_file(file: 'char *', keys: 'char *') -> "int *":
    return _gribapi_swig.grib_c_index_new_from_file(file, keys)
grib_c_index_new_from_file = _gribapi_swig.grib_c_index_new_from_file

def grib_c_index_add_file(INPUT: 'int *', file: 'char *') -> "int":
    return _gribapi_swig.grib_c_index_add_file(INPUT, file)
grib_c_index_add_file = _gribapi_swig.grib_c_index_add_file

def grib_c_new_from_index(INPUT: 'int *', INOUT: 'int *') -> "int *":
    return _gribapi_swig.grib_c_new_from_index(INPUT, INOUT)
grib_c_new_from_index = _gribapi_swig.grib_c_new_from_index

def grib_c_index_write(INPUT: 'int *', file: 'char *') -> "int":
    return _gribapi_swig.grib_c_index_write(INPUT, file)
grib_c_index_write = _gribapi_swig.grib_c_index_write

def grib_c_index_read(file: 'char *') -> "int *":
    return _gribapi_swig.grib_c_index_read(file)
grib_c_index_read = _gribapi_swig.grib_c_index_read

def grib_c_new_from_message(INOUT: 'int *', binmsg: 'char *', INPUT: 'size_t *') -> "int *":
    return _gribapi_swig.grib_c_new_from_message(INOUT, binmsg, INPUT)
grib_c_new_from_message = _gribapi_swig.grib_c_new_from_message

def codes_c_close_file(fd: 'int', fname: 'char *') -> "int":
    return _gribapi_swig.codes_c_close_file(fd, fname)
codes_c_close_file = _gribapi_swig.codes_c_close_file

def grib_c_count_in_file(f: 'FILE *') -> "int *":
    return _gribapi_swig.grib_c_count_in_file(f)
grib_c_count_in_file = _gribapi_swig.grib_c_count_in_file

def grib_c_release(gid: 'int *') -> "int":
    return _gribapi_swig.grib_c_release(gid)
grib_c_release = _gribapi_swig.grib_c_release

def grib_c_write(gid: 'int *', f: 'FILE *') -> "int":
    return _gribapi_swig.grib_c_write(gid, f)
grib_c_write = _gribapi_swig.grib_c_write

def grib_c_get_size_long(gid: 'int *', key: 'char *') -> "long *":
    return _gribapi_swig.grib_c_get_size_long(gid, key)
grib_c_get_size_long = _gribapi_swig.grib_c_get_size_long

def grib_c_get_string_length(gid: 'int *', key: 'char *') -> "size_t *":
    return _gribapi_swig.grib_c_get_string_length(gid, key)
grib_c_get_string_length = _gribapi_swig.grib_c_get_string_length

def grib_c_clone(gid: 'int *', INOUT: 'int *') -> "int *":
    return _gribapi_swig.grib_c_clone(gid, INOUT)
grib_c_clone = _gribapi_swig.grib_c_clone

def grib_c_copy_namespace(gid: 'int *', name: 'char *', INPUT: 'int *') -> "int":
    return _gribapi_swig.grib_c_copy_namespace(gid, name, INPUT)
grib_c_copy_namespace = _gribapi_swig.grib_c_copy_namespace

def grib_c_get_message_size(gid: 'int *') -> "size_t *":
    return _gribapi_swig.grib_c_get_message_size(gid)
grib_c_get_message_size = _gribapi_swig.grib_c_get_message_size

def grib_c_get_message_offset(gid: 'int *') -> "size_t *":
    return _gribapi_swig.grib_c_get_message_offset(gid)
grib_c_get_message_offset = _gribapi_swig.grib_c_get_message_offset

def grib_c_get_native_type(gid: 'int *', key: 'char *') -> "int *":
    return _gribapi_swig.grib_c_get_native_type(gid, key)
grib_c_get_native_type = _gribapi_swig.grib_c_get_native_type

def grib_c_multi_new() -> "int *":
    return _gribapi_swig.grib_c_multi_new()
grib_c_multi_new = _gribapi_swig.grib_c_multi_new

def grib_c_multi_support_on() -> "int":
    return _gribapi_swig.grib_c_multi_support_on()
grib_c_multi_support_on = _gribapi_swig.grib_c_multi_support_on

def grib_c_multi_write(gid: 'int *', f: 'FILE *') -> "int":
    return _gribapi_swig.grib_c_multi_write(gid, f)
grib_c_multi_write = _gribapi_swig.grib_c_multi_write

def grib_c_multi_support_off() -> "int":
    return _gribapi_swig.grib_c_multi_support_off()
grib_c_multi_support_off = _gribapi_swig.grib_c_multi_support_off

def grib_c_multi_release(gid: 'int *') -> "int":
    return _gribapi_swig.grib_c_multi_release(gid)
grib_c_multi_release = _gribapi_swig.grib_c_multi_release

def grib_c_multi_append(arg1: 'int *', arg2: 'int *', arg3: 'int *') -> "int":
    return _gribapi_swig.grib_c_multi_append(arg1, arg2, arg3)
grib_c_multi_append = _gribapi_swig.grib_c_multi_append

def grib_c_gribex_mode_on() -> "int":
    return _gribapi_swig.grib_c_gribex_mode_on()
grib_c_gribex_mode_on = _gribapi_swig.grib_c_gribex_mode_on

def grib_c_gribex_mode_off() -> "int":
    return _gribapi_swig.grib_c_gribex_mode_off()
grib_c_gribex_mode_off = _gribapi_swig.grib_c_gribex_mode_off

def grib_c_keys_iterator_next(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_keys_iterator_next(iterid)
grib_c_keys_iterator_next = _gribapi_swig.grib_c_keys_iterator_next

def codes_c_bufr_keys_iterator_next(iterid: 'int *') -> "int":
    return _gribapi_swig.codes_c_bufr_keys_iterator_next(iterid)
codes_c_bufr_keys_iterator_next = _gribapi_swig.codes_c_bufr_keys_iterator_next

def grib_c_keys_iterator_delete(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_keys_iterator_delete(iterid)
grib_c_keys_iterator_delete = _gribapi_swig.grib_c_keys_iterator_delete

def codes_c_bufr_keys_iterator_delete(iterid: 'int *') -> "int":
    return _gribapi_swig.codes_c_bufr_keys_iterator_delete(iterid)
codes_c_bufr_keys_iterator_delete = _gribapi_swig.codes_c_bufr_keys_iterator_delete

def grib_c_skip_computed(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_skip_computed(iterid)
grib_c_skip_computed = _gribapi_swig.grib_c_skip_computed

def grib_c_skip_coded(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_skip_coded(iterid)
grib_c_skip_coded = _gribapi_swig.grib_c_skip_coded

def grib_c_skip_edition_specific(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_skip_edition_specific(iterid)
grib_c_skip_edition_specific = _gribapi_swig.grib_c_skip_edition_specific

def grib_c_skip_duplicates(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_skip_duplicates(iterid)
grib_c_skip_duplicates = _gribapi_swig.grib_c_skip_duplicates

def grib_c_skip_read_only(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_skip_read_only(iterid)
grib_c_skip_read_only = _gribapi_swig.grib_c_skip_read_only

def grib_c_skip_function(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_skip_function(iterid)
grib_c_skip_function = _gribapi_swig.grib_c_skip_function

def grib_c_keys_iterator_rewind(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_keys_iterator_rewind(iterid)
grib_c_keys_iterator_rewind = _gribapi_swig.grib_c_keys_iterator_rewind

def codes_c_bufr_keys_iterator_rewind(iterid: 'int *') -> "int":
    return _gribapi_swig.codes_c_bufr_keys_iterator_rewind(iterid)
codes_c_bufr_keys_iterator_rewind = _gribapi_swig.codes_c_bufr_keys_iterator_rewind

def grib_c_bufr_copy_data(gid: 'int *', INOUT: 'int *') -> "int *":
    return _gribapi_swig.grib_c_bufr_copy_data(gid, INOUT)
grib_c_bufr_copy_data = _gribapi_swig.grib_c_bufr_copy_data

def grib_c_keys_iterator_get_name(iterid: 'int *', len: 'int') -> "char *":
    return _gribapi_swig.grib_c_keys_iterator_get_name(iterid, len)
grib_c_keys_iterator_get_name = _gribapi_swig.grib_c_keys_iterator_get_name

def codes_c_bufr_keys_iterator_get_name(iterid: 'int *', len: 'int') -> "char *":
    return _gribapi_swig.codes_c_bufr_keys_iterator_get_name(iterid, len)
codes_c_bufr_keys_iterator_get_name = _gribapi_swig.codes_c_bufr_keys_iterator_get_name

def grib_c_index_get_size_long(iid: 'int *', key: 'char *') -> "long *":
    return _gribapi_swig.grib_c_index_get_size_long(iid, key)
grib_c_index_get_size_long = _gribapi_swig.grib_c_index_get_size_long

def grib_c_index_get_long(iid: 'int *', key: 'char *', val: 'long *', size: 'int *') -> "int":
    return _gribapi_swig.grib_c_index_get_long(iid, key, val, size)
grib_c_index_get_long = _gribapi_swig.grib_c_index_get_long

def grib_c_index_get_real8(iid: 'int *', key: 'char *', val: 'double *', size: 'int *') -> "int":
    return _gribapi_swig.grib_c_index_get_real8(iid, key, val, size)
grib_c_index_get_real8 = _gribapi_swig.grib_c_index_get_real8

def grib_c_index_get_string(iid: 'int *', key: 'char *', INPUT: 'int *', INOUT: 'int *') -> "char *, int *":
    return _gribapi_swig.grib_c_index_get_string(iid, key, INPUT, INOUT)
grib_c_index_get_string = _gribapi_swig.grib_c_index_get_string

def grib_c_index_select_long(iid: 'int *', key: 'char *', INPUT: 'long *') -> "int":
    return _gribapi_swig.grib_c_index_select_long(iid, key, INPUT)
grib_c_index_select_long = _gribapi_swig.grib_c_index_select_long

def grib_c_index_select_real8(iid: 'int *', key: 'char *', INPUT: 'double *') -> "int":
    return _gribapi_swig.grib_c_index_select_real8(iid, key, INPUT)
grib_c_index_select_real8 = _gribapi_swig.grib_c_index_select_real8

def grib_c_index_select_string(iid: 'int *', key: 'char *', val: 'char *') -> "int":
    return _gribapi_swig.grib_c_index_select_string(iid, key, val)
grib_c_index_select_string = _gribapi_swig.grib_c_index_select_string

def grib_c_index_release(iid: 'int *') -> "int":
    return _gribapi_swig.grib_c_index_release(iid)
grib_c_index_release = _gribapi_swig.grib_c_index_release

def grib_c_iterator_delete(iterid: 'int *') -> "int":
    return _gribapi_swig.grib_c_iterator_delete(iterid)
grib_c_iterator_delete = _gribapi_swig.grib_c_iterator_delete

def grib_c_iterator_next(iterid: 'int *') -> "double *, double *, double *":
    return _gribapi_swig.grib_c_iterator_next(iterid)
grib_c_iterator_next = _gribapi_swig.grib_c_iterator_next

def grib_c_get_string(gid: 'int *', key: 'char *', string_val: 'char *') -> "size_t *":
    return _gribapi_swig.grib_c_get_string(gid, key, string_val)
grib_c_get_string = _gribapi_swig.grib_c_get_string

def grib_c_get_string_array(gid: 'int *', key: 'char *', array_string_val: 'char **', size: 'size_t *') -> "int":
    return _gribapi_swig.grib_c_get_string_array(gid, key, array_string_val, size)
grib_c_get_string_array = _gribapi_swig.grib_c_get_string_array

def grib_c_set_string(gid: 'int *', key: 'char *', sval: 'char *', len2: 'int') -> "int":
    return _gribapi_swig.grib_c_set_string(gid, key, sval, len2)
grib_c_set_string = _gribapi_swig.grib_c_set_string

def grib_c_get_long(gid: 'int *', key: 'char *') -> "long *":
    return _gribapi_swig.grib_c_get_long(gid, key)
grib_c_get_long = _gribapi_swig.grib_c_get_long

def grib_c_set_long(gid: 'int *', key: 'char *', INPUT: 'long *') -> "int":
    return _gribapi_swig.grib_c_set_long(gid, key, INPUT)
grib_c_set_long = _gribapi_swig.grib_c_set_long

def grib_c_get_double(gid: 'int *', key: 'char *') -> "double *":
    return _gribapi_swig.grib_c_get_double(gid, key)
grib_c_get_double = _gribapi_swig.grib_c_get_double

def grib_c_set_double(gid: 'int *', key: 'char *', INPUT: 'double *') -> "int":
    return _gribapi_swig.grib_c_set_double(gid, key, INPUT)
grib_c_set_double = _gribapi_swig.grib_c_set_double

def grib_c_set_real8_array(gid: 'int *', key: 'char *', val: 'double *', size: 'int *') -> "int":
    return _gribapi_swig.grib_c_set_real8_array(gid, key, val, size)
grib_c_set_real8_array = _gribapi_swig.grib_c_set_real8_array

def grib_c_get_real8_array(gid: 'int *', key: 'char *', val: 'double *', size: 'int *') -> "int":
    return _gribapi_swig.grib_c_get_real8_array(gid, key, val, size)
grib_c_get_real8_array = _gribapi_swig.grib_c_get_real8_array

def grib_c_get_long_array(gid: 'int *', key: 'char *', val: 'long *', size: 'int *') -> "int":
    return _gribapi_swig.grib_c_get_long_array(gid, key, val, size)
grib_c_get_long_array = _gribapi_swig.grib_c_get_long_array

def grib_c_set_long_array(gid: 'int *', key: 'char *', val: 'long *', size: 'int *') -> "int":
    return _gribapi_swig.grib_c_set_long_array(gid, key, val, size)
grib_c_set_long_array = _gribapi_swig.grib_c_set_long_array

def grib_c_get_real8_element(gid: 'int *', key: 'char *', INPUT: 'int *') -> "double *":
    return _gribapi_swig.grib_c_get_real8_element(gid, key, INPUT)
grib_c_get_real8_element = _gribapi_swig.grib_c_get_real8_element

def grib_c_get_real8_elements(gid: 'int *', key: 'char *', index: 'int *', val: 'double *', size: 'int *') -> "int":
    return _gribapi_swig.grib_c_get_real8_elements(gid, key, index, val, size)
grib_c_get_real8_elements = _gribapi_swig.grib_c_get_real8_elements

def grib_c_set_missing(gid: 'int *', key: 'char *') -> "int":
    return _gribapi_swig.grib_c_set_missing(gid, key)
grib_c_set_missing = _gribapi_swig.grib_c_set_missing

def grib_c_set_key_vals(gid: 'int *', keyvals: 'char *') -> "int":
    return _gribapi_swig.grib_c_set_key_vals(gid, keyvals)
grib_c_set_key_vals = _gribapi_swig.grib_c_set_key_vals

def grib_c_is_missing(gid: 'int *', key: 'char *') -> "int *":
    return _gribapi_swig.grib_c_is_missing(gid, key)
grib_c_is_missing = _gribapi_swig.grib_c_is_missing

def grib_c_is_defined(gid: 'int *', key: 'char *') -> "int *":
    return _gribapi_swig.grib_c_is_defined(gid, key)
grib_c_is_defined = _gribapi_swig.grib_c_is_defined

def grib_c_set_string_array(gid: 'int *', key: 'char *', val: 'char const **') -> "int":
    return _gribapi_swig.grib_c_set_string_array(gid, key, val)
grib_c_set_string_array = _gribapi_swig.grib_c_set_string_array

def grib_set_double_ndarray(gid: 'int *', key: 'char *', dpin_val: 'double *') -> "int":
    return _gribapi_swig.grib_set_double_ndarray(gid, key, dpin_val)
grib_set_double_ndarray = _gribapi_swig.grib_set_double_ndarray

def grib_set_long_ndarray(gid: 'int *', key: 'char *', lpin_val: 'long *') -> "int":
    return _gribapi_swig.grib_set_long_ndarray(gid, key, lpin_val)
grib_set_long_ndarray = _gribapi_swig.grib_set_long_ndarray

def grib_get_double_ndarray(gid: 'int *', key: 'char *', dpout_val: 'double *') -> "int":
    return _gribapi_swig.grib_get_double_ndarray(gid, key, dpout_val)
grib_get_double_ndarray = _gribapi_swig.grib_get_double_ndarray

def grib_get_long_ndarray(gid: 'int *', key: 'char *', lpout_val: 'long *') -> "int":
    return _gribapi_swig.grib_get_long_ndarray(gid, key, lpout_val)
grib_get_long_ndarray = _gribapi_swig.grib_get_long_ndarray

def grib_get_double_ndelements(gid: 'int *', key: 'char *', ipin_index: 'int *', dpout_val: 'double *') -> "int":
    return _gribapi_swig.grib_get_double_ndelements(gid, key, ipin_index, dpout_val)
grib_get_double_ndelements = _gribapi_swig.grib_get_double_ndelements

def grib_c_find_nearest_single(gid: 'int *', arg2: 'int *', arg3: 'double *', arg4: 'double *') -> "double *, double *, double *, double *, int *":
    return _gribapi_swig.grib_c_find_nearest_single(gid, arg2, arg3, arg4)
grib_c_find_nearest_single = _gribapi_swig.grib_c_find_nearest_single

def grib_c_find_nearest_four_single(gid: 'int *', arg2: 'int *', arg3: 'double *', arg4: 'double *', outlats: 'double *', outlons: 'double *', values: 'double *', distances: 'double *', indexes: 'int *') -> "int":
    return _gribapi_swig.grib_c_find_nearest_four_single(gid, arg2, arg3, arg4, outlats, outlons, values, distances, indexes)
grib_c_find_nearest_four_single = _gribapi_swig.grib_c_find_nearest_four_single

def grib_c_get_message(gid: 'int *') -> "size_t *":
    return _gribapi_swig.grib_c_get_message(gid)
grib_c_get_message = _gribapi_swig.grib_c_get_message

def grib_c_get_error_string(INPUT: 'int *', len: 'int') -> "char *":
    return _gribapi_swig.grib_c_get_error_string(INPUT, len)
grib_c_get_error_string = _gribapi_swig.grib_c_get_error_string

def no_fail_on_wrong_length(flag: 'int') -> "void":
    return _gribapi_swig.no_fail_on_wrong_length(flag)
no_fail_on_wrong_length = _gribapi_swig.no_fail_on_wrong_length

def grib_c_get_api_version() -> "long":
    return _gribapi_swig.grib_c_get_api_version()
grib_c_get_api_version = _gribapi_swig.grib_c_get_api_version

def grib_c_gts_header_on() -> "void":
    return _gribapi_swig.grib_c_gts_header_on()
grib_c_gts_header_on = _gribapi_swig.grib_c_gts_header_on

def grib_c_gts_header_off() -> "void":
    return _gribapi_swig.grib_c_gts_header_off()
grib_c_gts_header_off = _gribapi_swig.grib_c_gts_header_off

def grib_c_set_definitions_path(path: 'char const *') -> "void":
    return _gribapi_swig.grib_c_set_definitions_path(path)
grib_c_set_definitions_path = _gribapi_swig.grib_c_set_definitions_path

def grib_c_set_samples_path(path: 'char const *') -> "void":
    return _gribapi_swig.grib_c_set_samples_path(path)
grib_c_set_samples_path = _gribapi_swig.grib_c_set_samples_path
# This file is compatible with both classic and new-style classes.


