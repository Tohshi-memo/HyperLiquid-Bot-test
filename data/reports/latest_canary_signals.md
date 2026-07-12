# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T18:07:34.026347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0457` n `12`; crypto_alt avg `-0.0457` n `230`; crypto_major avg `-0.0929` n `8`; equity avg `-0.0173` n `92`; fx avg `-0.1093` n `6`; index avg `-0.0161` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0106` n `765`
- 1h: commodity avg `0.0554` n `12`; crypto_alt avg `-0.1321` n `230`; crypto_major avg `-0.1399` n `8`; equity avg `-0.0276` n `92`; fx avg `-0.0154` n `6`; index avg `-0.0191` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.0703` n `765`
- 4h: commodity avg `0.1715` n `12`; crypto_alt avg `0.0574` n `230`; crypto_major avg `0.305` n `8`; equity avg `-0.0458` n `92`; fx avg `-0.0203` n `6`; index avg `0.0148` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.0879` n `759`
- 24h: commodity avg `0.6036` n `12`; crypto_alt avg `-1.4303` n `230`; crypto_major avg `-0.5575` n `8`; equity avg `-0.2073` n `92`; fx avg `0.0025` n `6`; index avg `-0.1083` n `25`; metal avg `-0.1008` n `20`; unknown avg `0.1503` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
