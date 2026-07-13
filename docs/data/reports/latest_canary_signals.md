# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T03:37:28.904887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.1649` n `230`; crypto_major avg `-0.1775` n `8`; equity avg `-0.1441` n `92`; fx avg `0.0068` n `6`; index avg `-0.013` n `25`; metal avg `-0.0317` n `20`; unknown avg `1.2361` n `766`
- 1h: commodity avg `-0.0444` n `12`; crypto_alt avg `-1.1707` n `230`; crypto_major avg `-1.0681` n `8`; equity avg `-0.807` n `92`; fx avg `0.027` n `6`; index avg `-0.1282` n `25`; metal avg `-0.2069` n `20`; unknown avg `1.6378` n `766`
- 4h: commodity avg `0.0906` n `12`; crypto_alt avg `-1.2393` n `230`; crypto_major avg `-1.1322` n `8`; equity avg `-1.9388` n `92`; fx avg `0.0993` n `6`; index avg `-0.4094` n `25`; metal avg `-0.2204` n `20`; unknown avg `1.7891` n `766`
- 24h: commodity avg `0.1532` n `12`; crypto_alt avg `-2.5579` n `230`; crypto_major avg `-1.5226` n `8`; equity avg `-2.3679` n `92`; fx avg `0.0387` n `6`; index avg `-0.4367` n `25`; metal avg `-0.5258` n `20`; unknown avg `-0.1293` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1788`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1786`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1152`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1132`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1043`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0896`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `669`, weak_sample_signal
