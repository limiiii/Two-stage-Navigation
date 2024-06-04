#include<iostream>
#include<queue>
#include<iomanip>
#include<vector>
#include<cmath>
#include<set>
#include<unordered_map>
using namespace std;

//不同的环境，只需要修改邻接表G中的数据（单位为执行导航所需时间秒，100表示不可达）
//cliplim为网络的输出结果，通过dijkstra()执行计算各节点之间的dis矩阵、节点邻居映射哈希表、通过computeQ_getpath计算Q值并返回结果集
class Solution {
private:
    const double inf = 5000;
    //地图中各节点之间的邻接表
    vector<vector<double>> G{{0, 5, 2, 100, 100, 100, 100},
                          {5, 0, 100, 1, 6, 100, 100},
                          {2, 100, 0, 6, 100, 8, 100},
                          {100, 1, 6, 0, 1, 2, 100}, 
                          {100, 6, 100, 1, 0, 100, 7},
                          {100, 100, 8, 2, 100, 0, 3},
                          {100, 100, 100, 100, 7, 3, 0}};
    //初始化邻居字典，key表示节点，value表示与其相邻的点
    unordered_map<int, vector<int>> neighbormap;
public:
    Solution(){
        for(int i = 0; i < G.size(); i++){
            bool flag = false;
            for(int j = 0; j < G[i].size(); j++){
                if(flag == false && G[i][j] < 100 && G[i][j] != 0){
                    vector<int> tmp{j};
                    neighbormap[i] = tmp;
                    flag = true;
                }
                else if(G[i][j] < 100 && G[i][j] != 0){
                    neighbormap[i].push_back(j);
                }
                else continue;
            }
        }
        cout<<"init neighormap success!"<<endl;
        checkneighboroutput();
    }
    vector<vector<double>> dijkstra() {
        int n = G.size(); // 图的顶点数量
        vector<vector<double>> result;
        for(int source = 0; source < n; source++){
            vector<double> dist(n, inf); // 存储源点到各个顶点的最短距离
            vector<bool> visited(n, false); // 标记顶点是否被访问过
            dist[source] = 0; // 源点到自身的距离为0

            // 创建一个优先队列，按照距离的增序排列，每个元素存储顶点编号和距离
            priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> pq;
            pq.push(make_pair(0, source)); // 将源点加入优先队列

            while (!pq.empty()) {
                int u = pq.top().second;
                pq.pop();

                visited[u] = true; // 将顶点标记为已访问

                // 遍历与顶点u相邻的顶点
                for (int v = 0; v < n; ++v) {
                    if (G[u][v] != 0 && !visited[v]) {
                        double new_dist = dist[u] + G[u][v]; // u到v的距离

                        if (new_dist < dist[v]) {
                            dist[v] = new_dist; // 更新最短距离
                            pq.push(make_pair(dist[v], v)); // 将v加入优先队列
                        }
                    }
                }
            }
        result.push_back(dist);
        }
        //使用softmax对每一行进行归一化
        for(auto& row:result){
            double sumexp = 0;
            for(auto value : row){
                sumexp += value;
            }
            for(auto& value : row){
                value = -(value) / sumexp;
            }
        }
        return result;
    }
    
    vector<int> computeQ_getpath(vector<vector<double>> cliplim, vector<vector<double>> dis, int startnode){
        int n = cliplim[0].size();
        int m = dis.size();
        //n = 4, m = 7
        vector<vector<double>> Q(n + 1, vector<double>(m, -inf));
        vector<int> path(n);
        double maximun = -inf; int maxindex;
        for(int i = 0; i < m; i++){
            Q[0][i] = dis[startnode][i];
            if(maximun < dis[startnode][i]){
                maximun = dis[startnode][i];
                maxindex = i;
            }
        }
        set<int> visited;
        queue<int> que;
        for(int i = 1; i <= n; i++){
            que.push(maxindex);
            visited.insert(maxindex);
            while(!que.empty()){
                int nodev = que.front();
                que.pop();
                Q[i][nodev] = max(Q[i][nodev], Q[i - 1][nodev] + cliplim[nodev][i - 1]);
                vector<int> neighbor = neighbormap[nodev];
                for(int k = 0; k < neighbor.size(); k++){
                    Q[i][nodev] = max(Q[i][nodev], Q[i][neighbor[k]] + dis[nodev][neighbor[k]]);
                    if(visited.find(neighbor[k]) == visited.end()){
                        que.push(neighbor[k]);
                        visited.insert(neighbor[k]);
                    }
                }
            }
            maximun = -inf;
            for(int k = 0; k < m; k++){
                if(maximun < Q[i][k]){
                    maximun = Q[i][k];
                    maxindex = k;
                }
            }
            if(visited.size() == m){
                 cout<<"Q数组第"<<i<<"行计算成功！本次循环使Q取得最大值的节点为-----"<<maxindex<<endl;
                 path.push_back(maxindex);
            }
            visited.clear();
        }
        cout<<"检查计算的Q值："<<endl;
        for(int i = 0; i < Q.size(); i++){
            for(int j = 0; j < Q[0].size(); j++){
                cout<<setw(10)<< Q[i][j];
            }
            cout<<endl;
        }
        return path;
    }
    void checkneighboroutput(){
        //检查dis和heighbormap是否正确初始化
        cout<<"输出节点及其邻居："<<endl;
        for(auto iter:neighbormap){
            cout<<"key="<<iter.first<<" "<<"value=";
            for(auto it:iter.second){
                cout<<it<<" ";
            }
            cout<<endl;
        }
    }
};


int main(){
    //模拟clip网络的输出概率
    vector<vector<double>> cliplim{{0.1, 0.1, 0.05, 0.025},
                                   {0.4, 0.1, 0.05, 0.025},
                                   {0.1, 0.1, 0.1, 0.025},
                                   {0.1, 0.4, 0.05, 0.025},
                                   {0.1, 0.1, 0.6, 0.05},
                                   {0.1, 0.1, 0.05, 0.8},
                                   {0.1, 0.1, 0.1, 0.05}};
    Solution s;
    vector<vector<double>> dis = s.dijkstra();
    vector<int> path = s.computeQ_getpath(cliplim, dis, 0);

    //检查dis是否正确初始化,Q计算是否正确
    cout<<"输出距离代价矩阵："<<endl;
    for(int i = 0; i < dis.size(); i++){
        for(int j = 0; j < dis[0].size(); j++){
            cout<<setw(10)<< dis[i][j];
        }
        cout<<endl;
    }
    return 0;
}