# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T10:52:24.043089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `0.0515` n `231`; crypto_major avg `0.0386` n `8`; equity avg `-0.0052` n `127`; fx avg `0.0022` n `6`; index avg `0.0019` n `26`; metal avg `0.0119` n `20`; unknown avg `0.0321` n `793`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.0324` n `231`; crypto_major avg `0.0649` n `8`; equity avg `0.0021` n `127`; fx avg `0.0005` n `6`; index avg `0.0046` n `26`; metal avg `0.0043` n `20`; unknown avg `0.0333` n `793`
- 4h: commodity avg `0.0463` n `12`; crypto_alt avg `-0.2159` n `231`; crypto_major avg `0.1285` n `8`; equity avg `0.0267` n `127`; fx avg `0.0025` n `6`; index avg `-0.0096` n `26`; metal avg `0.0115` n `20`; unknown avg `0.0434` n `791`
- 24h: commodity avg `-0.1031` n `12`; crypto_alt avg `-2.1233` n `231`; crypto_major avg `-2.0062` n `8`; equity avg `-1.3962` n `127`; fx avg `-0.0894` n `6`; index avg `-0.1253` n `26`; metal avg `-0.6617` n `20`; unknown avg `-0.4336` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
