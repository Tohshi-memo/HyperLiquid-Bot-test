# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T00:52:30.607596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.0158` n `239`; crypto_major avg `-0.0472` n `8`; equity avg `0.1237` n `168`; fx avg `-0.0196` n `6`; index avg `0.0235` n `27`; metal avg `0.0416` n `20`; unknown avg `23.7125` n `1265`
- 1h: commodity avg `0.0415` n `13`; crypto_alt avg `-0.1812` n `239`; crypto_major avg `-0.3303` n `8`; equity avg `-0.3843` n `168`; fx avg `0.0183` n `6`; index avg `-0.0377` n `27`; metal avg `-0.023` n `20`; unknown avg `84.8074` n `1225`
- 4h: commodity avg `0.0655` n `13`; crypto_alt avg `-0.4438` n `239`; crypto_major avg `-0.3652` n `8`; equity avg `-0.8666` n `168`; fx avg `0.0272` n `6`; index avg `-0.0977` n `27`; metal avg `-0.0425` n `20`; unknown avg `86.7841` n `1147`
- 24h: commodity avg `0.6009` n `13`; crypto_alt avg `-3.0642` n `239`; crypto_major avg `-2.756` n `8`; equity avg `-4.8554` n `167`; fx avg `0.2037` n `6`; index avg `-0.4038` n `27`; metal avg `-1.3168` n `20`; unknown avg `492.7463` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
