#!/usr/bin/env python3
# coding: utf-8

import SimpleITK as sitk

dirname = 'dicom'

series_IDs = sitk.ImageSeriesReader_GetGDCMSeriesIDs(dirname)

if not series_IDs:
    print('No series in directory ' + '\'' + dirname + '\'')

for series in series_IDs:
    filename = series.split('.')[-1]
    sitk.WriteImage(sitk.ReadImage(sitk.ImageSeriesReader_GetGDCMSeriesFileNames(dirname, series)),
                    'mhd/'+filename+'.mhd')
