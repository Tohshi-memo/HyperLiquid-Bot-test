# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T12:22:30.563175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `13`; crypto_alt avg `-0.0305` n `237`; crypto_major avg `-0.0174` n `8`; equity avg `0.0287` n `152`; fx avg `0.0099` n `6`; index avg `-0.0054` n `26`; metal avg `0.0029` n `20`; unknown avg `0.0094` n `1240`
- 1h: commodity avg `0.0022` n `13`; crypto_alt avg `0.2412` n `237`; crypto_major avg `0.2235` n `8`; equity avg `0.8417` n `152`; fx avg `0.0105` n `6`; index avg `0.1337` n `26`; metal avg `0.0854` n `20`; unknown avg `12.5012` n `1234`
- 4h: commodity avg `0.0187` n `13`; crypto_alt avg `0.8821` n `237`; crypto_major avg `0.7311` n `8`; equity avg `1.2491` n `152`; fx avg `0.0097` n `6`; index avg `0.1707` n `26`; metal avg `0.0487` n `20`; unknown avg `1.3534` n `1234`
- 24h: commodity avg `-0.3399` n `13`; crypto_alt avg `0.3044` n `237`; crypto_major avg `0.243` n `8`; equity avg `0.2789` n `152`; fx avg `0.0461` n `6`; index avg `0.1045` n `26`; metal avg `0.2012` n `20`; unknown avg `0.0165` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2602`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
