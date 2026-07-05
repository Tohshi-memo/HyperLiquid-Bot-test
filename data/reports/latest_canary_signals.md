# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T04:07:26.564509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.0431` n `229`; crypto_major avg `0.0137` n `8`; equity avg `0.0055` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0128` n `25`; metal avg `0.003` n `20`; unknown avg `0.5288` n `765`
- 1h: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.0579` n `229`; crypto_major avg `0.0306` n `8`; equity avg `0.0077` n `88`; fx avg `-0.0026` n `6`; index avg `0.0097` n `25`; metal avg `0.001` n `20`; unknown avg `0.4278` n `765`
- 4h: commodity avg `0.0411` n `12`; crypto_alt avg `-0.8878` n `229`; crypto_major avg `-0.9711` n `8`; equity avg `0.1003` n `88`; fx avg `-0.0022` n `6`; index avg `-0.0035` n `25`; metal avg `-0.025` n `20`; unknown avg `-0.245` n `763`
- 24h: commodity avg `0.0446` n `12`; crypto_alt avg `-1.0923` n `229`; crypto_major avg `-1.1117` n `8`; equity avg `0.1384` n `88`; fx avg `-0.0012` n `6`; index avg `0.0208` n `25`; metal avg `0.0793` n `20`; unknown avg `-0.9199` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
