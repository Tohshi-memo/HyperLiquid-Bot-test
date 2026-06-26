# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T23:52:32.975294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `-0.0253` n `228`; crypto_major avg `-0.1032` n `8`; equity avg `-0.0229` n `88`; fx avg `-0.004` n `6`; index avg `-0.0009` n `23`; metal avg `0.0141` n `20`; unknown avg `0.0913` n `764`
- 1h: commodity avg `0.0624` n `12`; crypto_alt avg `0.0993` n `228`; crypto_major avg `0.1135` n `8`; equity avg `0.0523` n `88`; fx avg `-0.0293` n `6`; index avg `0.0162` n `23`; metal avg `0.0324` n `20`; unknown avg `0.0927` n `764`
- 4h: commodity avg `0.1998` n `12`; crypto_alt avg `-0.3468` n `228`; crypto_major avg `-0.3564` n `8`; equity avg `0.1974` n `88`; fx avg `0.0526` n `6`; index avg `-0.0251` n `23`; metal avg `0.0984` n `20`; unknown avg `-0.1155` n `748`
- 24h: commodity avg `-0.2149` n `12`; crypto_alt avg `1.4846` n `228`; crypto_major avg `1.2721` n `8`; equity avg `-0.2604` n `87`; fx avg `-0.0166` n `6`; index avg `-0.3242` n `23`; metal avg `0.7975` n `20`; unknown avg `0.286` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
