# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T00:07:31.117575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.1983` n `239`; crypto_major avg `0.1204` n `8`; equity avg `0.0952` n `160`; fx avg `0.0317` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0295` n `20`; unknown avg `-0.0343` n `1251`
- 1h: commodity avg `0.0101` n `13`; crypto_alt avg `0.0451` n `239`; crypto_major avg `0.1147` n `8`; equity avg `0.2534` n `160`; fx avg `0.0403` n `6`; index avg `-0.0312` n `27`; metal avg `-0.0267` n `20`; unknown avg `0.0729` n `1249`
- 4h: commodity avg `0.0985` n `13`; crypto_alt avg `-0.4555` n `239`; crypto_major avg `0.4047` n `8`; equity avg `0.3545` n `160`; fx avg `0.0893` n `6`; index avg `0.0022` n `27`; metal avg `-0.0331` n `20`; unknown avg `-0.1062` n `1209`
- 24h: commodity avg `-0.3702` n `13`; crypto_alt avg `2.0699` n `239`; crypto_major avg `0.6033` n `8`; equity avg `5.7319` n `160`; fx avg `-0.0026` n `6`; index avg `0.6463` n `27`; metal avg `0.5392` n `20`; unknown avg `4.906` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
