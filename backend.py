import osmnx as ox
import networkx as nx
import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString, MultiPoint
from shapely.ops import nearest_points
from fiona.crs import from_epsg
import branca.colormap as cm
import folium
import pysal


def networkFromPlaceName(regionName, networkType="all", whichResult=1):
    """
    Create a networkx graph from OSM database within the spatial \
boundaries of user entered region name.

    Parameters
    ----------
    regionName: string
        name of the area where the road network data is obtained
    networkType: string
        what type of street network to get
    whichResult: integer
        resulting number that returns polygon data from the
        query of OpenStreetMap database

    Returns
    -------
    G: networkx multidigraph
        road network of region
    """

    G = ox.graph_from_place(regionName, network_type=str(networkType),
                            which_result=int(whichResult))
    return G


def networkFromPolygon(shpLocation, networkType="all"):
    """
    Create a networkx graph from OSM database within the \
spatial boundaries of user entered shapefile.

    Parameters
    ----------
    name: string
        absolute path of the shapefile to be used
    *args: string
        what type of street network to get

    Returns
    -------
    G: networkx multidigraph
        road network of region
    """

    boundary = gpd.read_file(shpLocation)
    boundary["geometry"] = boundary["geometry"].to_crs(epsg=4326)
    boundary.crs = from_epsg(4326)
    geometry = boundary.geometry.values[0]
    check = geometry.is_valid

    if check:
        G = ox.graph_from_polygon(geometry, clean_periphery=False,
                                  network_type=str(networkType))
        return G
    elif not check:
        return "N"


def degreeCentrality(G, outPath, *args):
    """
    Compute degree centrality of a node and save the output and road network
    data in shapefile format.

    Parameters
    ----------
    G: graph
        A networkx graph
    outpath: string
        absolute path to save the output of analysis
    *args: string
        path to save the output of analysis in html webmap format

    Returns
    -------
    ################################################################
    """

    G_proj = nx.MultiGraph(ox.project_graph(G))
    nodes, edges = ox.graph_to_gdfs(G_proj)
    nodes["x"] = nodes["x"].astype(float)

    degree_centrality = nx.degree_centrality(G_proj)
    degree = gpd.GeoDataFrame(pd.Series(degree_centrality), columns=["degree"])
    nodes_dgr = nodes.merge(degree, left_index=True, right_index=True)

    argument = [i for i in args]
    if any(argument):
        linear = cm.LinearColormap(["blue", "yellow", "red"], vmin=0, vmax=5)
        nodes_dgr['geoid'] = nodes_dgr.index.astype(str)
        lat = list(nodes_dgr["lat"])
        lon = list(nodes_dgr["lon"])
        dgr = list(nodes_dgr["degree"])
        name = list(nodes_dgr["osmid"])

        m = ox.plot_graph_folium(G, edge_width=1.5)
        fgdgr = folium.FeatureGroup(name="Degrees of Nodes")

        classifier = pysal.viz.mapclassify.NaturalBreaks.make(k=5)
        classifications = nodes_dgr[["degree"]].apply(classifier)
        classifications.columns = ["class"]
        nodes_dgr = nodes_dgr.join(classifications)

        for lt, ln, dg, nm, cl in zip(
                lat, lon, dgr, name, list(nodes_dgr["class"])
                ):
            fgdgr.add_child(
                folium.CircleMarker(
                    location=[lt, ln],
                    popup='Degree Centrality of the {}. \
node is {:.5f}'.format(str(nm), dg),
                    radius=4, fill_color=linear(cl), color="grey",
                    fill_opacity=1, weight=0.5)
                    )

        # fgavg.add_child(marker_cluster)
        m.add_child(fgdgr)
        # m.add_child(linear)
        m.save(argument[0])

        ox.save_graph_shapefile(G_proj, filename="network", folder=outPath)
        nodes_dgr.to_file(outPath + "/degree_centrality.shp")
        return "I"
    else:
        ox.save_graph_shapefile(G_proj, filename="network", folder=outPath)
        nodes_dgr.to_file(outPath + "/degree_centrality.shp")
        return "G"


