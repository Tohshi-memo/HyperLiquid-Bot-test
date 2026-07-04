# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T05:27:36.200028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.2426` n `229`; crypto_major avg `-0.2048` n `8`; equity avg `-0.0032` n `88`; fx avg `0.0` n `6`; index avg `-0.0266` n `25`; metal avg `-0.0124` n `20`; unknown avg `0.1336` n `765`
- 1h: commodity avg `-0.0294` n `12`; crypto_alt avg `-0.1331` n `229`; crypto_major avg `-0.143` n `8`; equity avg `0.0198` n `88`; fx avg `0.0037` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0076` n `20`; unknown avg `1.7743` n `765`
- 4h: commodity avg `-0.0467` n `12`; crypto_alt avg `-0.0272` n `229`; crypto_major avg `0.2502` n `8`; equity avg `0.1666` n `88`; fx avg `0.0104` n `6`; index avg `0.0139` n `25`; metal avg `0.0241` n `20`; unknown avg `1.0814` n `763`
- 24h: commodity avg `-0.1207` n `12`; crypto_alt avg `2.3192` n `229`; crypto_major avg `2.8369` n `8`; equity avg `0.5443` n `88`; fx avg `-0.1941` n `6`; index avg `0.0373` n `25`; metal avg `-0.0721` n `20`; unknown avg `4.1346` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
