#!/usr/bin/env python
import pdb
from Src.Network.GridNetwork import GridNetwork
#from Src.Network.Obj.Edge import Edge
from Src.PrintOut.PrintOutGridNetwork import PrintOutGridNetwork

gNetwork = GridNetwork(2,2,1000,900)
gNodeList = gNetwork.genGridNodes()
gNetwork.genGridAdjArea(gNetwork.EDGE_TYPE_SECONDARY_URBAN)
gNetwork.genVehicles()#TODO the number of vehicle should set at here
#gNetwork.genPloys(4,600)
gNetwork.genPolyGroup(4,3, 3.0)

NetworkName = "GridNetwork"
#Print out .nod.xml
printOut = PrintOutGridNetwork(NetworkName, PrintOutGridNetwork.FILE_TYPE_NOD, PrintOutGridNetwork.FILE_SUFFIX_XML, PrintOutGridNetwork.TAG_NODES)
printOut.printOutNodXml(gNodeList)
#Print out .edg.xml
printOut = PrintOutGridNetwork(NetworkName, PrintOutGridNetwork.FILE_TYPE_EDG, PrintOutGridNetwork.FILE_SUFFIX_XML,	PrintOutGridNetwork.TAG_EDGES)
printOut.printOutEdgXml(gNodeList)
#Print out .typ.xml
printOut = PrintOutGridNetwork(NetworkName, PrintOutGridNetwork.FILE_TYPE_TYP, PrintOutGridNetwork.FILE_SUFFIX_XML,	PrintOutGridNetwork.TAG_TYPES)
printOut.printOutTypXml(gNetwork.getEdgeType())
#Print out .rou.xml
printOut = PrintOutGridNetwork(NetworkName, PrintOutGridNetwork.FILE_TYPE_ROU, PrintOutGridNetwork.FILE_SUFFIX_XML, PrintOutGridNetwork.TAG_ROUTES)
printOut.printOutRouXml(gNetwork.getVehicleList(), gNetwork.getVehicleType())
#Print out .poly.xml
printOut = PrintOutGridNetwork(NetworkName, PrintOutGridNetwork.FILE_TYPE_POLY, PrintOutGridNetwork.FILE_SUFFIX_XML, PrintOutGridNetwork.TAG_SHAPES)
printOut.printOutPolyXml(gNetwork.getPolyList())

