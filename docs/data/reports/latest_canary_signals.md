# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T02:52:29.893567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `-0.3897` n `232`; crypto_major avg `-0.2722` n `8`; equity avg `-0.1726` n `134`; fx avg `0.0071` n `6`; index avg `-0.0237` n `26`; metal avg `-0.015` n `20`; unknown avg `0.7478` n `797`
- 1h: commodity avg `0.0247` n `12`; crypto_alt avg `-0.6785` n `232`; crypto_major avg `-0.5758` n `8`; equity avg `-0.0317` n `134`; fx avg `-0.0435` n `6`; index avg `-0.0081` n `26`; metal avg `-0.1608` n `20`; unknown avg `0.7659` n `789`
- 4h: commodity avg `-0.1017` n `12`; crypto_alt avg `0.6084` n `232`; crypto_major avg `0.0242` n `8`; equity avg `0.4564` n `134`; fx avg `-0.1805` n `6`; index avg `0.1221` n `26`; metal avg `0.0958` n `20`; unknown avg `1.0414` n `783`
- 24h: commodity avg `0.1315` n `12`; crypto_alt avg `-0.2631` n `232`; crypto_major avg `-1.6922` n `8`; equity avg `0.5043` n `134`; fx avg `-0.3501` n `6`; index avg `0.1612` n `26`; metal avg `0.1631` n `20`; unknown avg `7374.4764` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
