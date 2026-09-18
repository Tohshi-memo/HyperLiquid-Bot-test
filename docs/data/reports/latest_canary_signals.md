# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T01:07:29.942507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.1544` n `234`; crypto_major avg `0.3088` n `8`; equity avg `0.0721` n `140`; fx avg `0.0024` n `6`; index avg `0.0105` n `26`; metal avg `0.0521` n `20`; unknown avg `0.1001` n `917`
- 1h: commodity avg `0.0001` n `12`; crypto_alt avg `0.3468` n `234`; crypto_major avg `0.33` n `8`; equity avg `-0.0293` n `140`; fx avg `0.0236` n `6`; index avg `0.004` n `26`; metal avg `0.1529` n `20`; unknown avg `-0.0927` n `911`
- 4h: commodity avg `-0.0457` n `12`; crypto_alt avg `1.0765` n `234`; crypto_major avg `0.7674` n `8`; equity avg `-0.1404` n `140`; fx avg `0.0753` n `6`; index avg `-0.0827` n `26`; metal avg `0.1885` n `20`; unknown avg `-0.1102` n `837`
- 24h: commodity avg `-0.1233` n `12`; crypto_alt avg `3.6275` n `234`; crypto_major avg `2.3312` n `8`; equity avg `1.427` n `138`; fx avg `0.0517` n `6`; index avg `0.1717` n `26`; metal avg `0.4453` n `20`; unknown avg `1.7232` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
