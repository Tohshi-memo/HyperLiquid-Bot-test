# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T03:52:26.431371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `-0.1543` n `228`; crypto_major avg `-0.1489` n `8`; equity avg `-0.0465` n `88`; fx avg `-0.0035` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0068` n `20`; unknown avg `-0.1676` n `764`
- 1h: commodity avg `0.063` n `12`; crypto_alt avg `-0.4518` n `228`; crypto_major avg `-0.2947` n `8`; equity avg `-0.0252` n `88`; fx avg `-0.0012` n `6`; index avg `-0.0124` n `23`; metal avg `-0.0004` n `20`; unknown avg `9.6006` n `764`
- 4h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.1132` n `228`; crypto_major avg `0.1095` n `8`; equity avg `0.1361` n `88`; fx avg `0.0214` n `6`; index avg `0.0181` n `23`; metal avg `0.0085` n `20`; unknown avg `0.145` n `764`
- 24h: commodity avg `-0.062` n `12`; crypto_alt avg `2.1366` n `228`; crypto_major avg `1.8574` n `8`; equity avg `2.041` n `87`; fx avg `-0.0245` n `6`; index avg `0.2136` n `23`; metal avg `1.2824` n `20`; unknown avg `0.0381` n `716`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
