from urllib.parse import urljoin
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

apiVersion = config['DEFAULT']['tomtomApiVersion']
tomtomBaseUrl = config['DEFAULT']['tomtomApiUrl']
tomtomApiKey = config['DEFAULT']['AtomtomApiKey']

def BuildPostRouteAnalysisJobUrl():
    url = urljoin(tomtomBaseUrl,'/traffic/trafficstats/routeanalysis')
    url = urljoin(url, apiVersion)
    url = urljoin(url, '?key={}'.format(tomtomApiKey))
return url

def BuildGetRouteAnalysisJobStatusUrl(string jobId):
    url = urljoin(tomtomBaseUrl,'/traffic/trafficstats/status/')
    url = urljoin(url, apiVersion)
    url = urljoin(url, '{}?key={}'.format(jobId, tomtomApiKey))
    return url