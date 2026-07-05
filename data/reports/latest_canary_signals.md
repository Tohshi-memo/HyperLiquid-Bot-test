# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T05:22:28.924889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0218` n `229`; crypto_major avg `-0.0548` n `8`; equity avg `0.0096` n `88`; fx avg `0.0005` n `6`; index avg `-0.0137` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.597` n `765`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.0903` n `229`; crypto_major avg `-0.3034` n `8`; equity avg `0.0057` n `88`; fx avg `-0.0009` n `6`; index avg `0.037` n `25`; metal avg `-0.0033` n `20`; unknown avg `2.2636` n `765`
- 4h: commodity avg `0.0271` n `12`; crypto_alt avg `-0.3254` n `229`; crypto_major avg `-0.401` n `8`; equity avg `0.165` n `88`; fx avg `-0.0027` n `6`; index avg `0.0356` n `25`; metal avg `-0.0196` n `20`; unknown avg `-0.1428` n `765`
- 24h: commodity avg `0.0818` n `12`; crypto_alt avg `-0.6943` n `229`; crypto_major avg `-0.9992` n `8`; equity avg `0.2137` n `88`; fx avg `-0.0094` n `6`; index avg `0.0726` n `25`; metal avg `0.0831` n `20`; unknown avg `-0.8389` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
