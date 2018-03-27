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
	os.chdir(jupiter_config.WAVE_PATH)

	os.system("sudo docker build -f home.Dockerfile . -t docker.io/anrg/rpi_wave_home:v0")
	os.system("sudo docker push docker.io/anrg/rpi_wave_home:v0")
	
	os.system("sudo docker build -f worker.Dockerfile . -t docker.io/anrg/rpi_wave_worker:v0")
	os.system("sudo docker push docker.io/anrg/rpi_wave_worker:v0")

if __name__ == '__main__':
	build_push_rpis_circe()
	# build_push_rpis_exec()
	# build_push_rpis_heft()
	# build_push_rpis_netr()
	# build_push_rpis_wave()