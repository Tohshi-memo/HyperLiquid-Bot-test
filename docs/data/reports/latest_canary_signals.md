# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T12:03:58.466324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `13`; crypto_alt avg `0.0943` n `239`; crypto_major avg `0.0537` n `8`; equity avg `-0.1096` n `168`; fx avg `0.0242` n `6`; index avg `-0.0` n `27`; metal avg `-0.0212` n `20`; unknown avg `0.7749` n `1241`
- 1h: commodity avg `-0.0276` n `13`; crypto_alt avg `0.0894` n `239`; crypto_major avg `0.0053` n `8`; equity avg `-0.7015` n `168`; fx avg `0.011` n `6`; index avg `-0.0596` n `27`; metal avg `-0.1186` n `20`; unknown avg `1.3101` n `1245`
- 4h: commodity avg `-0.2382` n `13`; crypto_alt avg `-0.0468` n `239`; crypto_major avg `-0.1539` n `8`; equity avg `-0.4473` n `168`; fx avg `0.0068` n `6`; index avg `-0.0371` n `27`; metal avg `-0.0902` n `20`; unknown avg `177.7702` n `1133`
- 24h: commodity avg `0.1008` n `13`; crypto_alt avg `1.5978` n `239`; crypto_major avg `2.6531` n `8`; equity avg `2.961` n `168`; fx avg `-0.0685` n `6`; index avg `0.2099` n `27`; metal avg `1.0771` n `20`; unknown avg `41.8756` n `1023`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
