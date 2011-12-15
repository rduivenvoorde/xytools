XY Tools plugin (version 0.2)
=============================

Aim
---

The idea of the xy-tools-plugin is to group some functionality needed when you often work with tables with x and y columns (eg Excel files, dbf files or even txt/csv files).

The plugin has the following functions:

1. fill an x- and y-column of a given attribute table by clicking on a (reference) map.

2. after 'filling the x and y column' you are able to export the table to a point shape file by using the x- and y-column as coordinates for the Point geometries

3. open Excel files, either as a Memory-layer with geometries on 0,0 or using coordinates from an x and y column

4. save the attribute table of a layer as an Excel file

It started off as a plugin for a user who had an excell file with
toponiemen / fieldnames and a stack of old scanned cadastral maps.

Use
---

If you have installed the xytools plugins, you should see a new button in the edit/digitize toolbar (see red circle in image):

.. image:: img/xytoolbutton.png

and a context menu in the plugin menu:

.. image:: img/save.png

Filling an x and y column of a dbf file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the dbf file by opening it as a normal 'vector' layer.

Start by 'toggle edit' of a given layer (1).

When the layer is a vector layer, the xytool-button will be activated (2).

When checked a dialog pops up (3) where you will have to choose the
x and y columns.

Before clicking in the map: open the attribute table and make one feature/record active (4).

.. image:: img/activate.png

You can now click in the map to fill the designated x and y fields of the selected record. 

When selecting a record in the attribute table a red cross is shown on those x,y coordinates

The tool behaves as a normal digitize tool. By toggling editing again you will be asked to either
save your edits, or discard them.

.. image:: img/click.png


Saving the attribute table as a shape file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the menu of xy tools there is the possibility to save a attribute table as a point shape file (img below).

Geometries of the shape file will be using the x- and y- columns for there coordinates.

.. image:: img/save.png

Opening an Excel file as a Vector layer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*(to use this functionality you should have the xlrd library installed. On Windows you can get it via osgeo4w. For Linux you can probably install it via your package manager. Or you can get it from the project page: http://www.python-excel.org/ )*

Op open an Excel file and use it either as a attribute table OR as a point vector layer, choose 'Open Excel file as attribute tabl or Point layer' from the xytools plugin menu options:

.. image:: img/save.png

You will be given the option to choose an x- and y-column from the excel file. The values of those columns will be used as x and y coordinate for the Point features of the Memory layer. 

You can also CANCEL the xy-column dialog, then the rows will also be read as features, BUT the geometries will all have zero's as x and y 

There are some things to consider for this:

- the excel file is read into a 'Memory layer'. That is it is volatile: **edits in this layer will NOT be saved into the excel file**  AND quiting QGIS will discard the layer. If you want to save the layer, use the normal QGIS menu options to save the memory layer to something else like a shapefile, a spatialite file or an KML-file.

- the first row of the excel file will be read as attribute names/keys. So if you have data without a column header, please add one before opening it in qgis with the xytool plugin

- when there is a non numeric value in one of the cells of the excel table, the proces is stopped and the layer is discarded

- opening of newer Excel (xlsx) files is not supported by the python lib used for handling excel files. Use LibreOffice, OpenOffice or Excel to open the file and save it as a xls file first.

Saving the attribute table of a vector layer as an Excel file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*(to use this functionality you should have the xlw library installed. On Windows you can get it via osgeo4w. For Linux you can probably install it via your package manager. Or you can get it from the project page: http://www.python-excel.org/ )*

When you have a vector layer active, choose 'Save attribute table as Excel file' from the xytools plugin menu options:

.. image:: img/save.png

It will ask you where to save the file and do a simple save. That is: use the attribute key's in the first row and all values of a geometry as a row (as strings).



Notes and versions
------------------

Currently the plugin is working both with shape files and single dbf-files. Saving csv files is not supported by
the underlying OGR-library.

So: for a dbf you can add and remove records. But if you want further editing: like inserting records, adding columns etc,
either use Libre/Open-office, or one of the other qgis table plugins.

- 0.2.0 open Excel files either as attribute table, or as point shape file (python xlrd lib needed).  Ability to save current attributetable as an Excel file (python xlwt lib needed). Attiion of plugin metadata to plugin.

- 0.1.2 coordinates as floats instead of ints, Makefile and dist changes

- 0.1.1 first public version in git



Ideas/todo
----------

- maybe some kind of dialog for the plugin?

- after clicking an xy, move selected record in attribute table to next row (and stop doing this if the click is a right click)

- instead of saving as shape: make it a memory layer, giving it the possibility to use the generic 'save as'-whatever dialog.

- reproject / change srs of a table containing x and y colum

- selecting a record of a single dbf raises errors in command box


And
---

If you find bugs or have ideas for this plugin, contact Richard Duivenvoorde ( richard@duif.net ).
