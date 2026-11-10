# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T05:22:32.183361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0446` n `13`; crypto_alt avg `-0.0871` n `239`; crypto_major avg `0.037` n `8`; equity avg `0.2107` n `160`; fx avg `-0.0338` n `6`; index avg `0.0482` n `27`; metal avg `0.0702` n `20`; unknown avg `-0.1326` n `1257`
- 1h: commodity avg `-0.0072` n `13`; crypto_alt avg `0.0978` n `239`; crypto_major avg `0.2433` n `8`; equity avg `0.3333` n `160`; fx avg `-0.0345` n `6`; index avg `0.0689` n `27`; metal avg `0.0628` n `20`; unknown avg `-0.3448` n `1249`
- 4h: commodity avg `-0.109` n `13`; crypto_alt avg `0.173` n `239`; crypto_major avg `-0.1906` n `8`; equity avg `0.1155` n `160`; fx avg `-0.0342` n `6`; index avg `0.0267` n `27`; metal avg `-0.0542` n `20`; unknown avg `0.0873` n `1235`
- 24h: commodity avg `-0.614` n `13`; crypto_alt avg `1.301` n `239`; crypto_major avg `0.0433` n `8`; equity avg `3.9075` n `160`; fx avg `0.0093` n `6`; index avg `0.4083` n `27`; metal avg `0.1315` n `20`; unknown avg `189.3184` n `1067`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
