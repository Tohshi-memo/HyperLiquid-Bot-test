# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T11:37:17.530805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2649` n `12`; crypto_alt avg `0.1434` n `228`; crypto_major avg `0.1028` n `8`; equity avg `0.1213` n `66`; fx avg `0.0102` n `5`; index avg `0.0186` n `23`; metal avg `0.3179` n `18`; unknown avg `-0.0258` n `383`
- 1h: commodity avg `-0.3004` n `12`; crypto_alt avg `0.2313` n `228`; crypto_major avg `-0.0114` n `8`; equity avg `-0.0073` n `66`; fx avg `0.0056` n `5`; index avg `-0.0917` n `23`; metal avg `0.3119` n `18`; unknown avg `-0.0322` n `383`
- 4h: commodity avg `0.0651` n `12`; crypto_alt avg `-0.1301` n `228`; crypto_major avg `-0.16` n `8`; equity avg `0.0237` n `66`; fx avg `0.072` n `5`; index avg `-0.0773` n `23`; metal avg `0.007` n `18`; unknown avg `-0.577` n `383`
- 24h: commodity avg `0.5896` n `12`; crypto_alt avg `-3.0079` n `228`; crypto_major avg `-1.8695` n `8`; equity avg `-0.1741` n `65`; fx avg `0.1007` n `5`; index avg `-0.0918` n `23`; metal avg `0.2069` n `18`; unknown avg `-0.6495` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
