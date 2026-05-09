# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T20:07:14.800549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.0726` n `228`; crypto_major avg `-0.1106` n `8`; equity avg `0.1814` n `65`; fx avg `0.0008` n `5`; index avg `0.035` n `23`; metal avg `0.0015` n `18`; unknown avg `0.0616` n `376`
- 1h: commodity avg `0.0134` n `12`; crypto_alt avg `-0.0399` n `228`; crypto_major avg `-0.027` n `8`; equity avg `0.1191` n `65`; fx avg `0.0002` n `5`; index avg `0.0048` n `23`; metal avg `0.0483` n `18`; unknown avg `-0.0928` n `376`
- 4h: commodity avg `0.0324` n `12`; crypto_alt avg `0.7905` n `228`; crypto_major avg `0.3437` n `8`; equity avg `0.293` n `65`; fx avg `-0.0108` n `5`; index avg `0.0531` n `23`; metal avg `0.1384` n `18`; unknown avg `0.1018` n `376`
- 24h: commodity avg `0.3214` n `12`; crypto_alt avg `0.7535` n `228`; crypto_major avg `0.5195` n `8`; equity avg `0.8335` n `65`; fx avg `-0.0453` n `5`; index avg `0.3048` n `23`; metal avg `-0.0881` n `18`; unknown avg `0.2295` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
