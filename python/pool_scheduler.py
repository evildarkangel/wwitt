
# Scheduler Pool
# Creates N instances of a worker class and feeds them data as necessary

from async_http import Async_HTTP
from dns_solver import DNS_Solver

class Pool_Scheduler():
	def __init__(self,num_workers,constructor,*args):
		self._workers = []
		for i in range(num_workers):
			worker = constructor(*args)
			worker.start()
			self._workers.append(worker)

	# Jobs is a list of jobs to be distributed
	def addWork(self,jobs):
		while (len(jobs) != 0):
			print len(jobs)
			# Scheduler the work in the worker with less work
			worker = min ( (x.numPendingJobs(),x) for x in self._workers ) [1]
			worker.enqueueJobs( [jobs.pop()] )

	# Gets number of jobs still to finish
	def numActiveJobs(self):
		return ( x.numPendingJobs() for x in self._workers )

	# Stop all workers!
	def finalize(self):
		for w in self._workers:
			w.stopWorking()

	# Wait jobs to finish
	def wait(self):
		for w in self._workers:
			w.waitEnd()

	# Get emptiest worker
	def getWorkerInstance(self):
		return min ( (x.numPendingJobs(),x) for x in self._workers ) [1]


