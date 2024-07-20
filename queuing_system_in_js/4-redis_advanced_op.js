import redis from "redis";
const client = redis.createClient()

client.on("connect", function() {
    console.log("Redis client connect to the server");
});

client.on("error", function (error) {
    console.log("Redis client not connect to the server:" + error.message)
});

client.hSet("HolbertonSchools","Portland","50")
client.hSet("HolbertonSchools","Seattle","80")
client.hSet("HolbertonSchools","New York","20")
client.hSet("HolbertonSchools","Bogota","20")
client.hSet("HolbertonSchools","Cali","40")
client.hSet("HolbertonSchools","Paris","2")

client.hGetAll("HolbertonSchools",(err,result) => {
    if (err){
        console.error();(err);
        return
    }
    console.log(result);
})

