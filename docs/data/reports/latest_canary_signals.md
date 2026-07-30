# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T12:22:29.902184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0418` n `12`; crypto_alt avg `-0.0352` n `230`; crypto_major avg `-0.0585` n `8`; equity avg `0.0229` n `102`; fx avg `0.0008` n `6`; index avg `-0.0271` n `25`; metal avg `-0.0289` n `20`; unknown avg `0.031` n `779`
- 1h: commodity avg `-0.0348` n `12`; crypto_alt avg `0.1959` n `230`; crypto_major avg `0.1727` n `8`; equity avg `0.6434` n `102`; fx avg `0.0256` n `6`; index avg `0.0928` n `25`; metal avg `-0.0175` n `20`; unknown avg `0.0551` n `779`
- 4h: commodity avg `-0.3663` n `12`; crypto_alt avg `0.2519` n `230`; crypto_major avg `0.6069` n `8`; equity avg `2.024` n `102`; fx avg `-0.0351` n `6`; index avg `0.2868` n `25`; metal avg `0.2357` n `20`; unknown avg `0.0904` n `771`
- 24h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.1975` n `230`; crypto_major avg `0.3602` n `8`; equity avg `-1.118` n `102`; fx avg `-0.0462` n `6`; index avg `-0.1218` n `25`; metal avg `0.6412` n `20`; unknown avg `-0.1701` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
