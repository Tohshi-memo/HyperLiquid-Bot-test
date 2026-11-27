# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T11:22:24.251312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0591` n `13`; crypto_alt avg `0.0483` n `239`; crypto_major avg `0.195` n `8`; equity avg `-0.0133` n `168`; fx avg `-0.0131` n `6`; index avg `0.0052` n `27`; metal avg `-0.0399` n `20`; unknown avg `0.1319` n `1261`
- 1h: commodity avg `-0.0543` n `13`; crypto_alt avg `0.0388` n `239`; crypto_major avg `0.1513` n `8`; equity avg `0.0192` n `168`; fx avg `-0.0026` n `6`; index avg `0.0155` n `27`; metal avg `-0.0188` n `20`; unknown avg `0.1131` n `1255`
- 4h: commodity avg `-0.202` n `13`; crypto_alt avg `-0.175` n `239`; crypto_major avg `0.0646` n `8`; equity avg `0.2589` n `168`; fx avg `-0.039` n `6`; index avg `0.0202` n `27`; metal avg `-0.0033` n `20`; unknown avg `179.6063` n `1119`
- 24h: commodity avg `0.108` n `13`; crypto_alt avg `1.69` n `239`; crypto_major avg `3.0123` n `8`; equity avg `3.9274` n `168`; fx avg `-0.084` n `6`; index avg `0.306` n `27`; metal avg `1.2013` n `20`; unknown avg `261.1603` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
