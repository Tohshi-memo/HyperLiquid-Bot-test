# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T19:52:31.997883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.1214` n `234`; crypto_major avg `0.0566` n `8`; equity avg `0.0172` n `140`; fx avg `0.0006` n `6`; index avg `-0.0002` n `26`; metal avg `0.003` n `20`; unknown avg `1.2551` n `935`
- 1h: commodity avg `-0.0168` n `12`; crypto_alt avg `0.3616` n `234`; crypto_major avg `0.0602` n `8`; equity avg `0.0351` n `140`; fx avg `-0.0023` n `6`; index avg `-0.0019` n `26`; metal avg `0.002` n `20`; unknown avg `54.5189` n `933`
- 4h: commodity avg `0.0355` n `12`; crypto_alt avg `0.3505` n `234`; crypto_major avg `-0.2758` n `8`; equity avg `0.0863` n `140`; fx avg `-0.0073` n `6`; index avg `0.0143` n `26`; metal avg `-0.0027` n `20`; unknown avg `167.6261` n `875`
- 24h: commodity avg `0.0111` n `12`; crypto_alt avg `1.8684` n `234`; crypto_major avg `0.1227` n `8`; equity avg `0.1233` n `140`; fx avg `-0.0036` n `6`; index avg `0.0351` n `26`; metal avg `-0.0239` n `20`; unknown avg `5.9783` n `784`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
