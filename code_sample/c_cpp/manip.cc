#include <stdio.h>
#include <unistd.h>

//$B4X@a3Q$r%^%K%T%e%l!<%?$KAw$k4X?t(B
//$B0z?t(B: $B3F4X@a3Q$H(Bwait$B!J(Bms$B!K(B
void sendAngles(int j1,int j2,int j3,int j5,int j6,double wait)
{
	FILE *manip = fopen("/run/shm/angles","w");
	if(manip == NULL)
		return;
	fprintf(manip,"%d,%d,%d,%d,%d\n",j1,j2,j3,j5,j6);
	fclose(manip);
	usleep((int)(wait*1000));
}

int main(int argc, char const* argv[])
{
	for(int i=0;i<10;i++){
		if(i%2){
			sendAngles(45,45,45,45,45,3000.0);
		}else{
			sendAngles(0,0,0,0,0,3000.0);
		}
	}

	return 0;
}
