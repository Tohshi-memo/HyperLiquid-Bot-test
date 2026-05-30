# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T21:52:18.385315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `-0.0659` n `228`; crypto_major avg `-0.0953` n `8`; equity avg `-0.0083` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0133` n `23`; metal avg `0.0203` n `18`; unknown avg `0.1846` n `421`
- 1h: commodity avg `0.1626` n `12`; crypto_alt avg `0.0301` n `228`; crypto_major avg `0.0959` n `8`; equity avg `0.0586` n `69`; fx avg `-0.0017` n `6`; index avg `-0.0003` n `23`; metal avg `0.0145` n `18`; unknown avg `0.1716` n `421`
- 4h: commodity avg `0.186` n `12`; crypto_alt avg `0.3731` n `228`; crypto_major avg `0.0601` n `8`; equity avg `0.2936` n `69`; fx avg `0.0056` n `6`; index avg `-0.0148` n `23`; metal avg `-0.0` n `18`; unknown avg `-0.0211` n `421`
- 24h: commodity avg `0.0815` n `12`; crypto_alt avg `1.9262` n `228`; crypto_major avg `2.9377` n `8`; equity avg `1.0814` n `69`; fx avg `0.0312` n `6`; index avg `0.0463` n `23`; metal avg `0.1283` n `18`; unknown avg `0.4391` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
