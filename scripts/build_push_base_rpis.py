import sys
sys.path.append("../")
import jupiter_config
import os
import configparser

sys.path.append(jupiter_config.CIRCE_PATH)

def build_push_rpis_circe():
	os.chdir(jupiter_config.CIRCE_PATH)
	os.system("sudo docker build -f rpi_circe_home.Dockerfile .. -t docker.io/anrg/rpi_circe_home:v0")
	os.system("sudo docker push docker.io/anrg/rpi_circe_home:v0")
	os.system("sudo docker build -f rpi_circe_worker.Dockerfile .. -t docker.io/anrg/rpi_circe_worker:v0")
	os.system("sudo docker push docker.io/anrg/rpi_circe_worker:v0")

def build_push_rpis_exec():
	os.chdir(jupiter_config.EXEC_PROFILER_PATH )
	os.system("sudo docker build -f rpi_exec_home.Dockerfile ../.. -t docker.io/anrg/rpi_exec_home:v0")
	os.system("sudo docker push docker.io/anrg/rpi_exec_home:v0")

	os.system("sudo docker build -f rpi_exec_worker.Dockerfile ../.. -t docker.io/anrg/rpi_exec_worker:v0")
	os.system("sudo docker push docker.io/anrg/rpi_exec_worker:v0")

def build_push_rpis_heft():
	os.chdir(jupiter_config.HEFT_PATH)
	os.system("sudo docker build -f rpi_heft.Dockerfile ../.. -t docker.io/anrg/rpi_heft:v0")
	os.system("sudo docker push docker.io/anrg/rpi_heft:v0")

def build_push_rpis_netr():
	os.chdir(jupiter_config.NETR_PROFILER_PATH)
	os.system("sudo docker build -f rpi_profiler_home.Dockerfile ../.. -t docker.io/anrg/rpi_netr_home:v0")
	os.system("sudo docker push docker.io/anrg/rpi_netr_home:v0")

	os.system("sudo docker build -f rpi_profiler_worker.Dockerfile ../.. -t docker.io/anrg/rpi_netr_worker:v0")
	os.system("sudo docker push docker.io/anrg/rpi_netr_worker:v0")

def build_push_rpis_wave():
	os.system("cp " + jupiter_config.APP_PATH + "configuration.txt " + jupiter_config.WAVE_PATH + "DAG.txt")
	os.system("cp " + jupiter_config.APP_PATH + "input_node.txt " + jupiter_config.WAVE_PATH + "input_node.txt")
	os.system("cp " + jupiter_config.HERE + "jupiter_config.ini "+ jupiter_config.WAVE_PATH + "jupiter_config.ini")
	os.chdir(jupiter_config.WAVE_PATH)

	# os.system("sudo docker build -f rpi_greedywave_home.Dockerfile . -t docker.io/anrg/rpi_greedywave_home:v0")
	# os.system("sudo docker push docker.io/anrg/rpi_greedywave_home:v0")
	
	# os.system("sudo docker build -f rpi_greedywave_worker.Dockerfile . -t docker.io/anrg/rpi_greedywave_worker:v0")
	# os.system("sudo docker push docker.io/anrg/rpi_greedywave_worker:v0")

	os.system("sudo docker build -f rpi_randomwave_home.Dockerfile . -t docker.io/anrg/rpi_randomwave_home:v0")
	os.system("sudo docker push docker.io/anrg/rpi_randomwave_home:v0")
	
	# os.system("sudo docker build -f rpi_randomwave_worker.Dockerfile . -t docker.io/anrg/rpi_randomwave_worker:v0")
	# os.system("sudo docker push docker.io/anrg/rpi_randomwave_worker:v0")

	os.system("rm DAG.txt")
	os.system("rm input_node.txt")
	os.system("rm jupiter_config.ini")

if __name__ == '__main__':
	# build_push_rpis_circe()
	# build_push_rpis_exec()
	# build_push_rpis_heft()
	# build_push_rpis_netr()
	build_push_rpis_wave()