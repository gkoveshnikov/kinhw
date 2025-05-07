cmake -S . -B build/Release -DCMAKE_BUILD_TYPE=Release && cmake --build build/Release/ -j && ./bin/kinhw && python ./scripts/graph.py ./output/data.csv
