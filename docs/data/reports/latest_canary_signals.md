# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T01:22:29.747655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.326` n `13`; crypto_alt avg `0.233` n `234`; crypto_major avg `0.1479` n `8`; equity avg `0.0409` n `142`; fx avg `0.005` n `6`; index avg `0.0026` n `26`; metal avg `0.0619` n `20`; unknown avg `0.0534` n `974`
- 1h: commodity avg `-0.4124` n `13`; crypto_alt avg `0.4981` n `234`; crypto_major avg `0.1737` n `8`; equity avg `0.1896` n `142`; fx avg `0.0618` n `6`; index avg `0.0645` n `26`; metal avg `0.1606` n `20`; unknown avg `2.4829` n `956`
- 4h: commodity avg `-0.3915` n `13`; crypto_alt avg `0.9696` n `234`; crypto_major avg `0.1153` n `8`; equity avg `0.3818` n `142`; fx avg `0.0952` n `6`; index avg `0.1264` n `26`; metal avg `0.0138` n `20`; unknown avg `0.6494` n `942`
- 24h: commodity avg `-0.2686` n `13`; crypto_alt avg `0.6312` n `234`; crypto_major avg `0.8394` n `8`; equity avg `-0.1418` n `142`; fx avg `0.1928` n `6`; index avg `0.0545` n `26`; metal avg `-0.1134` n `20`; unknown avg `778.6197` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
