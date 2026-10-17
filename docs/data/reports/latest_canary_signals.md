# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T04:52:29.779553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `13`; crypto_alt avg `-0.2287` n `236`; crypto_major avg `-0.1219` n `8`; equity avg `-0.0129` n `151`; fx avg `0.0` n `6`; index avg `0.0087` n `26`; metal avg `-0.0052` n `20`; unknown avg `-0.0671` n `1193`
- 1h: commodity avg `0.003` n `13`; crypto_alt avg `-0.0401` n `236`; crypto_major avg `-0.1305` n `8`; equity avg `0.0008` n `151`; fx avg `-0.0025` n `6`; index avg `0.0082` n `26`; metal avg `-0.0066` n `20`; unknown avg `-0.2136` n `1185`
- 4h: commodity avg `0.0483` n `13`; crypto_alt avg `0.2805` n `236`; crypto_major avg `0.149` n `8`; equity avg `0.1901` n `151`; fx avg `0.0087` n `6`; index avg `0.0338` n `26`; metal avg `0.0192` n `20`; unknown avg `1.1018` n `1183`
- 24h: commodity avg `0.5938` n `13`; crypto_alt avg `-1.1153` n `236`; crypto_major avg `-1.0044` n `8`; equity avg `-4.4013` n `151`; fx avg `-0.0515` n `6`; index avg `-0.6935` n `26`; metal avg `-0.2503` n `20`; unknown avg `40.9471` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1739`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1198`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0767`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
