# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T07:22:27.225060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0402` n `13`; crypto_alt avg `0.0423` n `237`; crypto_major avg `-0.0649` n `8`; equity avg `-0.0096` n `152`; fx avg `0.0009` n `6`; index avg `0.0093` n `26`; metal avg `0.0013` n `20`; unknown avg `0.0047` n `1240`
- 1h: commodity avg `0.088` n `13`; crypto_alt avg `-0.1287` n `237`; crypto_major avg `-0.0676` n `8`; equity avg `-0.0874` n `152`; fx avg `-0.027` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0258` n `20`; unknown avg `-0.0398` n `1238`
- 4h: commodity avg `0.1216` n `13`; crypto_alt avg `0.218` n `237`; crypto_major avg `0.3831` n `8`; equity avg `0.0762` n `152`; fx avg `0.0126` n `6`; index avg `-0.006` n `26`; metal avg `-0.1439` n `20`; unknown avg `0.2751` n `1200`
- 24h: commodity avg `-0.5924` n `13`; crypto_alt avg `-0.5716` n `237`; crypto_major avg `-0.485` n `8`; equity avg `-0.5437` n `152`; fx avg `0.0418` n `6`; index avg `-0.0362` n `26`; metal avg `0.0817` n `20`; unknown avg `0.1583` n `985`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2524`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