def betweennessCentrality(G, outPath, *args):
    """
    Compute betweenness centrality of a node and \
save the output and road network
    data in shapefile format.

    Parameters
    ----------
    G: graph
        A networkx graph
    outpath: string
        absolute path to save the output of analysis
    *args: string
        path to save the output of analysis in html webmap format

    Returns
    -------
    ################################################################
    """

    G_proj = nx.MultiGraph(ox.project_graph(G))
    nodes, edges = ox.graph_to_gdfs(G_proj)
    nodes["x"] = nodes["x"].astype(float)

    G_proj = nx.DiGraph(G_proj)
    btw_centrality = nx.betweenness_centrality(G_proj)
    betweenness = gpd.GeoDataFrame(pd.Series(btw_centrality),
                                   columns=["betweenness"])
    nodes_btw = nodes.merge(betweenness, left_index=True, right_index=True)

    argument = [i for i in args]
    if any(argument):
        linear = cm.LinearColormap(["blue", "yellow", "red"], vmin=0, vmax=5)
        nodes_btw['geoid'] = nodes_btw.index.astype(str)
        lat = list(nodes_btw["lat"])
        lon = list(nodes_btw["lon"])
        btw = list(nodes_btw["betweenness"])
        name = list(nodes_btw["osmid"])

        m = ox.plot_graph_folium(G, edge_width=1.5)
        fgbtw = folium.FeatureGroup(name="Betweenness Centrality of Nodes")

        classifier = pysal.viz.mapclassify.NaturalBreaks.make(k=5)
        classifications = nodes_btw[["betweenness"]].apply(classifier)
        classifications.columns = ["class"]
        nodes_btw = nodes_btw.join(classifications)

        for lt, ln, bt, nm, cl in zip(
                lat, lon, btw, name, list(nodes_btw["class"])):
            fgbtw.add_child(
                folium.CircleMarker(
                    location=[lt, ln],
                    popup='Betweenness Degree of the {}. \
node is {:.5f}'.format(str(nm), bt),
                    radius=4, fill_color=linear(cl), color="grey",
                    fill_opacity=1, weight=0.5)
                    )

        m.add_child(fgbtw)
        m.save(argument[0])
        
        G_proj = nx.MultiGraph(G_proj)
        ox.save_graph_shapefile(G_proj, filename="network", folder=outPath)
        nodes_btw.to_file(outPath + "/btw_centrality.shp")
        return "I"
    else:
        G_proj = nx.MultiGraph(G_proj)
        ox.save_graph_shapefile(G_proj, filename="network", folder=outPath)
        nodes_btw.to_file(outPath + "/btw_centrality.shp")
        return "G"


def closenessCentrality(G, outPath, *args):
    """
    Compute closeness centrality of a node and \
save the output and road network
    data in shapefile format.

    Parameters
    ----------
    G: graph
        A networkx graph
    outpath: string
        path to save the output of analysis
    *args: string
        path to save the output of analysis in html webmap format

    Returns
    -------
    ################################################################
    """

    G_proj = nx.MultiGraph(ox.project_graph(G))
    nodes, edges = ox.graph_to_gdfs(G_proj)
    nodes["x"] = nodes["x"].astype(float)

    cls_centrality = nx.closeness_centrality(G_proj)
    closeness = gpd.GeoDataFrame(pd.Series(cls_centrality),
                                 columns=["closeness"])
    nodes_cls = nodes.merge(closeness, left_index=True, right_index=True)

    argument = [i for i in args]
    if any(argument):
        linear = cm.LinearColormap(["blue", "yellow", "red"], vmin=0, vmax=5)
        nodes_cls['geoid'] = nodes_cls.index.astype(str)
        lat = list(nodes_cls["lat"])
        lon = list(nodes_cls["lon"])
        clsn = list(nodes_cls["closeness"])
        name = list(nodes_cls["osmid"])

        m = ox.plot_graph_folium(G, edge_width=1.5)
        fgcls = folium.FeatureGroup(name="Closeness Centrality of Nodes")

        classifier = pysal.viz.mapclassify.NaturalBreaks.make(k=5)
        classifications = nodes_cls[["closeness"]].apply(classifier)
        classifications.columns = ["class"]
        nodes_cls = nodes_cls.join(classifications)

        for lt, ln, cl, nm, clss in zip(
                lat, lon, clsn, name, list(nodes_cls["class"])):
            fgcls.add_child(
                folium.CircleMarker(
                    location=[lt, ln],
                    popup='Closeness Degree of the {}. \
node is {:.5f}'.format(str(nm), cl),
                    radius=4, fill_color=linear(clss), color="grey",
                    fill_opacity=1, weight=0.5))

        m.add_child(fgcls)
        m.save(argument[0])

        ox.save_graph_shapefile(G_proj, filename="network", folder=outPath)
        nodes_cls.to_file(outPath + "/cls_centrality.shp")
        return "I"
    else:
        ox.save_graph_shapefile(G_proj, filename="network", folder=outPath)
        nodes_cls.to_file(outPath + "/cls_centrality.shp")
        return "G"


