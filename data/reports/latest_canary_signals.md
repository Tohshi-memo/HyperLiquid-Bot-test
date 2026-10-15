# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T19:17:33.659928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `0.0681` n `236`; crypto_major avg `0.0672` n `8`; equity avg `0.4189` n `151`; fx avg `0.0025` n `6`; index avg `0.0568` n `26`; metal avg `0.0237` n `20`; unknown avg `17.5262` n `1136`
- 1h: commodity avg `-0.0837` n `13`; crypto_alt avg `0.6318` n `236`; crypto_major avg `0.5162` n `8`; equity avg `1.1182` n `151`; fx avg `-0.0072` n `6`; index avg `0.1586` n `26`; metal avg `0.0369` n `20`; unknown avg `3.033` n `1134`
- 4h: commodity avg `-0.0441` n `13`; crypto_alt avg `1.5279` n `236`; crypto_major avg `0.7875` n `8`; equity avg `0.9974` n `151`; fx avg `0.0161` n `6`; index avg `0.1194` n `26`; metal avg `0.0118` n `20`; unknown avg `-0.0558` n `1128`
- 24h: commodity avg `-0.0462` n `13`; crypto_alt avg `1.1433` n `236`; crypto_major avg `0.6817` n `8`; equity avg `-0.3335` n `151`; fx avg `0.1876` n `6`; index avg `-0.1083` n `26`; metal avg `0.4098` n `20`; unknown avg `0.4593` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0882`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0809`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0542`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0538`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
