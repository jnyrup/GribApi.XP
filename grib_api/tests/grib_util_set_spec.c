/*
 * Copyright 2005-2017 ECMWF.
 *
 * This software is licensed under the terms of the Apache Licence Version 2.0
 * which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
 *
 * In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
 * virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.
 */

#include "grib_api_internal.h"
#include "eccodes.h"
#include <assert.h>

#define STR_EQUAL(s1, s2) (strcmp((s1), (s2)) == 0)

int get_packing_type_code(const char* packingType)
{
    int result = GRIB_UTIL_PACKING_TYPE_GRID_SIMPLE;
    if (packingType==NULL)
        return result;

    if (STR_EQUAL(packingType, "grid_jpeg"))
        result = GRIB_UTIL_PACKING_TYPE_JPEG;
    else if (STR_EQUAL(packingType, "grid_simple"))
        result = GRIB_UTIL_PACKING_TYPE_GRID_SIMPLE;
    else if (STR_EQUAL(packingType, "grid_second_order"))
        result = GRIB_UTIL_PACKING_TYPE_GRID_SECOND_ORDER;

    return result;
}

void test_reduced_gg(int remove_local_def, int edition, const char* packingType,
                     const char* input_filename, const char* output_filename)
{
    /* based on copy_spec_from_ksec */
    int err = 0;
    size_t slen = 32, inlen = 0, outlen = 0;
    size_t i=0, size=0;
    int set_spec_flags=0;
    double* values = NULL;
    FILE* in = NULL;
    FILE* out = NULL;
    const void* buffer = NULL;
    char gridType[128] = {0,};

    codes_handle *handle = 0;
    codes_handle *finalh = 0;
    grib_util_grid_spec spec={0,};
    grib_util_packing_spec packing_spec={0,};

    in = fopen(input_filename,"r");     assert(in);
    handle = grib_handle_new_from_file(0,in,&err);    assert(handle);

    CODES_CHECK(grib_get_string(handle, "gridType", gridType, &slen),0);
    if (!STR_EQUAL(gridType, "reduced_gg")) {
        grib_handle_delete(handle);
        return;
    }
    out = fopen(output_filename,"w");   assert(out);

    CODES_CHECK(grib_get_size(handle,"values",&inlen), 0);
    values = (double*)malloc(sizeof(double)*inlen);
    CODES_CHECK(grib_get_double_array(handle, "values", values,&inlen), 0);
    for(i=0; i<inlen; ++i) {
        values[i] *= 1.10;
    }

    spec.grid_type = GRIB_UTIL_GRID_SPEC_REDUCED_GG;
    spec.N = 32;   /* hardcoded for now */
    spec.Nj = 2 * spec.N;
    outlen = inlen;
    spec.iDirectionIncrementInDegrees = 1.5;
    spec.jDirectionIncrementInDegrees = 1.5;
    spec.latitudeOfFirstGridPointInDegrees  = 87.863799;
    spec.longitudeOfFirstGridPointInDegrees = 0.0;
    spec.latitudeOfLastGridPointInDegrees   = -spec.latitudeOfFirstGridPointInDegrees;
    spec.longitudeOfLastGridPointInDegrees  = 357.187500;
    spec.bitmapPresent = 0;

    /*packing_spec.packing_type = GRIB_UTIL_PACKING_TYPE_GRID_SECOND_ORDER;*/
    packing_spec.packing_type = get_packing_type_code(packingType);
    packing_spec.bitsPerValue = 24;
    packing_spec.accuracy=GRIB_UTIL_ACCURACY_USE_PROVIDED_BITS_PER_VALUES;
    packing_spec.packing=GRIB_UTIL_PACKING_USE_PROVIDED;

    finalh = grib_util_set_spec(
            handle,
            &spec,
            &packing_spec,
            set_spec_flags,
            values,
            outlen,
            &err);
    assert(finalh);
    assert(err == 0);

    /* Write out the message to the output file */
    CODES_CHECK(grib_get_message(finalh, &buffer, &size),0);
    if(fwrite(buffer,1,size,out) != size) {
        assert(0);
    }
    grib_handle_delete(handle);
    grib_handle_delete(finalh);
    fclose(in);
    fclose(out);
}