def origindestination(originPath, destinationPath, networkType="all"):
    """
    Create a bounding box from user entered origin and destination points, \
get the corresponding road network
    and form the origin destination cost matrix.

    Parameters
    ----------
    originPath: string
        absolute path of the origin shapefile to be used
    destinationPath: string
        absolute path of the destination shapefile to be used
    networkType: string
        what type of street network to get

    Returns
    -------
    route_gdf: GeoDataFrame
        geopandas dataframe of routes
    nodes: GeoDataFrame
        geopandas dataframe of nodes
    G_proj: networkx multidigraph
        road network of closed region that is reprojected in corresponding \
UTM zone
    """

    origins = gpd.read_file(originPath)
    destinations = gpd.read_file(destinationPath)

    origins["geometry"] = origins["geometry"].to_crs(epsg=4326)
    destinations["geometry"] = destinations["geometry"].to_crs(epsg=4326)
    origins.crs = from_epsg(4326)
    destinations.crs = from_epsg(4326)

    points_concat = gpd.GeoDataFrame(pd.concat([origins, destinations],
                                               ignore_index=True, sort=True))
    minx, miny, maxx, maxy = points_concat.geometry.total_bounds

    G = ox.graph_from_bbox(maxy+0.005, miny-0.005, maxx+0.005, minx-0.005,
                           clean_periphery=False,
                           network_type=str(networkType))

    G_proj = nx.MultiGraph(ox.project_graph(G))
    nodes, edges = ox.graph_to_gdfs(G_proj)
    nodes["x"] = nodes["x"].astype(float)

    origins = origins.to_crs(nodes.crs)
    destinations = destinations.to_crs(nodes.crs)
    origins["x"] = origins.geometry.x
    origins["y"] = origins.geometry.y
    destinations["x"] = destinations.geometry.x
    destinations["y"] = destinations.geometry.y

    orignodes = list(ox.get_nearest_nodes(G_proj, origins["x"],
                                          origins["y"], method="kdtree"))
    destnodes = list(ox.get_nearest_nodes(G_proj, destinations["x"],
                                          destinations["y"], method="kdtree"))

    routelinelist = []
    fromlist = []
    tolist = []
    for dest in destnodes:
        for org in orignodes:
            try:
                route = nx.shortest_path(G_proj, org, dest, weight="length")
                route_nodes = nodes.loc[route]
                fromlist.append(route[0])
                tolist.append(route[-1])
                route_line = LineString(list(route_nodes.geometry.values))
                routelinelist.append(route_line)
            except:
                pass

    route_gdf = gpd.GeoDataFrame(crs=edges.crs)
    route_gdf["geometry"] = routelinelist
    route_gdf["length"] = route_gdf.length
    route_gdf["from_id"] = fromlist
    route_gdf["to_id"] = tolist

    return route_gdf, nodes, G_proj, origins, destinations


