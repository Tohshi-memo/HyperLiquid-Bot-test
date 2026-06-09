# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T07:37:25.138020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.3609` n `228`; crypto_major avg `-0.4533` n `8`; equity avg `-0.154` n `74`; fx avg `-0.0072` n `6`; index avg `-0.094` n `23`; metal avg `0.0393` n `18`; unknown avg `0.0202` n `547`
- 1h: commodity avg `0.1315` n `12`; crypto_alt avg `-0.299` n `228`; crypto_major avg `-0.4472` n `8`; equity avg `-0.2516` n `74`; fx avg `0.0314` n `6`; index avg `-0.085` n `23`; metal avg `-0.0247` n `18`; unknown avg `0.1996` n `547`
- 4h: commodity avg `0.0413` n `12`; crypto_alt avg `1.5721` n `228`; crypto_major avg `0.7863` n `8`; equity avg `0.5882` n `74`; fx avg `0.0159` n `6`; index avg `0.2482` n `23`; metal avg `0.2691` n `18`; unknown avg `0.3198` n `503`
- 24h: commodity avg `-1.1518` n `12`; crypto_alt avg `0.0987` n `228`; crypto_major avg `0.387` n `8`; equity avg `2.3794` n `74`; fx avg `-0.0915` n `6`; index avg `1.0311` n `23`; metal avg `0.498` n `18`; unknown avg `-2.8377` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
