# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T16:22:29.781405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `13`; crypto_alt avg `0.0825` n `239`; crypto_major avg `0.2652` n `8`; equity avg `0.0868` n `161`; fx avg `0.0135` n `6`; index avg `0.0164` n `27`; metal avg `-0.0117` n `20`; unknown avg `0.0488` n `1261`
- 1h: commodity avg `-0.1764` n `13`; crypto_alt avg `0.7191` n `239`; crypto_major avg `1.0725` n `8`; equity avg `1.101` n `161`; fx avg `0.0278` n `6`; index avg `0.1233` n `27`; metal avg `-0.0227` n `20`; unknown avg `0.2983` n `1243`
- 4h: commodity avg `0.2301` n `13`; crypto_alt avg `0.7795` n `239`; crypto_major avg `1.0433` n `8`; equity avg `1.2597` n `161`; fx avg `0.0203` n `6`; index avg `0.1124` n `27`; metal avg `-0.2424` n `20`; unknown avg `-0.1043` n `1225`
- 24h: commodity avg `0.7744` n `13`; crypto_alt avg `1.0461` n `239`; crypto_major avg `1.8988` n `8`; equity avg `5.3398` n `161`; fx avg `-0.0941` n `6`; index avg `0.4853` n `27`; metal avg `0.3137` n `20`; unknown avg `2.8877` n `1153`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2504`, n `668`, moderate_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
