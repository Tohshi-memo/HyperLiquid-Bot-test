# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T18:52:29.370249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0691` n `12`; crypto_alt avg `0.2896` n `228`; crypto_major avg `0.3696` n `8`; equity avg `0.071` n `88`; fx avg `0.0018` n `6`; index avg `0.0087` n `23`; metal avg `0.0797` n `20`; unknown avg `0.1276` n `765`
- 1h: commodity avg `0.014` n `12`; crypto_alt avg `0.1839` n `228`; crypto_major avg `0.4216` n `8`; equity avg `0.1252` n `88`; fx avg `-0.009` n `6`; index avg `0.0086` n `23`; metal avg `0.0701` n `20`; unknown avg `0.0015` n `765`
- 4h: commodity avg `-0.1996` n `12`; crypto_alt avg `0.1673` n `228`; crypto_major avg `0.6832` n `8`; equity avg `0.7412` n `88`; fx avg `0.0015` n `6`; index avg `0.1036` n `23`; metal avg `-0.119` n `20`; unknown avg `-0.1131` n `765`
- 24h: commodity avg `0.158` n `12`; crypto_alt avg `-2.2488` n `228`; crypto_major avg `-1.8915` n `8`; equity avg `1.1922` n `88`; fx avg `0.1421` n `6`; index avg `0.3077` n `23`; metal avg `0.27` n `20`; unknown avg `8.4455` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
