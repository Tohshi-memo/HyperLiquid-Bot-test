# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T20:37:25.876911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.0641` n `229`; crypto_major avg `-0.104` n `8`; equity avg `-0.006` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0041` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0733` n `765`
- 1h: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.0858` n `229`; crypto_major avg `-0.0467` n `8`; equity avg `0.0296` n `88`; fx avg `-0.0118` n `6`; index avg `-0.006` n `25`; metal avg `0.0112` n `20`; unknown avg `0.0247` n `765`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `0.3954` n `229`; crypto_major avg `0.281` n `8`; equity avg `0.1336` n `88`; fx avg `-0.0029` n `6`; index avg `0.0023` n `25`; metal avg `0.018` n `20`; unknown avg `0.7248` n `765`
- 24h: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.8669` n `229`; crypto_major avg `-0.3617` n `8`; equity avg `0.3568` n `88`; fx avg `-0.0348` n `6`; index avg `0.0817` n `25`; metal avg `0.0622` n `20`; unknown avg `1.0977` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
