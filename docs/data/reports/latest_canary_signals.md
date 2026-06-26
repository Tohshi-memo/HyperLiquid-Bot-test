# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T22:22:01.341811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.0331` n `228`; crypto_major avg `0.1202` n `8`; equity avg `0.0426` n `88`; fx avg `-0.0086` n `6`; index avg `-0.0033` n `23`; metal avg `-0.0073` n `20`; unknown avg `-0.0` n `748`
- 1h: commodity avg `-0.06` n `12`; crypto_alt avg `-0.0642` n `228`; crypto_major avg `0.0436` n `8`; equity avg `0.16` n `88`; fx avg `-0.0349` n `6`; index avg `0.0031` n `23`; metal avg `0.0086` n `20`; unknown avg `-0.0736` n `748`
- 4h: commodity avg `0.2658` n `12`; crypto_alt avg `-0.573` n `228`; crypto_major avg `-0.5579` n `8`; equity avg `0.0763` n `88`; fx avg `0.0512` n `6`; index avg `-0.1028` n `23`; metal avg `0.0353` n `20`; unknown avg `1.0696` n `748`
- 24h: commodity avg `-0.2583` n `12`; crypto_alt avg `1.3507` n `228`; crypto_major avg `1.3904` n `8`; equity avg `-0.1683` n `87`; fx avg `-0.0048` n `6`; index avg `-0.3229` n `23`; metal avg `0.7386` n `20`; unknown avg `0.055` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2191`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
