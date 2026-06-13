# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T02:07:28.970347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0507` n `12`; crypto_alt avg `-0.0423` n `228`; crypto_major avg `-0.0551` n `8`; equity avg `0.0605` n `74`; fx avg `-0.0001` n `6`; index avg `0.0825` n `23`; metal avg `-0.0175` n `18`; unknown avg `0.0046` n `643`
- 1h: commodity avg `0.0363` n `12`; crypto_alt avg `0.446` n `228`; crypto_major avg `0.2168` n `8`; equity avg `0.0976` n `74`; fx avg `0.0241` n `6`; index avg `0.1446` n `23`; metal avg `-0.0157` n `18`; unknown avg `-0.4308` n `643`
- 4h: commodity avg `-0.079` n `12`; crypto_alt avg `1.0322` n `228`; crypto_major avg `0.1624` n `8`; equity avg `0.1921` n `74`; fx avg `0.0676` n `6`; index avg `0.1425` n `23`; metal avg `0.0703` n `18`; unknown avg `-0.5034` n `643`
- 24h: commodity avg `-0.6142` n `12`; crypto_alt avg `0.5649` n `228`; crypto_major avg `0.449` n `8`; equity avg `-0.5265` n `74`; fx avg `0.0083` n `6`; index avg `0.5515` n `23`; metal avg `0.459` n `18`; unknown avg `40.6196` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
