# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T00:37:28.476245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.2886` n `239`; crypto_major avg `-0.1407` n `8`; equity avg `-0.1071` n `166`; fx avg `0.0357` n `6`; index avg `-0.0622` n `27`; metal avg `0.0478` n `20`; unknown avg `-0.0556` n `1266`
- 1h: commodity avg `0.048` n `13`; crypto_alt avg `0.0206` n `239`; crypto_major avg `-0.1566` n `8`; equity avg `0.0906` n `166`; fx avg `0.0289` n `6`; index avg `0.0919` n `27`; metal avg `0.1768` n `20`; unknown avg `158.5974` n `1258`
- 4h: commodity avg `0.1009` n `13`; crypto_alt avg `-0.2954` n `239`; crypto_major avg `-0.4335` n `8`; equity avg `-0.0589` n `166`; fx avg `0.0209` n `6`; index avg `0.0371` n `27`; metal avg `0.1158` n `20`; unknown avg `-0.6097` n `1216`
- 24h: commodity avg `-1.0416` n `13`; crypto_alt avg `0.9562` n `239`; crypto_major avg `0.7899` n `8`; equity avg `5.4243` n `166`; fx avg `-0.1409` n `6`; index avg `0.5282` n `27`; metal avg `0.5344` n `20`; unknown avg `298.9571` n `1049`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
