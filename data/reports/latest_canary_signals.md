# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T17:07:44.856785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `13`; crypto_alt avg `0.1838` n `238`; crypto_major avg `0.1775` n `8`; equity avg `0.0874` n `154`; fx avg `0.0003` n `6`; index avg `-0.0084` n `27`; metal avg `0.0291` n `20`; unknown avg `0.0824` n `1232`
- 1h: commodity avg `-0.0307` n `13`; crypto_alt avg `0.1501` n `238`; crypto_major avg `0.2904` n `8`; equity avg `-0.021` n `154`; fx avg `0.0036` n `6`; index avg `-0.0357` n `27`; metal avg `0.0122` n `20`; unknown avg `1.1409` n `1232`
- 4h: commodity avg `-0.2365` n `13`; crypto_alt avg `0.9082` n `238`; crypto_major avg `0.9433` n `8`; equity avg `1.4507` n `154`; fx avg `-0.038` n `6`; index avg `0.1735` n `27`; metal avg `0.2941` n `20`; unknown avg `0.8289` n `1150`
- 24h: commodity avg `-0.6161` n `13`; crypto_alt avg `0.2772` n `237`; crypto_major avg `0.8175` n `8`; equity avg `1.3998` n `154`; fx avg `-0.0522` n `6`; index avg `0.3635` n `27`; metal avg `0.0599` n `20`; unknown avg `34.8931` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2255`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2016`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
