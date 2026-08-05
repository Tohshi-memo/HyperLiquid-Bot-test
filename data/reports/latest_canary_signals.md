# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T07:31:29.966422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0948` n `12`; crypto_alt avg `0.0118` n `230`; crypto_major avg `-0.0105` n `8`; equity avg `-0.1304` n `108`; fx avg `0.0055` n `6`; index avg `-0.0216` n `25`; metal avg `-0.034` n `20`; unknown avg `-0.001` n `781`
- 1h: commodity avg `0.2249` n `12`; crypto_alt avg `-0.2646` n `230`; crypto_major avg `-0.4324` n `8`; equity avg `-0.307` n `108`; fx avg `0.0214` n `6`; index avg `-0.0425` n `25`; metal avg `-0.0496` n `20`; unknown avg `-0.0356` n `781`
- 4h: commodity avg `0.4225` n `12`; crypto_alt avg `0.1978` n `230`; crypto_major avg `0.0904` n `8`; equity avg `-0.0414` n `108`; fx avg `0.0422` n `6`; index avg `-0.0098` n `25`; metal avg `0.2997` n `20`; unknown avg `0.1021` n `749`
- 24h: commodity avg `-1.1048` n `12`; crypto_alt avg `0.5508` n `230`; crypto_major avg `0.5438` n `8`; equity avg `3.0445` n `108`; fx avg `-0.0144` n `6`; index avg `0.6703` n `25`; metal avg `1.2087` n `20`; unknown avg `0.0932` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
