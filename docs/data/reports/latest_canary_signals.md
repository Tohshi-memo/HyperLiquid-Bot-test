# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T11:22:29.420573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.0231` n `229`; crypto_major avg `-0.0116` n `8`; equity avg `-0.026` n `88`; fx avg `0.0014` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.0173` n `765`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.0396` n `229`; crypto_major avg `0.0126` n `8`; equity avg `0.0733` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0043` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0528` n `765`
- 4h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.1982` n `229`; crypto_major avg `-0.0281` n `8`; equity avg `0.0411` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0128` n `25`; metal avg `0.0256` n `20`; unknown avg `-0.1391` n `765`
- 24h: commodity avg `-0.0428` n `12`; crypto_alt avg `-0.8845` n `229`; crypto_major avg `-0.6194` n `8`; equity avg `0.2328` n `88`; fx avg `0.0221` n `6`; index avg `0.027` n `25`; metal avg `0.0666` n `20`; unknown avg `-1.2208` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