def potentialAccessibility(gdf, nodes, G, origins,
                           destinations, outPath, weight=1, *args):
    """
    Write the result of potential accessibility \
analysis to shapefile and webmap*.
    *Optional

    Parameters
    ----------
    gdf: GeoDataFrame
        geopandas dataframe of routes
    nodes: GeoDataFrame
        geopandas dataframe of nodes
    G: networkx multidigraph
        road network
    *args: string
        path to save the output of analysis in html webmap format

    Returns
    -------
    ####################################################
    """

    gdf["access"] = (1 / (gdf["length"]/1000))

    orig_grouped = (
        (gdf.groupby("from_id")).sum()).merge(
            nodes, left_index=True, right_on="osmid")
            
    dest_grouped = (
        (gdf.groupby("to_id")).sum()).merge(
            nodes, left_index=True, right_on="osmid")
            
    orig_gdf = gpd.GeoDataFrame(
        orig_grouped.drop(["to_id", "y", "x", "highway", "lon", "lat"],
                            axis=1), crs=nodes.crs)
    
    dest_gdf = gpd.GeoDataFrame(
        dest_grouped.drop(["from_id", "y", "x", "highway", "lon", "lat"],
                            axis=1), crs=nodes.crs)

    def get_nearest_POI(row, gdf2):
        geom = MultiPoint(list(gdf2.geometry))
        nearest_ = nearest_points(row["geometry"], geom)
        return nearest_[1]

    orig_gdf["nearest"] = orig_gdf.apply(
        get_nearest_POI, gdf2=origins, axis=1
        )
    dest_gdf["nearest"] = dest_gdf.apply(
        get_nearest_POI, gdf2=destinations, axis=1
        )
    
    orig_gdf.geometry = orig_gdf["nearest"]
    dest_gdf.geometry = dest_gdf["nearest"]
    
    origins = gpd.sjoin(origins, orig_gdf,
                        how="inner", op="intersects")
    origins.drop(["nearest"], axis=1, inplace=True)
    destinations = gpd.sjoin(destinations, dest_gdf,
                             how="inner", op="intersects")
    destinations.drop(["nearest"], axis=1, inplace=True)

    if isinstance(weight, int):
        destinations["weighted_access"] = destinations.access*weight
    elif isinstance(weight, str):
        destinations["weighted_access"] = destinations.access*destinations.weight

    argument = [i for i in args]
    if any(argument):
        linear = cm.LinearColormap(["blue", "yellow", "red"], vmin=0, vmax=5)
        dest_grouped['geoid'] = dest_grouped.index.astype(str)
        orig_grouped['geoid'] = orig_grouped.index.astype(str)

        latd = list(dest_grouped["lat"])
        lond = list(dest_grouped["lon"])
        accd = list(dest_grouped["access"])
        named = list(dest_grouped["osmid"])

        lato = list(orig_grouped["lat"])
        lono = list(orig_grouped["lon"])
        acco = list(orig_grouped["access"])
        nameo = list(orig_grouped["osmid"])

        m = folium.Map(location=[
            dest_grouped["lat"].mean(), dest_grouped["lon"].mean()
            ], zoom_start=13, control_scale=True, prefer_canvas=True)

        fgdest = folium.FeatureGroup(name="Destination Accessibility")

        classifier = pysal.viz.mapclassify.NaturalBreaks.make(k=5)
        classifications = dest_grouped[["access"]].apply(classifier)
        classifications.columns = ["class"]
        dest_grouped = dest_grouped.join(classifications)

        for lt, ln, av, nm, cl in zip(
                latd, lond, accd, named, list(dest_grouped["class"])):
            fgdest.add_child(
                folium.CircleMarker(
                    location=[lt, ln],
                    popup='Accessibilty of {}. node is \
{:.5f}'.format(str(nm), av),
                    radius=4, fill_color=linear(cl), color="grey",
                    fill_opacity=1, weight=0.5))

        fgorig = folium.FeatureGroup(name="Origin Accessibility")

        classifications2 = orig_grouped[["access"]].apply(classifier)
        classifications2.columns = ["class"]
        orig_grouped = orig_grouped.join(classifications2)

        for lto, lno, avo, nmo, clo in zip(
                lato, lono, acco, nameo, list(orig_grouped["class"])):
            fgorig.add_child(
                folium.CircleMarker(
                    location=[lto, lno],
                    popup='Accessibilty of {}. node is \
{:.5f}'.format(str(nmo), avo),
                    radius=4, fill_color=linear(clo), color="grey",
                    fill_opacity=1, weight=0.5))

        m.add_child(fgdest)
        m.add_child(fgorig)
        folium.LayerControl().add_to(m)
        m.save(argument[0])
        ox.save_graph_shapefile(G, filename="network", folder=outPath)
        origins.to_file(outPath + "/origins.shp")
        destinations.to_file(outPath + "/destinations.shp")
        return "I"
    else:
        ox.save_graph_shapefile(G, filename="network", folder=outPath)
        origins.to_file(outPath + "/origins.shp")
        destinations.to_file(outPath + "/destinations.shp")
        return "P"


