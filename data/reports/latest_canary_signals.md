# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T10:37:30.590605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `12`; crypto_alt avg `0.1911` n `234`; crypto_major avg `0.2536` n `8`; equity avg `0.077` n `140`; fx avg `-0.0106` n `6`; index avg `0.024` n `26`; metal avg `0.01` n `20`; unknown avg `-0.1614` n `925`
- 1h: commodity avg `-0.0154` n `12`; crypto_alt avg `0.5762` n `234`; crypto_major avg `0.5932` n `8`; equity avg `0.1375` n `140`; fx avg `-0.0265` n `6`; index avg `0.0159` n `26`; metal avg `-0.0317` n `20`; unknown avg `-0.2027` n `923`
- 4h: commodity avg `0.0781` n `12`; crypto_alt avg `1.43` n `234`; crypto_major avg `1.2607` n `8`; equity avg `0.0203` n `140`; fx avg `0.0806` n `6`; index avg `-0.0127` n `26`; metal avg `0.0306` n `20`; unknown avg `0.8097` n `917`
- 24h: commodity avg `-0.1537` n `12`; crypto_alt avg `6.3465` n `234`; crypto_major avg `5.0531` n `8`; equity avg `1.757` n `140`; fx avg `0.1745` n `6`; index avg `0.235` n `26`; metal avg `0.6517` n `20`; unknown avg `2.6953` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
