import { createClient } from "redis";

const client = createClient()

client.on("connect", function() {
    console.log("Redis client connect to the server");
});

client.on("error", function (error) {
    console.log("Redis client not connect to the server:" + error.message)
});