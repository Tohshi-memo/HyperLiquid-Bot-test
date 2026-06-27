# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T11:22:43.383836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.1033` n `228`; crypto_major avg `-0.1137` n `8`; equity avg `-0.0579` n `88`; fx avg `-0.0006` n `6`; index avg `-0.0179` n `23`; metal avg `-0.0112` n `20`; unknown avg `0.0212` n `764`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `-0.1609` n `228`; crypto_major avg `-0.2233` n `8`; equity avg `-0.0102` n `88`; fx avg `0.0007` n `6`; index avg `-0.0249` n `23`; metal avg `-0.0054` n `20`; unknown avg `0.0245` n `764`
- 4h: commodity avg `0.072` n `12`; crypto_alt avg `-0.5056` n `228`; crypto_major avg `-0.4485` n `8`; equity avg `0.0342` n `88`; fx avg `-0.0055` n `6`; index avg `-0.029` n `23`; metal avg `-0.0255` n `20`; unknown avg `-0.155` n `748`
- 24h: commodity avg `0.089` n `12`; crypto_alt avg `1.8191` n `228`; crypto_major avg `1.797` n `8`; equity avg `1.8352` n `87`; fx avg `0.0208` n `6`; index avg `0.044` n `23`; metal avg `0.3061` n `20`; unknown avg `0.0998` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
