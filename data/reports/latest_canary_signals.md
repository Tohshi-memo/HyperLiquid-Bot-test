# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T00:07:34.339781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.0792` n `230`; crypto_major avg `-0.0209` n `8`; equity avg `0.066` n `102`; fx avg `0.0844` n `6`; index avg `0.1042` n `25`; metal avg `-0.0215` n `20`; unknown avg `-0.0667` n `779`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `-0.0885` n `230`; crypto_major avg `-0.2372` n `8`; equity avg `0.3158` n `102`; fx avg `0.1233` n `6`; index avg `0.1409` n `25`; metal avg `-0.0387` n `20`; unknown avg `0.0054` n `779`
- 4h: commodity avg `0.0691` n `12`; crypto_alt avg `-0.2008` n `230`; crypto_major avg `-0.1227` n `8`; equity avg `0.9649` n `102`; fx avg `0.1284` n `6`; index avg `0.1583` n `25`; metal avg `-0.0571` n `20`; unknown avg `-0.3661` n `779`
- 24h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.6787` n `230`; crypto_major avg `1.3188` n `8`; equity avg `7.5677` n `102`; fx avg `-0.2618` n `6`; index avg `0.979` n `25`; metal avg `0.482` n `20`; unknown avg `0.0346` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
