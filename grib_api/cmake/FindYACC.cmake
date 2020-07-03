# - Find yacc executable and provides macros to generate custom build rules
# The module defines the following variables:
#
#  YACC_EXECUTABLE - path to the yacc program
#  YACC_FOUND - true if the program was found
#
# The minimum required version of yacc can be specified using the
# standard CMake syntax, e.g. find_package(YACC 2.1.3)
#
# If yacc is found, the module defines the macros:
#  YACC_TARGET(<Name> <YaccInput> <CodeOutput> [VERBOSE <file>]
#              [COMPILE_FLAGS <string>])
# which will create  a custom rule to generate  a parser. <YaccInput> is
# the path to  a yacc file. <CodeOutput> is the name  of the source file
# generated by yacc.  A header file is also  be generated, and contains
# the  token  list.  If  COMPILE_FLAGS  option is  specified,  the  next
# parameter is  added in the yacc  command line.  if  VERBOSE option is
# specified, <file> is created  and contains verbose descriptions of the
# grammar and parser. The macro defines a set of variables:
#  YACC_${Name}_DEFINED - true is the macro ran successfully
#  YACC_${Name}_INPUT - The input source file, an alias for <YaccInput>
#  YACC_${Name}_OUTPUT_SOURCE - The source file generated by yacc
#  YACC_${Name}_OUTPUT_HEADER - The header file generated by yacc
#  YACC_${Name}_OUTPUTS - The sources files generated by yacc
#  YACC_${Name}_COMPILE_FLAGS - Options used in the yacc command line
#
#  ====================================================================

#=============================================================================
# Copyright 2009 Kitware, Inc.
# Copyright 2006 Tristan Carel
#
# Distributed under the OSI-approved BSD License (the "License");
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================

# This file is based on the FindFLEX CMake macro, and adapted by ECMWF

#=============================================================================
# (C) Copyright 2011- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.

FIND_PROGRAM(YACC_EXECUTABLE yacc DOC "path to the yacc/yacc executable")
MARK_AS_ADVANCED(YACC_EXECUTABLE)

