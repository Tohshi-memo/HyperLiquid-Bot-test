# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T18:26:04.754942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `13`; crypto_alt avg `0.2449` n `236`; crypto_major avg `0.1245` n `8`; equity avg `-0.0047` n `151`; fx avg `-0.0006` n `6`; index avg `0.0058` n `26`; metal avg `0.0093` n `20`; unknown avg `2.9614` n `1185`
- 1h: commodity avg `0.0538` n `13`; crypto_alt avg `0.6137` n `236`; crypto_major avg `0.4054` n `8`; equity avg `0.1111` n `151`; fx avg `-0.0127` n `6`; index avg `0.0073` n `26`; metal avg `0.0184` n `20`; unknown avg `0.0372` n `1183`
- 4h: commodity avg `0.0786` n `13`; crypto_alt avg `-0.4894` n `236`; crypto_major avg `-0.207` n `8`; equity avg `-0.2255` n `151`; fx avg `-0.0316` n `6`; index avg `-0.0545` n `26`; metal avg `-0.0215` n `20`; unknown avg `2.5729` n `1127`
- 24h: commodity avg `0.0217` n `13`; crypto_alt avg `-1.1313` n `236`; crypto_major avg `-0.2766` n `8`; equity avg `-0.5178` n `151`; fx avg `-0.0223` n `6`; index avg `-0.0811` n `26`; metal avg `0.0143` n `20`; unknown avg `4.3701` n `1019`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1712`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
