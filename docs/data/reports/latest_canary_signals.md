# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T22:07:28.324327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `0.0916` n `237`; crypto_major avg `0.1042` n `8`; equity avg `-0.0123` n `152`; fx avg `-0.0012` n `6`; index avg `0.0047` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.0506` n `1203`
- 1h: commodity avg `0.0015` n `13`; crypto_alt avg `0.1762` n `237`; crypto_major avg `0.1265` n `8`; equity avg `0.0259` n `152`; fx avg `-0.0085` n `6`; index avg `0.0106` n `26`; metal avg `-0.011` n `20`; unknown avg `0.0922` n `1159`
- 4h: commodity avg `-0.0954` n `13`; crypto_alt avg `0.905` n `237`; crypto_major avg `0.7` n `8`; equity avg `0.2844` n `152`; fx avg `-0.0071` n `6`; index avg `0.0511` n `26`; metal avg `0.012` n `20`; unknown avg `0.9499` n `1135`
- 24h: commodity avg `-0.0491` n `13`; crypto_alt avg `-2.2206` n `237`; crypto_major avg `-1.6149` n `8`; equity avg `-0.285` n `152`; fx avg `-0.042` n `6`; index avg `-0.034` n `26`; metal avg `-0.1611` n `20`; unknown avg `-0.3488` n `1062`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
