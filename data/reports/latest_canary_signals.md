# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T19:22:34.257683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0487` n `12`; crypto_alt avg `-0.0963` n `230`; crypto_major avg `-0.0828` n `8`; equity avg `0.1216` n `102`; fx avg `0.0054` n `6`; index avg `0.0474` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.112` n `780`
- 1h: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.373` n `230`; crypto_major avg `-0.39` n `8`; equity avg `0.0155` n `102`; fx avg `0.031` n `6`; index avg `0.0348` n `25`; metal avg `0.023` n `20`; unknown avg `-0.2216` n `780`
- 4h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.3738` n `230`; crypto_major avg `0.1104` n `8`; equity avg `0.7917` n `102`; fx avg `0.1229` n `6`; index avg `0.1875` n `25`; metal avg `0.1105` n `20`; unknown avg `14.7083` n `780`
- 24h: commodity avg `0.2711` n `12`; crypto_alt avg `-0.429` n `230`; crypto_major avg `-2.0943` n `8`; equity avg `0.3534` n `102`; fx avg `0.2566` n `6`; index avg `0.267` n `25`; metal avg `-0.3461` n `20`; unknown avg `0.318` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
