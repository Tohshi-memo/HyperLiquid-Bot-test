# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T07:52:27.705083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `13`; crypto_alt avg `0.0028` n `239`; crypto_major avg `0.1528` n `8`; equity avg `0.0873` n `158`; fx avg `-0.0081` n `6`; index avg `0.0356` n `27`; metal avg `0.0016` n `20`; unknown avg `0.0673` n `1262`
- 1h: commodity avg `0.0107` n `13`; crypto_alt avg `0.2073` n `239`; crypto_major avg `0.2061` n `8`; equity avg `0.0936` n `158`; fx avg `0.0022` n `6`; index avg `0.04` n `27`; metal avg `0.0107` n `20`; unknown avg `163.1146` n `1254`
- 4h: commodity avg `0.0266` n `13`; crypto_alt avg `-0.0698` n `239`; crypto_major avg `0.1468` n `8`; equity avg `0.1457` n `158`; fx avg `0.0159` n `6`; index avg `0.0356` n `27`; metal avg `0.0034` n `20`; unknown avg `-0.2451` n `1208`
- 24h: commodity avg `0.1185` n `13`; crypto_alt avg `-1.7812` n `239`; crypto_major avg `-0.5991` n `8`; equity avg `0.1307` n `158`; fx avg `0.0461` n `6`; index avg `0.0677` n `27`; metal avg `-0.0369` n `20`; unknown avg `158.5987` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
