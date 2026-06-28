# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T22:07:32.985095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2345` n `12`; crypto_alt avg `0.8641` n `228`; crypto_major avg `0.8576` n `8`; equity avg `0.169` n `88`; fx avg `0.0132` n `6`; index avg `0.0614` n `23`; metal avg `0.0624` n `20`; unknown avg `0.2238` n `764`
- 1h: commodity avg `-0.1994` n `12`; crypto_alt avg `0.1531` n `228`; crypto_major avg `0.319` n `8`; equity avg `0.1228` n `88`; fx avg `-0.0153` n `6`; index avg `0.0677` n `23`; metal avg `0.0312` n `20`; unknown avg `-0.1827` n `764`
- 4h: commodity avg `-0.4211` n `12`; crypto_alt avg `-0.1828` n `228`; crypto_major avg `-0.015` n `8`; equity avg `0.2406` n `88`; fx avg `-0.0592` n `6`; index avg `0.1286` n `23`; metal avg `0.0702` n `20`; unknown avg `0.5641` n `764`
- 24h: commodity avg `-0.2244` n `12`; crypto_alt avg `-0.0327` n `228`; crypto_major avg `-0.3298` n `8`; equity avg `0.404` n `88`; fx avg `-0.0795` n `6`; index avg `0.1323` n `23`; metal avg `0.0686` n `20`; unknown avg `15.1454` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
