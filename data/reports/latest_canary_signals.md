# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T22:37:30.358219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.0373` n `228`; crypto_major avg `0.0506` n `8`; equity avg `-0.0061` n `88`; fx avg `0.0113` n `6`; index avg `0.0014` n `23`; metal avg `0.0162` n `20`; unknown avg `-0.0519` n `764`
- 1h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.2833` n `228`; crypto_major avg `-0.0472` n `8`; equity avg `0.1155` n `88`; fx avg `-0.0466` n `6`; index avg `0.0041` n `23`; metal avg `0.0233` n `20`; unknown avg `0.3772` n `748`
- 4h: commodity avg `0.2375` n `12`; crypto_alt avg `-0.2663` n `228`; crypto_major avg `-0.1249` n `8`; equity avg `0.3177` n `88`; fx avg `0.067` n `6`; index avg `-0.0705` n `23`; metal avg `0.0579` n `20`; unknown avg `0.5216` n `748`
- 24h: commodity avg `-0.2507` n `12`; crypto_alt avg `1.2008` n `228`; crypto_major avg `1.2143` n `8`; equity avg `-0.1149` n `87`; fx avg `0.0093` n `6`; index avg `-0.3197` n `23`; metal avg `0.6339` n `20`; unknown avg `-0.0061` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2183`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
