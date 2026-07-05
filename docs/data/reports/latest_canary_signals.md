# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T23:37:25.916704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.2669` n `229`; crypto_major avg `-0.2993` n `8`; equity avg `-0.116` n `88`; fx avg `-0.0069` n `6`; index avg `-0.0133` n `25`; metal avg `0.009` n `20`; unknown avg `0.31` n `765`
- 1h: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.0209` n `229`; crypto_major avg `0.002` n `8`; equity avg `-0.0494` n `88`; fx avg `-0.0073` n `6`; index avg `0.0225` n `25`; metal avg `0.0514` n `20`; unknown avg `0.0549` n `765`
- 4h: commodity avg `-0.1756` n `12`; crypto_alt avg `0.5383` n `229`; crypto_major avg `0.9615` n `8`; equity avg `0.1215` n `88`; fx avg `0.0707` n `6`; index avg `0.0153` n `25`; metal avg `0.1823` n `20`; unknown avg `1.1807` n `765`
- 24h: commodity avg `-0.1813` n `12`; crypto_alt avg `0.0611` n `229`; crypto_major avg `0.8039` n `8`; equity avg `0.4252` n `88`; fx avg `0.0227` n `6`; index avg `0.0804` n `25`; metal avg `0.1979` n `20`; unknown avg `1.2888` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
