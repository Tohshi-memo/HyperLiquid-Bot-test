# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T01:22:22.787650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.8721` n `228`; crypto_major avg `0.9126` n `8`; equity avg `0.251` n `74`; fx avg `0.0008` n `6`; index avg `0.045` n `23`; metal avg `0.0831` n `18`; unknown avg `0.7207` n `516`
- 1h: commodity avg `0.0438` n `12`; crypto_alt avg `1.5916` n `228`; crypto_major avg `1.5157` n `8`; equity avg `0.3253` n `74`; fx avg `0.0018` n `6`; index avg `-0.0069` n `23`; metal avg `0.0881` n `18`; unknown avg `0.4614` n `516`
- 4h: commodity avg `0.0692` n `12`; crypto_alt avg `2.1471` n `228`; crypto_major avg `1.53` n `8`; equity avg `0.5167` n `74`; fx avg `-0.0256` n `6`; index avg `-0.0435` n `23`; metal avg `0.1536` n `18`; unknown avg `0.5275` n `515`
- 24h: commodity avg `0.1377` n `12`; crypto_alt avg `0.6511` n `228`; crypto_major avg `0.178` n `8`; equity avg `0.2243` n `74`; fx avg `0.0241` n `6`; index avg `-0.0395` n `23`; metal avg `-0.2677` n `18`; unknown avg `-0.0958` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
