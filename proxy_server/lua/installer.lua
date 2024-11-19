SERVER_ADDRESS = "{SERVER_ADDRESS}"

local runner = http.get(SERVER_ADDRESS.."/get_runner").readAll()
if fs.exists("runner")
then
    fs.delete("runner")
end

local file = fs.open("runner", "w")
file.write(runner)
file.close()
