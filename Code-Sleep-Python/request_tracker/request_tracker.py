#!/usr/bin/python3
import csv
from datetime import datetime
import pygal
import requests
import signal
import sys
import time


def getDeltaFromRequest(req):
    reqDelta = req.elapsed
    microDelta = reqDelta.microseconds
    milliDelta = microDelta / 1000

    return milliDelta


# TODO: Allow automatically stopping after some time
# TODO: Allow using a premade CSV file, generating chart and exiting.
# TODO: Split into a separate file or library.
class RequestTracker:
    url = None
    interval = 30
    working = False
    dataPoints = 0

    csvEnabled = False
    csvFile = None
    csvFilename = None
    csvWriter = None

    graphEnabled = False
    graphFilename = None
    graphData = []
    graph = None

    verbosityEnabled = False

    def __init__(self, url, interval=30):
        # TODO: Validate URL here or later
        self.url = url
        self.interval = interval

    def enableVerbosity(self):
        self.verbosityEnabled = True
        self.verbose('DBG : Verbosity enabled')

    def disableVerbosity(self):
        self.verbosityEnabled = False

    # TODO: Create .dbg, .info, .warn, .err functions based on this
    def verbose(self, str):
        if self.verbosityEnabled:
            print(str)

    def midrunError(self, str):
        self.verbose('ERR : Cannot toggle ' + str + ' during a run.')
        self.verbose('ERR : Stop the run, toggle ' + str + ' and start again.')

    def enableGraphs(self):
        if self.working:
            self.midrunError('graphs')
            return

        if self.graphEnabled:
            return

        if self.graphFilename is None:
            self.verbose('ERR : No graph filename set yet')
            return

        self.graphEnabled = True
        self.verbose('DBG : Graph will be output at end of run')

    def disableGraphs(self):
        if self.working:
            self.midrunError('graphs')
            return

        if not self.graphEnabled:
            return

        self.graphEnabled = False
        self.verbose('DBG : Graphs will not be output at end of run')

    def setGraphFilename(self, name):
        self.graphFilename = name
        self.verbose('DBG : Graph filename set to ' + name)

    def enableCSV(self):
        if self.working:
            self.midrunError('CSV')
            return

        if self.csvEnabled:
            return

        if self.csvFilename is None:
            self.verbose('ERR : No CSV filename set yet')
            return

        self.csvEnabled = True
        self.verbose('DBG : CSV file will be output throughout run')

    def disableCSV(self):
        if self.working:
            self.midrunError('CSV')
            return

        if not self.csvEnabled:
            return

        self.csvEnabled = False
        self.verbose('DBG : CSV wil not be output throughout run')

    def setCSVFilename(self, name):
        self.csvFilename = name
        self.verbose('DBG : Graph filename set to ' + name)

    def setInterval(self, interval):
        if self.working:
            self.midrunError('interval')
            return

        if interval <= 0:
            self.verbose('DBG : Cannot set an interval <= 0.')
            return

        self.interval = interval

    def start(self):
        if self.working:
            return

        self.working = True
        self.verbose('INFO: Starting run on URL ' + self.url)

        if self.graphEnabled:
            newGraph = pygal.Line()
            newGraph.title = 'Load delay over time for ' + self.url
            newGraph.x_labels = []

            self.graph = newGraph
            self.graph.add('Delay', self.graphData)
            self.verbose('DBG : Created graph')

        if self.csvEnabled:
            fields = ['timestamp', 'delay']
            self.csvFile = open(self.csvFilename, 'w', newline='')
            self.csvWriter = csv.DictWriter(self.csvFile, fieldnames=fields)

            self.csvWriter.writeheader()
            self.verbose('DBG : Created CSV file')

        self.work()

    def stop(self):
        if not self.working:
            return

        self.working = False
        self.closeCSV()
        self.finishGraph()

        self.verbose('INFO: Stopping run on URL ' + self.url)

    def closeCSV(self):
        if not self.csvEnabled:
            return

        self.csvFile.close()
        self.csvFile = None

    def dumpGraph(self):
        if not self.graphEnabled:
            return

        self.graph.render_to_file(self.graphFilename)

    def finishGraph(self):
        self.dumpGraph()
        self.graph = None
        self.graphData = []

    def processGraphData(self, timestamp, delay):
        if not self.graphEnabled:
            return

        szDatetime = str(datetime.fromtimestamp(timestamp))
        self.graph.x_labels.append(szDatetime)
        self.graphData.append(delay)

    def processCSVData(self, timestamp, delay):
        if not self.csvEnabled:
            return

        formattedData = {'timestamp': timestamp, 'delay': delay}
        self.csvWriter.writerow(formattedData)
        self.csvFile.flush()

    def processData(self, timestamp, delay):
        self.processGraphData(timestamp, delay)
        self.processCSVData(timestamp, delay)

    def work(self):
        self.verbose('INFO: Work started')
        while self.working:
            req = requests.get(self.url)
            timestamp = time.time()

            if req is None:
                print('INFO: Server failed to respond. Timestamp: ' + time)
                self.processCSVData(timestamp, 'Nonresponse')
                self.processGraphData(timestamp, 0)

            elif req.ok is not True:
                print('INFO: Server failing with code ' + str(req.getcode()))
                self.processCSVData(timestamp, 'HTTP ' + str(req.getcode()))
                self.processGraphData(timestamp, 0)

            else:
                milliDelta = getDeltaFromRequest(req)
                self.processData(timestamp, milliDelta)

                szDelta = str(milliDelta)
                szTime = str(timestamp)
                self.verbose('DBG : Delay=' + szDelta + ' Time=' + szTime)

                self.dataPoints += 1
                # FIXME: remove later?
                self.dumpGraph()

            time.sleep(self.interval)


# TODO: argv
worker = None


def sigint(signal, frame):
    if worker is not None:
        worker.verbose('WARN: SIGINT, shutting down')
        worker.stop()

        points = str(worker.dataPoints)
        print('Successfully stopped tracker with ' + points + ' data points')

    sys.exit(0)

signal.signal(signal.SIGINT, sigint)

worker = RequestTracker('http://facebook.com', 60)
worker.enableVerbosity()

worker.setGraphFilename('graph.svg')
worker.enableGraphs()

worker.setCSVFilename('decisions.csv')
worker.enableCSV()

worker.start()

