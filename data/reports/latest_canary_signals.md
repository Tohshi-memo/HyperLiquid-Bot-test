# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T18:22:33.905660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `13`; crypto_alt avg `-0.2681` n `238`; crypto_major avg `-0.1542` n `8`; equity avg `-0.0984` n `156`; fx avg `0.0071` n `6`; index avg `-0.0133` n `27`; metal avg `0.0069` n `20`; unknown avg `128.3527` n `1255`
- 1h: commodity avg `-0.0214` n `13`; crypto_alt avg `-0.2825` n `238`; crypto_major avg `-0.2359` n `8`; equity avg `-0.1422` n `156`; fx avg `0.0078` n `6`; index avg `-0.0157` n `27`; metal avg `0.0026` n `20`; unknown avg `160.2473` n `1249`
- 4h: commodity avg `-0.0963` n `13`; crypto_alt avg `-0.9083` n `238`; crypto_major avg `-0.4291` n `8`; equity avg `-0.1223` n `156`; fx avg `0.0231` n `6`; index avg `0.0207` n `27`; metal avg `0.0079` n `20`; unknown avg `-0.1026` n `1237`
- 24h: commodity avg `-0.0314` n `13`; crypto_alt avg `-0.7274` n `238`; crypto_major avg `-0.3102` n `8`; equity avg `0.2718` n `156`; fx avg `0.0105` n `6`; index avg `0.0714` n `27`; metal avg `0.0666` n `20`; unknown avg `3.5371` n `1004`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
