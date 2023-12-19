#include <iostream>
#include <tuple>
#include<utility>
using namespace std;
int main(){
    tuple <int,string> tupa(1,"andre");
    pair<decltype(tupa),string>par{tupa,get<1>(tupa)};
    auto [primeiro,segundo]=par;
    auto[first,second]=primeiro;
    cout<<first<<" "<<second;
    
}