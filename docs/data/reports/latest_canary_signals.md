# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T16:22:29.579876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0491` n `12`; crypto_alt avg `-0.1921` n `228`; crypto_major avg `-0.1595` n `8`; equity avg `-0.029` n `88`; fx avg `0.005` n `6`; index avg `-0.0132` n `23`; metal avg `-0.0038` n `20`; unknown avg `0.0415` n `764`
- 1h: commodity avg `-0.1433` n `12`; crypto_alt avg `0.1634` n `228`; crypto_major avg `-0.1089` n `8`; equity avg `-0.0562` n `88`; fx avg `0.0081` n `6`; index avg `-0.0117` n `23`; metal avg `-0.0085` n `20`; unknown avg `0.1193` n `764`
- 4h: commodity avg `-0.1546` n `12`; crypto_alt avg `0.7824` n `228`; crypto_major avg `0.9137` n `8`; equity avg `0.0893` n `88`; fx avg `0.0073` n `6`; index avg `0.0078` n `23`; metal avg `0.0039` n `20`; unknown avg `0.2709` n `764`
- 24h: commodity avg `0.1122` n `12`; crypto_alt avg `1.1296` n `228`; crypto_major avg `1.082` n `8`; equity avg `0.7588` n `87`; fx avg `0.083` n `6`; index avg `-0.0624` n `23`; metal avg `-0.0188` n `20`; unknown avg `0.4331` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
