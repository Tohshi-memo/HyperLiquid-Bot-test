# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T13:37:46.011029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1477` n `13`; crypto_alt avg `0.2833` n `239`; crypto_major avg `0.0762` n `8`; equity avg `0.0336` n `166`; fx avg `-0.0107` n `6`; index avg `0.0026` n `27`; metal avg `-0.0712` n `20`; unknown avg `-0.0604` n `1267`
- 1h: commodity avg `0.1546` n `13`; crypto_alt avg `-0.4475` n `239`; crypto_major avg `-0.4527` n `8`; equity avg `-0.2684` n `166`; fx avg `0.0251` n `6`; index avg `-0.0396` n `27`; metal avg `-0.1132` n `20`; unknown avg `159.6927` n `1257`
- 4h: commodity avg `0.1799` n `13`; crypto_alt avg `-1.2593` n `239`; crypto_major avg `-0.5025` n `8`; equity avg `-1.0098` n `166`; fx avg `0.0976` n `6`; index avg `-0.1917` n `27`; metal avg `0.0727` n `20`; unknown avg `479.178` n `1218`
- 24h: commodity avg `-0.1435` n `13`; crypto_alt avg `-1.9324` n `239`; crypto_major avg `-1.651` n `8`; equity avg `1.1127` n `166`; fx avg `0.0288` n `6`; index avg `0.2425` n `27`; metal avg `-0.2282` n `20`; unknown avg `175.0894` n `1140`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
