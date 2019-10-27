curl -XGET "http://localhost:9200/_cat/indices?pretty&h=index,health,store.size,pri,rep"

cmd=$(curl -XGET "http://localhost:9200/_cat/indices?pretty&h=index,health,store.size,pri,rep")

result='$cmd'

echo $result



#cmd=$(curl -XGET "http://localhost:9200/_cat/indices?pretty&h=index,health,store.size,pri,rep")

# -s disables status
# -f causes a non-zero return code for 400/500 response codes
cmd=$(curl -sf -XGET "http://localhost:9200/_cat/indices?pretty&h=index,health,store.size,pri,rep")

result=$cmd

echo $result

#for line in result:
  #echo $line

