# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T04:52:27.682149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `13`; crypto_alt avg `0.0491` n `239`; crypto_major avg `0.0524` n `8`; equity avg `0.0565` n `160`; fx avg `0.0025` n `6`; index avg `0.0154` n `27`; metal avg `-0.034` n `20`; unknown avg `18.9654` n `1259`
- 1h: commodity avg `0.0314` n `13`; crypto_alt avg `0.4215` n `239`; crypto_major avg `0.2497` n `8`; equity avg `0.3843` n `160`; fx avg `0.0038` n `6`; index avg `0.0365` n `27`; metal avg `0.0607` n `20`; unknown avg `0.3151` n `1243`
- 4h: commodity avg `-0.2138` n `13`; crypto_alt avg `0.1179` n `239`; crypto_major avg `-0.2868` n `8`; equity avg `-0.1503` n `160`; fx avg `-0.0011` n `6`; index avg `-0.0264` n `27`; metal avg `0.0327` n `20`; unknown avg `-0.124` n `1237`
- 24h: commodity avg `-0.8118` n `13`; crypto_alt avg `0.9197` n `239`; crypto_major avg `-0.4326` n `8`; equity avg `3.4479` n `160`; fx avg `0.0237` n `6`; index avg `0.329` n `27`; metal avg `0.0475` n `20`; unknown avg `188.5667` n `1071`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
