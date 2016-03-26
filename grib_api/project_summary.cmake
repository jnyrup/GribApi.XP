if( SWIG_FOUND )
  message( STATUS " SWIG command      : [${SWIG_EXECUTABLE}]" )
endif()

foreach( _tpl ${GRIB_API_TPLS} )
    string( TOUPPER ${_tpl} TPL )
    if( ${TPL}_FOUND )
        message( STATUS " ${_tpl} ${${_tpl}_VERSION}" )
        if( ${TPL}_INCLUDE_DIRS )
          message( STATUS "      includes : [${${TPL}_INCLUDE_DIRS}]" )
        endif()
        if( ${TPL}_LIBRARIES )
          message( STATUS "      libs     : [${${TPL}_LIBRARIES}]" )
        endif()
        if( ${TPL}_DEFINITIONS )
          message( STATUS "      defs     : [${${TPL}_DEFINITIONS}]" )
        endif()
    endif()
endforeach()
