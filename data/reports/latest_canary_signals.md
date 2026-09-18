# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T01:37:28.779340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0409` n `12`; crypto_alt avg `0.1811` n `234`; crypto_major avg `0.0972` n `8`; equity avg `-0.0241` n `140`; fx avg `0.0128` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0449` n `20`; unknown avg `-0.0097` n `919`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `0.608` n `234`; crypto_major avg `0.5823` n `8`; equity avg `-0.0992` n `140`; fx avg `0.018` n `6`; index avg `-0.0414` n `26`; metal avg `0.0211` n `20`; unknown avg `0.8195` n `917`
- 4h: commodity avg `-0.0545` n `12`; crypto_alt avg `1.2279` n `234`; crypto_major avg `0.8958` n `8`; equity avg `-0.2635` n `140`; fx avg `0.0934` n `6`; index avg `-0.1138` n `26`; metal avg `0.1622` n `20`; unknown avg `-0.1375` n `845`
- 24h: commodity avg `-0.2962` n `12`; crypto_alt avg `3.4183` n `234`; crypto_major avg `1.8773` n `8`; equity avg `1.1884` n `138`; fx avg `0.0813` n `6`; index avg `0.1396` n `26`; metal avg `0.3121` n `20`; unknown avg `1.8352` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
