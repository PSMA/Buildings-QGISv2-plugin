# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BuildingBeta
                                 A QGIS plugin
 BuildingBeta
                             -------------------
        begin                : 2018-02-12
        copyright            : (C) 2018 by BuildingBeta
        email                : BuildingBeta
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BuildingBeta class from file BuildingBeta.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .building_beta import BuildingBeta
    return BuildingBeta(iface)
