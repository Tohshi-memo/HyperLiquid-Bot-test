# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T20:37:32.586096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1187` n `12`; crypto_alt avg `-0.3577` n `228`; crypto_major avg `-0.3181` n `8`; equity avg `-0.1416` n `88`; fx avg `0.0005` n `6`; index avg `-0.0134` n `23`; metal avg `-0.0389` n `20`; unknown avg `-0.419` n `764`
- 1h: commodity avg `0.1341` n `12`; crypto_alt avg `-0.4832` n `228`; crypto_major avg `-0.6291` n `8`; equity avg `-0.0387` n `88`; fx avg `0.0009` n `6`; index avg `-0.0583` n `23`; metal avg `-0.0811` n `20`; unknown avg `-0.6372` n `764`
- 4h: commodity avg `0.0687` n `12`; crypto_alt avg `-0.4835` n `228`; crypto_major avg `-0.646` n `8`; equity avg `-0.284` n `87`; fx avg `0.0034` n `6`; index avg `-0.1799` n `23`; metal avg `-0.2533` n `20`; unknown avg `-0.1902` n `764`
- 24h: commodity avg `-0.3406` n `12`; crypto_alt avg `1.9575` n `228`; crypto_major avg `1.7797` n `8`; equity avg `-0.7252` n `87`; fx avg `-0.0837` n `6`; index avg `-0.3909` n `23`; metal avg `0.4816` n `20`; unknown avg `-0.3373` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2227`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
