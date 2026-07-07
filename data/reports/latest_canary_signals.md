# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T22:37:26.489207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `0.2485` n `229`; crypto_major avg `0.2473` n `8`; equity avg `-0.0004` n `91`; fx avg `-0.0226` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0286` n `20`; unknown avg `0.079` n `763`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `-0.0264` n `229`; crypto_major avg `0.2985` n `8`; equity avg `-0.0069` n `91`; fx avg `-0.0174` n `6`; index avg `-0.0159` n `25`; metal avg `-0.114` n `20`; unknown avg `0.0723` n `763`
- 4h: commodity avg `0.4965` n `12`; crypto_alt avg `-1.427` n `229`; crypto_major avg `-1.1134` n `8`; equity avg `-0.6309` n `91`; fx avg `-0.0174` n `6`; index avg `-0.1323` n `25`; metal avg `-0.4803` n `20`; unknown avg `0.5633` n `761`
- 24h: commodity avg `0.9515` n `12`; crypto_alt avg `-2.8043` n `229`; crypto_major avg `-1.8525` n `8`; equity avg `-3.5501` n `91`; fx avg `-0.2985` n `6`; index avg `-0.6677` n `25`; metal avg `-0.7139` n `20`; unknown avg `-0.2073` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
