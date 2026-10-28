# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T01:40:01.893753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.012` n `13`; crypto_alt avg `0.1067` n `238`; crypto_major avg `0.1894` n `8`; equity avg `0.0188` n `154`; fx avg `0.0409` n `6`; index avg `0.0094` n `27`; metal avg `-0.0211` n `20`; unknown avg `3.1634` n `1236`
- 1h: commodity avg `0.0995` n `13`; crypto_alt avg `0.3909` n `238`; crypto_major avg `0.4183` n `8`; equity avg `0.5546` n `154`; fx avg `0.0674` n `6`; index avg `0.1145` n `27`; metal avg `-0.0093` n `20`; unknown avg `2.6559` n `1232`
- 4h: commodity avg `0.1433` n `13`; crypto_alt avg `0.0342` n `238`; crypto_major avg `0.0127` n `8`; equity avg `0.6912` n `154`; fx avg `0.1165` n `6`; index avg `0.1506` n `27`; metal avg `-0.0352` n `20`; unknown avg `4.4549` n `1212`
- 24h: commodity avg `0.0491` n `13`; crypto_alt avg `1.5791` n `237`; crypto_major avg `1.4891` n `8`; equity avg `1.7656` n `154`; fx avg `0.071` n `6`; index avg `0.4116` n `27`; metal avg `0.2031` n `20`; unknown avg `355.7136` n `1028`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
