# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T01:07:30.526577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0789` n `12`; crypto_alt avg `-0.1397` n `228`; crypto_major avg `-0.1724` n `8`; equity avg `-0.1108` n `88`; fx avg `0.0031` n `6`; index avg `-0.0304` n `23`; metal avg `0.002` n `20`; unknown avg `18.8734` n `764`
- 1h: commodity avg `0.1345` n `12`; crypto_alt avg `0.0204` n `228`; crypto_major avg `-0.148` n `8`; equity avg `-0.105` n `88`; fx avg `-0.0077` n `6`; index avg `-0.056` n `23`; metal avg `-0.0064` n `20`; unknown avg `1.3929` n `764`
- 4h: commodity avg `0.4504` n `12`; crypto_alt avg `-0.4327` n `228`; crypto_major avg `-0.797` n `8`; equity avg `-0.1807` n `88`; fx avg `-0.0213` n `6`; index avg `-0.1142` n `23`; metal avg `0.0148` n `20`; unknown avg `-0.5604` n `764`
- 24h: commodity avg `0.3774` n `12`; crypto_alt avg `-0.7453` n `228`; crypto_major avg `-0.9935` n `8`; equity avg `0.2223` n `88`; fx avg `-0.0102` n `6`; index avg `-0.1196` n `23`; metal avg `-0.0392` n `20`; unknown avg `-0.6375` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
