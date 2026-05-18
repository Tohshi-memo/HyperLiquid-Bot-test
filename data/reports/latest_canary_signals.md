# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T19:22:20.875948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1922` n `12`; crypto_alt avg `0.122` n `228`; crypto_major avg `0.0732` n `8`; equity avg `0.0721` n `66`; fx avg `-0.0291` n `6`; index avg `0.0038` n `23`; metal avg `-0.1016` n `18`; unknown avg `-0.2281` n `383`
- 1h: commodity avg `-0.6741` n `12`; crypto_alt avg `0.6845` n `228`; crypto_major avg `0.5414` n `8`; equity avg `0.291` n `66`; fx avg `0.0049` n `6`; index avg `0.1625` n `23`; metal avg `0.3522` n `18`; unknown avg `0.4643` n `383`
- 4h: commodity avg `-0.0721` n `12`; crypto_alt avg `0.616` n `228`; crypto_major avg `0.7619` n `8`; equity avg `-0.2638` n `66`; fx avg `0.1387` n `6`; index avg `-0.1897` n `23`; metal avg `0.4113` n `18`; unknown avg `0.1538` n `383`
- 24h: commodity avg `0.6881` n `12`; crypto_alt avg `-2.3733` n `228`; crypto_major avg `-2.4684` n `8`; equity avg `-1.3219` n `66`; fx avg `0.1715` n `6`; index avg `-0.62` n `23`; metal avg `0.8021` n `18`; unknown avg `-0.7022` n `362`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
