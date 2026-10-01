# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T17:52:33.397527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `13`; crypto_alt avg `0.2789` n `234`; crypto_major avg `0.0924` n `8`; equity avg `0.0358` n `142`; fx avg `0.0117` n `6`; index avg `0.0106` n `26`; metal avg `-0.032` n `20`; unknown avg `-0.4106` n `975`
- 1h: commodity avg `0.0491` n `13`; crypto_alt avg `1.3008` n `234`; crypto_major avg `0.9657` n `8`; equity avg `0.8811` n `142`; fx avg `-0.024` n `6`; index avg `0.1753` n `26`; metal avg `0.1353` n `20`; unknown avg `1.5007` n `973`
- 4h: commodity avg `-0.0491` n `13`; crypto_alt avg `0.7127` n `234`; crypto_major avg `0.3454` n `8`; equity avg `1.1281` n `142`; fx avg `-0.1803` n `6`; index avg `0.1109` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.4695` n `909`
- 24h: commodity avg `-0.2227` n `13`; crypto_alt avg `-0.3268` n `234`; crypto_major avg `0.1648` n `8`; equity avg `1.1319` n `142`; fx avg `-0.1419` n `6`; index avg `0.136` n `26`; metal avg `0.0295` n `20`; unknown avg `-0.1576` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
