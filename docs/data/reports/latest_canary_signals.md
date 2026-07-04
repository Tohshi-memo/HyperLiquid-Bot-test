# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T19:22:25.198846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.038` n `229`; crypto_major avg `-0.0177` n `8`; equity avg `0.0638` n `88`; fx avg `0.001` n `6`; index avg `0.0019` n `25`; metal avg `0.0236` n `20`; unknown avg `-0.1897` n `765`
- 1h: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.2484` n `229`; crypto_major avg `-0.1565` n `8`; equity avg `0.0493` n `88`; fx avg `0.0041` n `6`; index avg `-0.0006` n `25`; metal avg `0.0148` n `20`; unknown avg `-0.283` n `765`
- 4h: commodity avg `-0.0512` n `12`; crypto_alt avg `0.1008` n `229`; crypto_major avg `0.0559` n `8`; equity avg `0.01` n `88`; fx avg `-0.0036` n `6`; index avg `-0.0245` n `25`; metal avg `0.0357` n `20`; unknown avg `-0.4878` n `765`
- 24h: commodity avg `-0.0531` n `12`; crypto_alt avg `0.8878` n `229`; crypto_major avg `1.169` n `8`; equity avg `0.1125` n `88`; fx avg `-0.0149` n `6`; index avg `-0.0642` n `25`; metal avg `0.0797` n `20`; unknown avg `0.1312` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
