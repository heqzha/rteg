#Road and Traffic Environment Generator(RTEG)
Road and Traffic Environment Generator is used to create Manhattan mobility model based road traffic environment which could run in SUMO. The size of city, number of roads, type of road, number of vehciles and size of obsticles(Building) could be customized.

To Run:
1. Start rteg, run python Main.py
2. Results are in Data/GridNetwork/
3. Generate road network, run: netconvert -c GridNetwork.netccfg
4. Test in sumo, run: sumo-gui GridNetwork.sumocfg
