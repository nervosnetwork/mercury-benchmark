wrk.method = "POST"
wrk.body   = "{\"jsonrpc\":\"2.0\",\"method\":\"build_deposit_transaction\",\"params\":[{\"from\":{\"items\":[{\"Address\":\"ckt1qyqzqfj8lmx9h8vvhk62uut8us844v0yh2hsnqvvgc\"}],\"source\":\"Free\"},\"amount\":30000000000,\"fee_rate\":1000}],\"amount\":100,\"fee_rate\":1000}],\"id\":100}"
wrk.headers["Content-Type"] = "application/json"