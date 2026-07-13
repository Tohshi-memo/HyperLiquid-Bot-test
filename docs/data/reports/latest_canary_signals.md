# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T00:22:28.475313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `0.1708` n `230`; crypto_major avg `0.2046` n `8`; equity avg `-0.1528` n `92`; fx avg `0.0128` n `6`; index avg `-0.0631` n `25`; metal avg `-0.0687` n `20`; unknown avg `0.1016` n `766`
- 1h: commodity avg `0.0582` n `12`; crypto_alt avg `0.9653` n `230`; crypto_major avg `1.0696` n `8`; equity avg `0.171` n `92`; fx avg `0.0378` n `6`; index avg `0.0127` n `25`; metal avg `0.1234` n `20`; unknown avg `0.2583` n `766`
- 4h: commodity avg `-0.1456` n `12`; crypto_alt avg `0.0319` n `230`; crypto_major avg `0.1697` n `8`; equity avg `-0.2581` n `92`; fx avg `-0.0066` n `6`; index avg `-0.0848` n `25`; metal avg `-0.1401` n `20`; unknown avg `-0.0226` n `765`
- 24h: commodity avg `-0.077` n `12`; crypto_alt avg `0.4201` n `230`; crypto_major avg `1.1756` n `8`; equity avg `-0.1905` n `92`; fx avg `-0.0246` n `6`; index avg `-0.0741` n `25`; metal avg `-0.2088` n `20`; unknown avg `0.4128` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
