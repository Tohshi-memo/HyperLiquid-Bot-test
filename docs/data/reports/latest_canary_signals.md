# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T21:37:24.520575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `0.0333` n `236`; crypto_major avg `0.0574` n `8`; equity avg `0.0711` n `151`; fx avg `0.0129` n `6`; index avg `0.0106` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.1171` n `1136`
- 1h: commodity avg `-0.0442` n `13`; crypto_alt avg `-0.0292` n `236`; crypto_major avg `-0.0822` n `8`; equity avg `-0.2332` n `151`; fx avg `-0.0102` n `6`; index avg `-0.0426` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.053` n `1128`
- 4h: commodity avg `-0.2334` n `13`; crypto_alt avg `0.3891` n `236`; crypto_major avg `0.1729` n `8`; equity avg `0.9323` n `151`; fx avg `-0.0275` n `6`; index avg `0.0592` n `26`; metal avg `0.1113` n `20`; unknown avg `-0.1058` n `1052`
- 24h: commodity avg `-0.2648` n `13`; crypto_alt avg `0.5936` n `236`; crypto_major avg `0.5563` n `8`; equity avg `0.3863` n `151`; fx avg `0.1778` n `6`; index avg `-0.0643` n `26`; metal avg `0.514` n `20`; unknown avg `23.627` n `926`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0966`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0924`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0883`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0745`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0506`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `666`, weak_sample_signal
