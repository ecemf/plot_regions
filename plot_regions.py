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

DATA_DIR = ''

def main(regions):
    """

    Arguments
    ---------
    regions : dict
        A nester dictionary of region aggregations
    """
    path_rg = os.path.join(DATA_DIR + "NUTS_RG_60M_2021_3035.geojson")
    gdf_rg = gpd.read_file(path_rg)
    gdf_rg.crs = "EPSG:3035"

    gdf_rg = gdf_rg[gdf_rg.LEVL_CODE == 0]

    gdf_rg['region'] = gdf_rg.CNTR_CODE.map(regions)

    fig, ax = plt.subplots()
    gdf_rg.plot(gdf_rg.region, ax=ax, figsize=(20,15), cmap='Accent',
                missing_kwds={'color': 'lightgrey'}, legend=True)
    ax.set_xlim(0.2e7, 0.8e7)
    ax.set_ylim(1.0e6, 6.0e6)
    fig.savefig('test.png')


def test_main():

    regions = {
        'FR' : 'WEU',
        'DE': 'EEU'
        }

    actual = main(regions)
    expected = None
    assert actual == expected

if __name__ == "__main__":

    test_main()