import redis from "redis"
import { promisify } from "util";
const client = redis.createClient()

client.on("connect", function() {
    console.log("Redis client connect to the server");
});

client.on("error", function (error) {
    console.log("Redis client not connect to the server:" + error.message)
});

function setNewSchool(schoolName, value) {
    client.set(schoolName,value, redis.print)
}
const getAsyncName = promisify(client.get).bind(client)
async function displaySchoolValue(schoolName) {
    
    try {
        const value = await  getAsyncName(schoolName);
        console.log(value);
    } catch (error) {
        console.log(`Error get value ${error}`);
    }
}