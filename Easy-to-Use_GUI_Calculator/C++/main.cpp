#include <iostream>
#include <string>
using namespace std;
int main(){
    cout << "Please input your name." << endl;
    string ipt1;
    cin >> ipt1;
    cout << "Hello, " << ipt1 << ". what do you want to do?"<<endl;
    cout << " 1:Mode 1 2:Mode 2" << endl;
    string ipt2;
    cin >> ipt2;
    if(ipt2 == "1") cout << "Mode 1 selected." << endl;
    else if (ipt2 == "2") cout << "Mode 2 selected." << endl;
}