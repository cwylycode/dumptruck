#include "asciibox.h"
#include <iostream>
#include <unistd.h>
using namespace std;

void _ascii_box_draw(int dimensions)
{
	for(int y = 0; y < dimensions; y++)
	{
		char line[dimensions+1];
		for(int x = 0; x < dimensions; x++)
		{
			if(y == 0 || y == dimensions-1) line[x] = '#';
			else if(x > 0 && x < dimensions-1) line[x] = ' ';
			else line[x] = '#';
		}
		line[dimensions] = '\0';
		cout<<line<<endl;
	}
}

void ascii_box_play(int loops, int size_min, int size_max, float speed)
{
	int i = 0;
	while(++i < loops+1)
	{
		for(int up = size_min; up <= size_max; up++)
		{
			cout << "\x1B[2J\x1B[H";
			_ascii_box_draw(up);
			usleep(1000000/speed);
		}
		for(int down = size_max; down >= size_min; down--)
		{
			cout << "\x1B[2J\x1B[H";
 			_ascii_box_draw(down);
			usleep(1000000/speed);
		}
	}
}