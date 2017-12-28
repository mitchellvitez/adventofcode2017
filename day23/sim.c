#include <stdio.h>

int main() {
	int a = 1;
	int b = 0;
	int c = 0;
	int d = 0;
	int e = 0;
	int f = 0;
	int g = 0;
	int h = 0;
	
	b = 107900;
	c = b + 17000;
	do {
		f = 1;
		d = 2;
		



		d -= 1;
		g += 1;
		do {
			e = 2;



			do {
				g = d * e - b;
				if (g == 0) {
					f = 0;
				}
				e -= 1;
				g = e - b;
			} while (g != 0);



			d -= 1;
			g = d - b;

			printf("%d\n", d);
			printf("%d\n", e);
			printf("%d\n", g);
		} while (g != 0);




		if (f == 0) {
			h += 1;
			/* printf("%d\n", h); */
		}
		g = b;
		g -= c;
		b += 17;
	} while (g != 0);
	printf("%d\n", h);
}
