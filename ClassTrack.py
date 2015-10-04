#!/usr/bin/env python

import sys
import array
import math
import glob
import os
class Tracker:
	space = 10;
	def __init__(self,argv,min_ex):
		space = min_ex;
		file_mod = 0;
		if len(argv) > 1 and len(argv) < 4:
			self.tmp_x = array.array('i',[0]*min_ex);	
			self.tmp_y = array.array('i',[0]*min_ex);
			self.tmp_r = array.array('i',[0]*min_ex);
		
			f = open(argv[1]);	
			self.file_mod = time.ctime(os.path.getmtime(f));
			cnt = 0;
			print "one"
			for l in f.readlines():
				x_t,y_t,r_t = l.strip().split();
				self.tmp_x[cnt] = int(x_t);
				self.tmp_y[cnt] = int(y_t);
				self.tmp_r[cnt] = int(math.floor(float(r_t)));
				cnt += 1;	
			
			self.init_x = array.array('i',[0] * cnt);
			self.init_y = array.array('i',[0] * cnt);
			self.init_r = array.array('i',[0] * cnt);
			
			self.MAP_X = array.array('i',[1] * cnt);
			self.MAP_Y = array.array('i',[1] * cnt);
			self.MAP_R = array.array('i',[1] * cnt);
			

			for i in range(0,cnt):
				self.init_x[i] = self.tmp_x[i];
				self.init_y[i] = self.tmp_y[i];
				self.init_r[i] = self.tmp_r[i];
	
			del self.tmp_x
			del self.tmp_y
			del self.tmp_r
	
		if len(argv) == 3:
			print "two"
			self.tmp_x = array.array('i',[0]*min_ex);
			self.tmp_y = array.array('i',[0]*min_ex);
			self.tmp_r = array.array('i',[0]*min_ex);

			f = open(argv[1]);
			self.file_mod = time.ctime(os.path.getmtime(f));
			cnt = 0;
			for l in f.readlines():
				x_t,y_t,r_t = l.strip().split();
				self.tmp_x = int(x_t);
				self.tmp_y = int(y_t);
				self.tmp_r = int(math.floor(float(r_t)));

			self.next_x = array.array('i',[0]*cnt);
			self.next_y = array.array('i',[0]*cnt);
			self.next_r = array.array('i',[0]*cnt);

			for i in range(0,cnt):
				self.next_x[i] = self.tmp_x[i];
				self.next_y[i] = self.tmp_y[i];
				self.next_r[i] = self.tmp_r[i];
			
			del self.tmp_x
			del self.tmp_y
			del self.tmp_r		
				
		if len(argv) > 3:
			print "initialisation went wrong, to many arguments given"
		if len(argv) == 1:
			print "nothing specified,waiting for the next val"

		def tracking(self):
		
			TMP_X = array.array('i',[0]*self.space);
			TMP_Y = array.array('i',[0]*self.space);
			TMP_R = array.array('i',[0]*self.space);
			TMP_X_MAP = array.array('i',[0]*self.space);
			TMP_Y_MAP = array.array('i',[0]*self.space);
			TMP_R_MAP = array.array('i',[0]*self.space);
			cnt = 0;
			cnt_x = 0;
			cnt_y = 0;
			cnt_z = 0;
			cnt_end_x = 0;
			cnt_end_y = 0;
			cnt_end_r = 0;
			for i in range(0,len(self.init_x)):
				for j in range(0,len(self.next_x)):
					tmp_x_map = 0;
					tmp_x_loc = array.array('i',[0]*100);
					for z in range(0,self.MAP_X[i]):
						for k in range(-1,2):
							if self.init_x[cnt_x+z] == self.next_x[j] + k:
								tmp_x_loc[tmp_x_map] = self.next_x[j];
								tmp_x_map += 1;
					if(cnt_x < len(self.init_x)):
						cnt_x += 1;
					else:
						break;

				if tmp_x_map != 0:
					for j in range(0,len(self.next_y)):
						tmp_y_map = 0;
						tmp_y_loc = array.array('i',[0]*100);
						for z in range(self.MAP_Y[i]):
							for k in range(-1,2):
								if self.init_y[cnt_y + z] == self.next_y[j] + k:
									tmp_y_loc[tmp_y_map] = self.next_y[j];
									tmp_y_map += 1;
						if(cnt_z < len(self.init_y)):
							cnt_z += 1;
						else:
							break;
				else:
					tmp_y_map = 0;

				if tmp_x_map != 0:	
					for j in range(0,len(self.next_r)):
						tmp_r_map = 0;
						tmp_r_loc = array.array('i',[0]*100);
						for z in range(self.MAP_R[i]):
							for k in range(-1,2):
								if self.init_x[i] == self.next_r[j] + k:
									tmp_r_loc[tmp_r_map] = self.next_r[j];
									tmp_r_map += 1;
						if(cnt_r < len(self.init_r)):
							cnt_r += 1;
						else:
							break;

				TMP_X_MAP[cnt] = tmp_x_map;
				TMP_Y_MAP[cnt] = tmp_y_map;		
				TMP_R_MAP[cnt] = tmp_r_map;
				
				for i in range(0,tmp_x_map):
					TMP_X[cnt +i] = tmp_x_loc[i];
					cnt_end_x +=1;
				for i in range(0,tmp_y_map):
					TMP_Y[cnt +i] = tmp_y_loc[i];
					cnt_end_y +=1;
				for i in range(0,tmp_r_map):
					TMP_R[cnt +i] = tmp_r_loc[i];
					cnt_end_r +=1;  

				cnt += 1;
			
		
			self.new_x_track = array.array('i',[0]*cnt_end_x);
			self.new_y_track = array.array('i',[0]*cnt_end_y);
			self.new_r_track = array.array('i',[0]*cnt_end_r);
		
			self.new_x_map = array.array('i',[0]*cnt_end_x);
			self.new_y_map = array.array('i',[0]*cnt_end_y);
			self.new_r_map = array.array('i',[0]*cnt_end_r);
		
			for i in range(0,cnt_end_x):
				self.new_x_track[i] = TMP_X[i];
				self.new_x_map[i] = TMP_X_MAP[i];
			for i in range(0,cnt_end_y):
				self.new_y_track[i] = TMP_Y[i];
				self.new_y_map[i] = TMP_Y_MAP[i];
			for i in range(0,cnt_end_r):
				self.new_r_track[i] = TMP_R[i];
				self.new_r_map[i] = TMP_R_MAP[i];

			
			del TMP_X_MAP
			del TMP_Y_MAP
			del TMP_R_MAP
			del TMP_X
			del TMP_Y
			del TMP_R
			del tmp_x_loc
			del tmp_y_loc
			del tmp_r_loc

			#careful! overwrites!
			def new_to_current(self):
				self.init_x.append(self.new_x_track);
				self.init_y.append(self.new_y_track);
				self.init_r.append(self.new_r_track);
				self.MAP_X.append(self.new_x_map);
				self.MAP_Y.append(self.new_y_map);
				self.MAP_R.append(self.new_r_map);
			def read_newest(self):
				
				newest = max(glob.iglob('*.txt'), key = os.path.getctime);
				print newest
				tmp_x = array.array('i',[0]*self.space);
				tmp_y = array.array('i',[0]*self.space);
				tmp_r = array.array('i',[0]*self.space);

				f = open(newest,'r');
				
				A = time.ctime(os.path.getmtime(f));
				if A != self.file_mod:
					for l in f.readlines():
						x_t,y_t,r_t = l.strip().split();
						tmp_x[cnt] = int(x_t);
						tmp_y[cnt] = int(y_t);
						tmp_r[cnt] = int(math.floor(float(r_t)));
						cnt += 1;
					self.init_x.append(tmp_x);
					self.init_y.append(tmp_y);
					self.init_r.append(tmp_r);
					
					return 1;
				else:
					return 0;
							
			def show(MAP,TRACK):
				for i in range(0,len(TRACK)):
					if MAP == 0:
						print "-1";
					else:
						for j in range(0,MAP[i]):
							print(TRACK[i + j]);
							print ","
					print "\t"
			def show_track(self):
				show(self.new_x_map,self.new_x_track);
				show(self.new_y_map,self.new_y_track);
				show(self.new_r_map,self.new_r_track);	
			def show_past(self):
				show(self.MAP_X,self.init_x);
				show(self.MAP_Y,self.init_y);
				show(self.MAP_R,self.init_r);

x = Tracker(sys.argv);
z += 1;
for z in range(0,-1):
	a = x.read_newest(x);
	if a == 1:
		x.show_track(x);
		x.new_to_current(x);
 		if(z == 100)
			break;		
