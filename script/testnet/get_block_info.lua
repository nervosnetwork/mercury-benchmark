wrk.method = "POST"
wrk.body   = "{\"jsonrpc\":\"2.0\",\"method\":\"get_block_info\",\"params\":[{\"block_number\":2172093}],\"id\":100}"
wrk.headers["Content-Type"] = "application/json"

