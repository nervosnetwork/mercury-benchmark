wrk.method = "POST"
wrk.body   = "{\"jsonrpc\":\"2.0\",\"method\":\"get_balance\",\"params\":[{\"udt_hashes\":[],\"address\":{\"KeyAddress\":\"ckt1qyqg88ccqm59ksxp85788pnqg4rkejdgcg2qxcu2qf\"}}],\"id\":100}"
wrk.headers["Content-Type"] = "application/json"