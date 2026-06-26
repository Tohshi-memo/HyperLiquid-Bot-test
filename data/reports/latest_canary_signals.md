# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T23:22:30.004320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `-0.0547` n `228`; crypto_major avg `-0.1249` n `8`; equity avg `0.0393` n `88`; fx avg `0.0571` n `6`; index avg `0.0062` n `23`; metal avg `0.014` n `20`; unknown avg `-0.0083` n `764`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `0.2037` n `228`; crypto_major avg `0.2111` n `8`; equity avg `0.0904` n `88`; fx avg `0.0487` n `6`; index avg `0.0091` n `23`; metal avg `0.0598` n `20`; unknown avg `-0.0037` n `764`
- 4h: commodity avg `0.2311` n `12`; crypto_alt avg `-0.3466` n `228`; crypto_major avg `-0.2291` n `8`; equity avg `0.3125` n `88`; fx avg `0.1009` n `6`; index avg `-0.0565` n `23`; metal avg `0.1536` n `20`; unknown avg `-0.0208` n `748`
- 24h: commodity avg `-0.2555` n `12`; crypto_alt avg `1.332` n `228`; crypto_major avg `0.9478` n `8`; equity avg `-0.5001` n `87`; fx avg `0.0521` n `6`; index avg `-0.3925` n `23`; metal avg `0.6761` n `20`; unknown avg `0.1526` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
