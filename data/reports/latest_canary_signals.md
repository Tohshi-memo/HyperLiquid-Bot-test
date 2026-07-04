# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T18:37:25.729049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.1044` n `229`; crypto_major avg `-0.0605` n `8`; equity avg `-0.0188` n `88`; fx avg `0.0026` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.0918` n `765`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.1433` n `229`; crypto_major avg `-0.0837` n `8`; equity avg `-0.039` n `88`; fx avg `-0.0025` n `6`; index avg `0.0036` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.4984` n `765`
- 4h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.7739` n `229`; crypto_major avg `0.662` n `8`; equity avg `-0.0035` n `88`; fx avg `0.0097` n `6`; index avg `-0.0223` n `25`; metal avg `0.021` n `20`; unknown avg `-0.0095` n `765`
- 24h: commodity avg `-0.0091` n `12`; crypto_alt avg `1.2845` n `229`; crypto_major avg `1.6647` n `8`; equity avg `0.1701` n `88`; fx avg `-0.013` n `6`; index avg `-0.0722` n `25`; metal avg `0.0458` n `20`; unknown avg `0.9741` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
