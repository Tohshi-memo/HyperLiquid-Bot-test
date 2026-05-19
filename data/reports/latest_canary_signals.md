# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T14:07:22.615100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1657` n `12`; crypto_alt avg `-0.2665` n `228`; crypto_major avg `-0.2921` n `8`; equity avg `-0.5576` n `66`; fx avg `-0.0023` n `6`; index avg `-0.2892` n `23`; metal avg `0.0504` n `18`; unknown avg `-0.1186` n `383`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `0.2373` n `228`; crypto_major avg `0.1777` n `8`; equity avg `-0.1485` n `66`; fx avg `-0.0222` n `6`; index avg `-0.4168` n `23`; metal avg `-0.3401` n `18`; unknown avg `-0.1593` n `383`
- 4h: commodity avg `0.1831` n `12`; crypto_alt avg `-0.187` n `228`; crypto_major avg `-0.0259` n `8`; equity avg `-0.5368` n `66`; fx avg `-0.0501` n `6`; index avg `-0.5564` n `23`; metal avg `-1.0148` n `18`; unknown avg `-0.624` n `383`
- 24h: commodity avg `1.3925` n `12`; crypto_alt avg `0.5918` n `228`; crypto_major avg `0.341` n `8`; equity avg `-2.0613` n `66`; fx avg `0.2196` n `6`; index avg `-1.4188` n `23`; metal avg `-1.7959` n `18`; unknown avg `-0.6785` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
