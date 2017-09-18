#include <vector>
#include <boost/pending/disjoint_sets.hpp>

int main()
{
	std::vector<int>  rank (100);
	std::vector<int>  parent (100);
	boost::disjoint_sets<int*,int*> ds(&rank[0], &parent[0]);
}

