# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T21:50:03.816946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0511` n `13`; crypto_alt avg `0.2999` n `237`; crypto_major avg `0.1273` n `8`; equity avg `0.2264` n `151`; fx avg `0.005` n `6`; index avg `0.039` n `26`; metal avg `-0.003` n `20`; unknown avg `0.9655` n `1154`
- 1h: commodity avg `-0.0341` n `13`; crypto_alt avg `0.6425` n `237`; crypto_major avg `0.6304` n `8`; equity avg `0.3413` n `151`; fx avg `-0.0328` n `6`; index avg `0.0497` n `26`; metal avg `0.0144` n `20`; unknown avg `1.6273` n `1114`
- 4h: commodity avg `-0.0087` n `13`; crypto_alt avg `-0.9619` n `237`; crypto_major avg `-0.2037` n `8`; equity avg `0.1329` n `151`; fx avg `-0.0426` n `6`; index avg `0.0138` n `26`; metal avg `-0.0308` n `20`; unknown avg `4.8438` n `1096`
- 24h: commodity avg `-0.0146` n `13`; crypto_alt avg `-3.0972` n `236`; crypto_major avg `-0.6834` n `8`; equity avg `0.1422` n `151`; fx avg `-0.046` n `6`; index avg `0.0248` n `26`; metal avg `0.0069` n `20`; unknown avg `0.0242` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2069`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1432`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1191`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0736`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0725`, n `666`, weak_sample_signal