def dailyAccessibility(gdf, nodes, G, origins, destinations,
                       outPath, weight=1, threshold=3000, *args):
    """
    Write the result of daily accessibility analysis to shapefile and webmap*.
    *Optional

    Parameters
    ----------
    gdf: GeoDataFrame
        geopandas dataframe of routes
    nodes: GeoDataFrame
        geopandas dataframe of nodes
    G: networkx multidigraph
        road network
    threshold: integer or float
        threshold value for daily accessibility computations
    *args: string
        path to save the output of analysis in html webmap format

    Returns
    -------
    ####################################################
    """

    gdf = gdf[gdf["length"] < int(threshold)]
    gdf["access"] = (1 / (gdf["length"]/1000))

    orig_grouped = (
        (gdf.groupby("from_id")).sum()).merge(
            nodes, left_index=True, right_on="osmid")
            
    dest_grouped = (
        (gdf.groupby("to_id")).sum()).merge(
            nodes, left_index=True, right_on="osmid")
            
    orig_gdf = gpd.GeoDataFrame(
        orig_grouped.drop(["to_id", "y", "x", "highway", "lon", "lat"],
                            axis=1), crs=nodes.crs)
    
    dest_gdf = gpd.GeoDataFrame(
        dest_grouped.drop(["from_id", "y", "x", "highway", "lon", "lat"],
                            axis=1), crs=nodes.crs)

    def get_nearest_POI(row, gdf2):
        geom = MultiPoint(list(gdf2.geometry))
        nearest_ = nearest_points(row["geometry"], geom)
        return nearest_[1]

    orig_gdf["nearest"] = orig_gdf.apply(
        get_nearest_POI, gdf2=origins, axis=1
        )
    dest_gdf["nearest"] = dest_gdf.apply(
        get_nearest_POI, gdf2=destinations, axis=1
        )
    
    orig_gdf.geometry = orig_gdf["nearest"]
    dest_gdf.geometry = dest_gdf["nearest"]
    
    origins = gpd.sjoin(origins, orig_gdf,
                        how="inner", op="intersects")
    origins.drop(["nearest"], axis=1, inplace=True)
    destinations = gpd.sjoin(destinations, dest_gdf,
                             how="inner", op="intersects")
    destinations.drop(["nearest"], axis=1, inplace=True)

    if (isinstance(weight, int) or isinstance(weight, float)):
        destinations["weighted_access"] = destinations.access*weight
    elif isinstance(weight, str):
        destinations["weighted_access"] = destinations.access*destinations.weight

    argument = [i for i in args]
    if any(argument):
        linear = cm.LinearColormap(["blue", "yellow", "red"], vmin=0, vmax=5)
        dest_grouped['geoid'] = dest_grouped.index.astype(str)
        orig_grouped['geoid'] = orig_grouped.index.astype(str)

        latd = list(dest_grouped["lat"])
        lond = list(dest_grouped["lon"])
        accd = list(dest_grouped["access"])
        named = list(dest_grouped["osmid"])

        lato = list(orig_grouped["lat"])
        lono = list(orig_grouped["lon"])
        acco = list(orig_grouped["access"])
        nameo = list(orig_grouped["osmid"])

        m = folium.Map(location=[
            dest_grouped["lat"].mean(),
            dest_grouped["lon"].mean()
            ], zoom_start=13, control_scale=True, prefer_canvas=True)

        fgdest = folium.FeatureGroup(name="Destination Accessibility")

        classifier = pysal.viz.mapclassify.NaturalBreaks.make(k=5)
        classifications = dest_grouped[["access"]].apply(classifier)
        classifications.columns = ["class"]
        dest_grouped = dest_grouped.join(classifications)

        for lt, ln, av, nm, cl in zip(
                latd, lond, accd, named, list(dest_grouped["class"])):
            fgdest.add_child(
                folium.CircleMarker(
                    location=[lt, ln],
                    popup='Accessibilty of {}. node is \
{:.5f}'.format(str(nm), av),
                    radius=4, fill_color=linear(cl), color="grey",
                    fill_opacity=1, weight=0.5))

        fgorig = folium.FeatureGroup(name="Origin Accessibility")

        classifications2 = orig_grouped[["access"]].apply(classifier)
        classifications2.columns = ["class"]
        orig_grouped = orig_grouped.join(classifications2)

        for lto, lno, avo, nmo, clo in zip(
                lato, lono, acco, nameo, list(orig_grouped["class"])):
            fgorig.add_child(
                folium.CircleMarker(
                    location=[lto, lno], popup='Accessibilty of {}. node is \
{:.5f}'.format(str(nmo), avo),
                    radius=4, fill_color=linear(clo), color="grey",
                    fill_opacity=1, weight=0.5))

        m.add_child(fgdest)
        m.add_child(fgorig)
        folium.LayerControl().add_to(m)
        m.save(argument[0])
        ox.save_graph_shapefile(G, filename="network", folder=outPath)
        origins.to_file(outPath + "/origins.shp")
        destinations.to_file(outPath + "/destinations.shp")
        return "I" 
    else:
        ox.save_graph_shapefile(G, filename="network", folder=outPath)
        origins.to_file(outPath + "/origins.shp")
        destinations.to_file(outPath + "/destinations.shp")
        return "D"
