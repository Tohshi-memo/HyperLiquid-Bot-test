# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T09:52:31.423521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `12`; crypto_alt avg `0.0064` n `229`; crypto_major avg `-0.0326` n `8`; equity avg `-0.0145` n `91`; fx avg `-0.0093` n `6`; index avg `0.0029` n `25`; metal avg `0.0123` n `20`; unknown avg `0.0086` n `766`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.1558` n `229`; crypto_major avg `0.2541` n `8`; equity avg `0.1328` n `91`; fx avg `0.0118` n `6`; index avg `0.0449` n `25`; metal avg `0.0291` n `20`; unknown avg `-0.0435` n `765`
- 4h: commodity avg `-0.103` n `12`; crypto_alt avg `0.2613` n `229`; crypto_major avg `0.377` n `8`; equity avg `-0.2901` n `91`; fx avg `-0.0505` n `6`; index avg `-0.0533` n `25`; metal avg `-0.1529` n `20`; unknown avg `1.1293` n `733`
- 24h: commodity avg `-0.8709` n `12`; crypto_alt avg `1.1762` n `229`; crypto_major avg `1.7018` n `8`; equity avg `0.3445` n `91`; fx avg `-0.1368` n `6`; index avg `0.2356` n `25`; metal avg `0.0741` n `20`; unknown avg `0.1328` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
