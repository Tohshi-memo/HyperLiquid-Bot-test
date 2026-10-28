# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T08:37:32.599484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.2616` n `238`; crypto_major avg `0.4064` n `8`; equity avg `-0.0383` n `154`; fx avg `0.0046` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0094` n `20`; unknown avg `84.1412` n `1234`
- 1h: commodity avg `-0.1065` n `13`; crypto_alt avg `0.4968` n `238`; crypto_major avg `0.7949` n `8`; equity avg `0.044` n `154`; fx avg `0.0388` n `6`; index avg `-0.0122` n `27`; metal avg `0.0501` n `20`; unknown avg `80.4233` n `1210`
- 4h: commodity avg `-0.0009` n `13`; crypto_alt avg `0.2439` n `238`; crypto_major avg `0.6165` n `8`; equity avg `0.3256` n `154`; fx avg `-0.0287` n `6`; index avg `0.0492` n `27`; metal avg `0.0258` n `20`; unknown avg `8.8738` n `1194`
- 24h: commodity avg `-0.3025` n `13`; crypto_alt avg `2.2364` n `238`; crypto_major avg `2.7498` n `8`; equity avg `3.9538` n `154`; fx avg `0.0862` n `6`; index avg `0.5529` n `27`; metal avg `0.4543` n `20`; unknown avg `16.7656` n `1026`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