void test_regular_ll(int remove_local_def, int edition, const char* packingType,
                     const char* input_filename, const char* output_filename)
{
    /* based on copy_spec_from_ksec */
    int err = 0;
    size_t slen = 32, inlen = 0, outlen = 0;
    size_t size=0;
    int set_spec_flags=0;
    double* values = NULL;
    FILE* in = NULL;
    FILE* out = NULL;
    const void* buffer = NULL;
    char gridType[128] = {0,};

    codes_handle *handle = 0;
    codes_handle *finalh = 0;
    grib_util_grid_spec spec={0,};
    grib_util_packing_spec packing_spec={0,};

    in = fopen(input_filename,"r");     assert(in);
    handle = codes_handle_new_from_file(0, in, PRODUCT_GRIB, &err);    assert(handle);

    CODES_CHECK(grib_get_string(handle, "gridType", gridType, &slen),0);
    if (!STR_EQUAL(gridType, "regular_ll")) {
        grib_handle_delete(handle);
        return;
    }
    out = fopen(output_filename,"w");   assert(out);

    CODES_CHECK(codes_get_size(handle,"values",&inlen), 0);
    values = (double*)malloc(sizeof(double)*inlen);
    CODES_CHECK(codes_get_double_array(handle, "values", values,&inlen), 0);

    spec.grid_type = GRIB_UTIL_GRID_SPEC_REGULAR_LL;
    spec.Nj = 14;
    spec.Ni = 17;
    outlen = spec.Nj * spec.Ni;
    spec.iDirectionIncrementInDegrees = 1.5;
    spec.jDirectionIncrementInDegrees = 1.5;
    spec.latitudeOfFirstGridPointInDegrees  = 60.0;
    spec.longitudeOfFirstGridPointInDegrees = -9.0;
    spec.latitudeOfLastGridPointInDegrees   = 40.5;
    spec.longitudeOfLastGridPointInDegrees  = 15.0;
    spec.bitmapPresent = 0;

    /*packing_spec.packing_type = GRIB_UTIL_PACKING_TYPE_GRID_SIMPLE;*/
    packing_spec.packing_type = get_packing_type_code(packingType);
    packing_spec.bitsPerValue = 24;
    packing_spec.accuracy=GRIB_UTIL_ACCURACY_USE_PROVIDED_BITS_PER_VALUES;
    packing_spec.packing=GRIB_UTIL_PACKING_USE_PROVIDED;

    if (edition != 0) {
        packing_spec.editionNumber = edition;
    }
    if (remove_local_def) {
        packing_spec.deleteLocalDefinition = 1;
    }

    finalh = codes_grib_util_set_spec(
            handle,
            &spec,
            &packing_spec,
            set_spec_flags,
            values,
            outlen,
            &err);
    assert(finalh);
    assert(err == 0);

    /* Write out the message to the output file */
    CODES_CHECK(codes_get_message(finalh, &buffer, &size),0);
    if(fwrite(buffer,1,size,out) != size) {
        assert(0);
    }
    codes_handle_delete(handle);
    codes_handle_delete(finalh);
    fclose(in);
    fclose(out);
}

void usage(const char *prog)
{
    fprintf(stderr, "%s: [-p packingType] [-r] [-e edition] in.grib out.grib\n", prog);
    fprintf(stderr, "-p  packingType: one of grid_jpeg, grid_second_order or grid_simple\n");
    fprintf(stderr, "-r  remove local definition\n");
    fprintf(stderr, "-e  edition: 1 or 2\n");
    exit(1);
}

int main(int argc, char *argv[])
{
    int opt = 0, remove_local_def = 0;
    int edition = 0;
    char* packingType = NULL;
    const char* prog = argv[0];
    char* infile_name = NULL;
    char* outfile_name = NULL;
    
    while ((opt = getopt(argc, argv, "re:p:")) != -1) {
        switch (opt) {
            case 'r':
                remove_local_def=1;
                break;
            case 'p':
                packingType = optarg;
                break;
            case 'e':
                edition = atoi(optarg);
                break;
            default:
                usage(prog);
                break;
        }
    }

    /* After option processing expect just two files */
    if (argc-optind != 2) usage(prog);

    /*for (i = optind; i < argc; i++) {
        printf ("File argument %s\n", argv[i]);
    }*/

    infile_name = argv[argc-2];
    outfile_name = argv[argc-1];

    test_regular_ll(remove_local_def, edition, packingType, infile_name, outfile_name);
    test_reduced_gg(remove_local_def, edition, packingType, infile_name, outfile_name);

    return 0;
}
