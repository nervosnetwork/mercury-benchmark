wrk.method = "POST"
wrk.body   = "{\"jsonrpc\":\"2.0\",\"method\":\"get_generic_block\",\"params\":[{\"block_num\":2172093,\"block_hash\":\"0xee8adba356105149cb9dc1cb0d09430a6bd01182868787ace587961c0d64e742\"}],\"id\":100}"
wrk.headers["Content-Type"] = "application/json"

