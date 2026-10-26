def classFactory(iface):
    from .gis_agent import GISAgentPlugin
    return GISAgentPlugin(iface)