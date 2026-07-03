# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T22:37:27.844746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0613` n `229`; crypto_major avg `-0.0414` n `8`; equity avg `-0.0416` n `88`; fx avg `0.0061` n `6`; index avg `0.0014` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0822` n `765`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `0.0257` n `229`; crypto_major avg `0.0307` n `8`; equity avg `-0.0642` n `88`; fx avg `0.0305` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0215` n `20`; unknown avg `-0.0586` n `765`
- 4h: commodity avg `-0.0221` n `12`; crypto_alt avg `0.5591` n `229`; crypto_major avg `0.6338` n `8`; equity avg `-0.0324` n `88`; fx avg `-0.0077` n `6`; index avg `-0.0446` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.319` n `765`
- 24h: commodity avg `0.134` n `12`; crypto_alt avg `3.3223` n `229`; crypto_major avg `3.4148` n `8`; equity avg `1.7111` n `88`; fx avg `-0.0579` n `6`; index avg `0.4449` n `25`; metal avg `0.5116` n `20`; unknown avg `5.1553` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
