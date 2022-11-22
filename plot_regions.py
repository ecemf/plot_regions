"""Plot regional aggregation

Arguments
---------
regions : dict
    A nester dictionary of region aggregations

Returns
-------
png file
"""

import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import os

DATA_DIR = 'data'

def main(regions):
    """

    Arguments
    ---------
    regions : dict
        A nester dictionary of region aggregations
    """
    path_rg = os.path.join(DATA_DIR, "NUTS_RG_60M_2021_3035.geojson")
    gdf_rg = gpd.read_file(path_rg)
    gdf_rg.crs = "EPSG:3035"

    gdf_rg = gdf_rg[gdf_rg.LEVL_CODE == 0]

    gdf_rg['region'] = gdf_rg.CNTR_CODE.map(regions)

    fig, ax = plt.subplots()
    gdf_rg.plot(gdf_rg.region, ax=ax, figsize=(20,15), cmap='Accent',
                missing_kwds={'color': 'lightgrey'}, legend=True)
    ax.set_xlim(0.2e7, 0.8e7)
    ax.set_ylim(1.2e6, 5.6e6)
    ax.axis('off')
    fig.savefig('example.png', bbox_inches='tight')


def test_main():

    regions = {
        'AT' : 'WEU',
        'BE' : 'WEU',
        'BG' : 'EEU',
        'HR' : 'EEU',
        'CY' : 'EEU',
        'CZ' : 'EEU',
        'DK' : 'WEU',
        'EE' : 'EEU',
        'FI' : 'SCA',
        'FR' : 'WEU',
        'DE' : 'WEU',
        'GR' : 'WEU',
        'HU' : 'EEU',
        'IE' : 'WEU',
        'IT' : 'WEU',
        'LV' : 'EEU',
        'LT' : 'EEU',
        'LU' : 'WEU',
        'MT' : 'WEU',
        'NL' : 'WEU',
        'NO' : 'SCA',
        'PL' : 'EEU',
        'PT' : 'WEU',
        'RO' : 'EEU',
        'SK' : 'EEU',
        'SI' : 'EEU',
        'ES' : 'WEU',
        'SE' : 'SCA',
        'UK' : 'WEU',
        }

    actual = main(regions)
    expected = None
    assert actual == expected

if __name__ == "__main__":

    test_main()