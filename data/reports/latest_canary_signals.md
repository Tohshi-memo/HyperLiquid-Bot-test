# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T02:07:31.778957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `13`; crypto_alt avg `-0.2366` n `235`; crypto_major avg `-0.1607` n `8`; equity avg `-0.025` n `144`; fx avg `-0.0149` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0129` n `20`; unknown avg `-0.0435` n `1077`
- 1h: commodity avg `0.041` n `13`; crypto_alt avg `-0.7976` n `235`; crypto_major avg `-0.6431` n `8`; equity avg `-0.2404` n `144`; fx avg `0.0034` n `6`; index avg `-0.0555` n `26`; metal avg `-0.1603` n `20`; unknown avg `1.578` n `1077`
- 4h: commodity avg `0.0547` n `13`; crypto_alt avg `-1.4299` n `235`; crypto_major avg `-0.7392` n `8`; equity avg `-0.1335` n `144`; fx avg `0.0117` n `6`; index avg `-0.0525` n `26`; metal avg `-0.0898` n `20`; unknown avg `0.4265` n `1071`
- 24h: commodity avg `-0.0109` n `13`; crypto_alt avg `-1.1113` n `235`; crypto_major avg `-0.6318` n `8`; equity avg `-0.137` n `144`; fx avg `-0.0235` n `6`; index avg `0.0384` n `26`; metal avg `-0.1127` n `20`; unknown avg `626.8641` n `798`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
