#include <bits/stdc++.h>
#include <cstdio>
#include <chrono>
#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main(){
	ofstream myFile;
	myFile.open("output.csv");
	srand(time(0));
    int p[2][10];
    for (int i=1;i<=10;++i){
    	myFile<< (rand()%20)+1 <<","<< (rand()%20)+1 <<endl;
    }
}