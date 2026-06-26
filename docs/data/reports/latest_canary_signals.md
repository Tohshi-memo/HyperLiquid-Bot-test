# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T19:37:30.128427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `12`; crypto_alt avg `0.0636` n `228`; crypto_major avg `0.1955` n `8`; equity avg `0.0742` n `88`; fx avg `-0.0072` n `6`; index avg `-0.0164` n `23`; metal avg `0.0278` n `20`; unknown avg `0.2313` n `764`
- 1h: commodity avg `0.059` n `12`; crypto_alt avg `0.3858` n `228`; crypto_major avg `0.4626` n `8`; equity avg `0.173` n `88`; fx avg `-0.0037` n `6`; index avg `-0.0227` n `23`; metal avg `-0.0241` n `20`; unknown avg `0.6522` n `764`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `0.6011` n `228`; crypto_major avg `0.3033` n `8`; equity avg `-0.2911` n `87`; fx avg `-0.0079` n `6`; index avg `-0.116` n `23`; metal avg `-0.1998` n `20`; unknown avg `-0.153` n `764`
- 24h: commodity avg `-0.5533` n `12`; crypto_alt avg `3.1584` n `228`; crypto_major avg `3.0483` n `8`; equity avg `-0.2805` n `87`; fx avg `-0.0921` n `6`; index avg `-0.2584` n `23`; metal avg `0.5086` n `20`; unknown avg `0.1599` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2182`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
