# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T01:37:29.982393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `-0.0027` n `239`; crypto_major avg `-0.034` n `8`; equity avg `0.2253` n `166`; fx avg `0.0124` n `6`; index avg `0.0448` n `27`; metal avg `-0.0471` n `20`; unknown avg `315.9953` n `1265`
- 1h: commodity avg `0.0463` n `13`; crypto_alt avg `-0.2381` n `239`; crypto_major avg `-0.3041` n `8`; equity avg `-0.0299` n `166`; fx avg `0.0821` n `6`; index avg `0.0118` n `27`; metal avg `0.053` n `20`; unknown avg `158.3268` n `1261`
- 4h: commodity avg `-0.2935` n `13`; crypto_alt avg `-0.3433` n `239`; crypto_major avg `-0.2391` n `8`; equity avg `0.4407` n `166`; fx avg `0.1175` n `6`; index avg `0.1071` n `27`; metal avg `0.2653` n `20`; unknown avg `0.9375` n `1212`
- 24h: commodity avg `-0.4177` n `13`; crypto_alt avg `0.468` n `239`; crypto_major avg `0.6796` n `8`; equity avg `1.2608` n `166`; fx avg `0.1653` n `6`; index avg `0.1604` n `27`; metal avg `0.2759` n `20`; unknown avg `242.8215` n `1029`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
