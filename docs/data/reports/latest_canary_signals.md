# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T00:22:28.863856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `0.0204` n `239`; crypto_major avg `-0.0851` n `8`; equity avg `-0.0937` n `160`; fx avg `-0.0096` n `6`; index avg `-0.015` n `27`; metal avg `-0.0049` n `20`; unknown avg `18.954` n `1262`
- 1h: commodity avg `0.0183` n `13`; crypto_alt avg `0.3915` n `239`; crypto_major avg `0.1604` n `8`; equity avg `0.0995` n `160`; fx avg `-0.0401` n `6`; index avg `0.0214` n `27`; metal avg `0.0368` n `20`; unknown avg `19.5194` n `1250`
- 4h: commodity avg `-0.065` n `13`; crypto_alt avg `0.4903` n `239`; crypto_major avg `0.0248` n `8`; equity avg `0.7809` n `160`; fx avg `-0.0422` n `6`; index avg `0.0803` n `27`; metal avg `0.0379` n `20`; unknown avg `1.6389` n `1228`
- 24h: commodity avg `0.0644` n `13`; crypto_alt avg `-0.3491` n `239`; crypto_major avg `-2.5368` n `8`; equity avg `-1.1652` n `160`; fx avg `-0.1966` n `6`; index avg `-0.0991` n `27`; metal avg `-0.5196` n `20`; unknown avg `21.4766` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2576`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
