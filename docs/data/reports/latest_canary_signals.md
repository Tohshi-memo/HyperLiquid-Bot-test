# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T17:37:31.013613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `-0.0074` n `229`; crypto_major avg `-0.0377` n `8`; equity avg `0.0626` n `92`; fx avg `-0.0098` n `6`; index avg `0.0377` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0143` n `765`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `0.1712` n `229`; crypto_major avg `0.073` n `8`; equity avg `0.0968` n `92`; fx avg `-0.0173` n `6`; index avg `0.0409` n `25`; metal avg `-0.0632` n `20`; unknown avg `-0.001` n `765`
- 4h: commodity avg `-0.1103` n `12`; crypto_alt avg `-0.3101` n `229`; crypto_major avg `-0.6771` n `8`; equity avg `-0.0426` n `92`; fx avg `-0.0605` n `6`; index avg `0.1332` n `25`; metal avg `0.079` n `20`; unknown avg `-0.097` n `765`
- 24h: commodity avg `-0.206` n `12`; crypto_alt avg `0.9522` n `229`; crypto_major avg `1.005` n `8`; equity avg `-0.8296` n `92`; fx avg `-0.1791` n `6`; index avg `0.022` n `25`; metal avg `-0.1811` n `20`; unknown avg `-0.0951` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
