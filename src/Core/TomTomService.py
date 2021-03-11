from ..Infrastructure.TomTomGateway import buildRouteAnalysisUrl
import requests


def buildPostRouteAnalysisJobUrl(payload):
    url = BuildRouteAnalysisUrl()

    r = requests.post(url, payload)
}

def GetRouteAnalysisJobStatusAsync(payload):
        url = BuildGetRouteAnalysisJobStatusUrl(payload.jobId)

        r = requests.get(url)