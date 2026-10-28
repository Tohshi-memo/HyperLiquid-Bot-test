# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T19:23:02.774869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.026` n `13`; crypto_alt avg `0.1722` n `238`; crypto_major avg `0.0265` n `8`; equity avg `-0.0665` n `155`; fx avg `-0.0004` n `6`; index avg `0.0119` n `27`; metal avg `0.0583` n `20`; unknown avg `183.2493` n `1238`
- 1h: commodity avg `-0.0956` n `13`; crypto_alt avg `0.9781` n `238`; crypto_major avg `0.5524` n `8`; equity avg `0.5389` n `155`; fx avg `0.0037` n `6`; index avg `0.0621` n `27`; metal avg `0.1517` n `20`; unknown avg `4.1228` n `1232`
- 4h: commodity avg `-0.0332` n `13`; crypto_alt avg `0.645` n `238`; crypto_major avg `0.6449` n `8`; equity avg `0.4444` n `155`; fx avg `0.0213` n `6`; index avg `0.0093` n `27`; metal avg `0.0421` n `20`; unknown avg `4.2761` n `1226`
- 24h: commodity avg `0.4838` n `13`; crypto_alt avg `0.5278` n `238`; crypto_major avg `0.5434` n `8`; equity avg `1.4359` n `154`; fx avg `0.2353` n `6`; index avg `0.2502` n `27`; metal avg `-0.1127` n `20`; unknown avg `6.5502` n `1100`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
