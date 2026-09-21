# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T00:07:26.549382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `0.386` n `234`; crypto_major avg `0.3938` n `8`; equity avg `0.1962` n `140`; fx avg `-0.0077` n `6`; index avg `0.0474` n `26`; metal avg `0.0123` n `20`; unknown avg `16.4042` n `935`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `0.6359` n `234`; crypto_major avg `0.642` n `8`; equity avg `0.2913` n `140`; fx avg `-0.0215` n `6`; index avg `0.0479` n `26`; metal avg `0.0065` n `20`; unknown avg `35.9807` n `935`
- 4h: commodity avg `-0.3701` n `12`; crypto_alt avg `0.6518` n `234`; crypto_major avg `0.7185` n `8`; equity avg `0.6912` n `140`; fx avg `0.0345` n `6`; index avg `0.157` n `26`; metal avg `0.0599` n `20`; unknown avg `1.6684` n `853`
- 24h: commodity avg `-0.1357` n `12`; crypto_alt avg `1.3879` n `234`; crypto_major avg `0.9992` n `8`; equity avg `0.5967` n `140`; fx avg `0.0414` n `6`; index avg `0.1086` n `26`; metal avg `0.0277` n `20`; unknown avg `3.5075` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
