# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T07:07:37.729688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `-0.0948` n `239`; crypto_major avg `-0.0534` n `8`; equity avg `-0.1224` n `165`; fx avg `0.0077` n `6`; index avg `0.0009` n `27`; metal avg `-0.0998` n `20`; unknown avg `-0.0993` n `1252`
- 1h: commodity avg `0.0365` n `13`; crypto_alt avg `-0.0461` n `239`; crypto_major avg `0.1424` n `8`; equity avg `-0.2212` n `165`; fx avg `0.0119` n `6`; index avg `-0.0026` n `27`; metal avg `-0.064` n `20`; unknown avg `202.8436` n `1254`
- 4h: commodity avg `-0.0972` n `13`; crypto_alt avg `0.0727` n `239`; crypto_major avg `0.2824` n `8`; equity avg `-0.4508` n `165`; fx avg `0.0127` n `6`; index avg `-0.0287` n `27`; metal avg `0.1974` n `20`; unknown avg `-0.38` n `1222`
- 24h: commodity avg `-0.1668` n `13`; crypto_alt avg `-3.2299` n `239`; crypto_major avg `-2.6891` n `8`; equity avg `-7.1129` n `165`; fx avg `0.0332` n `6`; index avg `-0.6523` n `27`; metal avg `-1.6685` n `20`; unknown avg `8.6799` n `1167`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
