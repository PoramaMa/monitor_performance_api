from cpu import *
from ram import *
from disk import *
dataCPU = []
total_cpu_avg = 0
dataRAM = []
used_ram_percent = 0
dataDISK = []
used_disk_percent = 0


class getStatusCPU(Resource):
    def get(self):
        global total_cpu_avg
        return str(total_cpu_avg)


class addStatusCPU(Resource):
    def post(self):
        global dataCPU
        global total_cpu_avg
        body = request.json
        dataCPU = body['data']
        total_cpu_avg = body['status']
        return str(total_cpu_avg)


class getStatusRAM(Resource):
    def get(self):
        global used_ram_percent
        return str(used_ram_percent)


class addStatusRAM(Resource):
    def post(self):
        global dataRAM
        global used_ram_percent
        body = request.json
        dataRAM = body['data']
        used_ram_percent = body['status']
        return str(used_ram_percent)


class getStatusDisk(Resource):
    def get(self):
        global used_disk_percent
        return str(used_disk_percent)


class addStatusDisk(Resource):
    def post(self):
        global dataDISK
        global used_disk_percent
        body = request.json
        dataDISK = body['data']
        used_disk_percent = body['status']
        return str(used_disk_percent)


class getAllPerformances(Resource):
    def get(self):
        global total_cpu_avg
        global used_ram_percent
        global used_disk_percent

        data = [{
            "labels": ["CPU"],
            "datasets": [
                {
                    "backgroundColor": ["#E46651", "#41B883"],
                    "data": [float(total_cpu_avg), 100-float(total_cpu_avg)],
                },
            ],
            "data": dataCPU
        }, {
            "labels": ["RAM"],
            "datasets": [
                {
                    "backgroundColor": ["#00D8FF", "#41B883"],
                    "data": [float(used_ram_percent), 100-float(used_ram_percent)],
                },
            ],
            "data": dataRAM
        }, {
            "labels": ["DISK"],
            "datasets": [
                {
                    "backgroundColor": ["#DD1B16", "#41B883"],
                    "data": [float(used_disk_percent), 100-float(used_disk_percent)],
                },
            ],
            "data": dataDISK
        }
        ]
        return data


api.add_resource(getStatusCPU, '/api/get/cpu')
api.add_resource(addStatusCPU, '/api/add/cpu')
api.add_resource(getStatusRAM, '/api/get/ram')
api.add_resource(addStatusRAM, '/api/add/ram')
api.add_resource(getStatusDisk, '/api/get/disk')
api.add_resource(addStatusDisk, '/api/add/disk')
api.add_resource(getAllPerformances, '/api/get/allPerformances')

if __name__ == '__main__':
    p1 = Process(target=run_cpu)
    p1.start()
    p2 = Process(target=run_ram)
    p2.start()
    p3 = Process(target=run_disk)
    p3.start()
    app.run(host='0.0.0.0')
    # app.run(host='0.0.0.0', port=6111)
    app.run(debug=False)