IF(YACC_EXECUTABLE)
  # the yacc commands should be executed with the C locale, otherwise
  # the message (which are parsed) may be translated
  SET(_Yacc_SAVED_LC_ALL "$ENV{LC_ALL}")
  SET(ENV{LC_ALL} C)

  SET(ENV{LC_ALL} ${_Yacc_SAVED_LC_ALL})

  # internal macro
  MACRO(YACC_TARGET_option_verbose Name YaccOutput filename)
    LIST(APPEND YACC_TARGET_cmdopt "--verbose")
    GET_FILENAME_COMPONENT(YACC_TARGET_output_path "${YaccOutput}" PATH)
    GET_FILENAME_COMPONENT(YACC_TARGET_output_name "${YaccOutput}" NAME_WE)
    ADD_CUSTOM_COMMAND(OUTPUT ${filename}
      COMMAND ${CMAKE_COMMAND}
      ARGS -E copy
      "${YACC_TARGET_output_path}/${YACC_TARGET_output_name}.output"
      "${filename}"
      DEPENDS
      "${YACC_TARGET_output_path}/${YACC_TARGET_output_name}.output"
      COMMENT "[YACC][${Name}] Copying yacc verbose table to ${filename}"
      WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
    SET(YACC_${Name}_VERBOSE_FILE ${filename})
    LIST(APPEND YACC_TARGET_extraoutputs
      "${YACC_TARGET_output_path}/${YACC_TARGET_output_name}.output")
  ENDMACRO(YACC_TARGET_option_verbose)

  # internal macro
  MACRO(YACC_TARGET_option_extraopts Options)
    SET(YACC_TARGET_extraopts "${Options}")
    SEPARATE_ARGUMENTS(YACC_TARGET_extraopts)
    LIST(APPEND YACC_TARGET_cmdopt ${YACC_TARGET_extraopts})
  ENDMACRO(YACC_TARGET_option_extraopts)

  #============================================================
  # YACC_TARGET (public macro)
  #============================================================
  #
  MACRO(YACC_TARGET Name YaccInput YaccOutput)
    SET(YACC_TARGET_output_header "")
    SET(YACC_TARGET_cmdopt "")
    SET(YACC_TARGET_outputs "${YaccOutput}")
    IF(NOT ${ARGC} EQUAL 3 AND NOT ${ARGC} EQUAL 5 AND NOT ${ARGC} EQUAL 7)
      MESSAGE(SEND_ERROR "Usage")
    ELSE()
      # Parsing parameters
      IF(${ARGC} GREATER 5 OR ${ARGC} EQUAL 5)
        IF("${ARGV3}" STREQUAL "VERBOSE")
          YACC_TARGET_option_verbose(${Name} ${YaccOutput} "${ARGV4}")
        ENDIF()
        IF("${ARGV3}" STREQUAL "COMPILE_FLAGS")
          YACC_TARGET_option_extraopts("${ARGV4}")
        ENDIF()
      ENDIF()

      IF(${ARGC} EQUAL 7)
        IF("${ARGV5}" STREQUAL "VERBOSE")
          YACC_TARGET_option_verbose(${Name} ${YaccOutput} "${ARGV6}")
        ENDIF()

        IF("${ARGV5}" STREQUAL "COMPILE_FLAGS")
          YACC_TARGET_option_extraopts("${ARGV6}")
        ENDIF()
      ENDIF()

      # Header's name generated by yacc (see option -d)
      LIST(APPEND YACC_TARGET_cmdopt "-d")
      STRING(REGEX REPLACE "^(.*)(\\.[^.]*)$" "\\2" _fileext "${ARGV2}")
      STRING(REPLACE "c" "h" _fileext ${_fileext})
      STRING(REGEX REPLACE "^(.*)(\\.[^.]*)$" "\\1${_fileext}"
          YACC_${Name}_OUTPUT_HEADER "${ARGV2}")
      LIST(APPEND YACC_TARGET_outputs "${YACC_${Name}_OUTPUT_HEADER}")

#       message ( STATUS "${YACC_EXECUTABLE} ${YACC_TARGET_cmdopt} ${CMAKE_CURRENT_BINARY_DIR}/${ARGV1}" )
#       message ( STATUS "${CMAKE_COMMAND} -E rename ${CMAKE_CURRENT_BINARY_DIR}/y.tab.h ${YACC_${Name}_OUTPUT_HEADER}" )
#       message ( STATUS "${CMAKE_COMMAND} -E rename ${CMAKE_CURRENT_BINARY_DIR}/y.tab.c ${ARGV2}" )

      ADD_CUSTOM_COMMAND(OUTPUT ${YACC_TARGET_outputs} ${YACC_TARGET_extraoutputs}
        COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_CURRENT_SOURCE_DIR}/${ARGV1} ${CMAKE_CURRENT_BINARY_DIR}
        COMMAND ${YACC_EXECUTABLE} ${YACC_TARGET_cmdopt} ${CMAKE_CURRENT_BINARY_DIR}/${ARGV1}
        COMMAND ${CMAKE_COMMAND} -E rename ${CMAKE_CURRENT_BINARY_DIR}/y.tab.h ${YACC_${Name}_OUTPUT_HEADER}
        COMMAND ${CMAKE_COMMAND} -E rename ${CMAKE_CURRENT_BINARY_DIR}/y.tab.c ${ARGV2}
        DEPENDS ${ARGV1}
        COMMENT "[YACC][${Name}] Building parser with yacc"
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

      # define target variables
      SET(YACC_${Name}_DEFINED TRUE)
      SET(YACC_${Name}_INPUT ${ARGV1})
      SET(YACC_${Name}_OUTPUTS ${YACC_TARGET_outputs})
      SET(YACC_${Name}_COMPILE_FLAGS ${YACC_TARGET_cmdopt})
      SET(YACC_${Name}_OUTPUT_SOURCE "${YaccOutput}")

    ENDIF(NOT ${ARGC} EQUAL 3 AND NOT ${ARGC} EQUAL 5 AND NOT ${ARGC} EQUAL 7)
  ENDMACRO(YACC_TARGET)
  #
  #============================================================

ENDIF(YACC_EXECUTABLE)

FIND_PACKAGE_HANDLE_STANDARD_ARGS(YACC REQUIRED_VARS  YACC_EXECUTABLE )

# FindYACC.cmake ends here
