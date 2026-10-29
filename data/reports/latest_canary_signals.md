# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T00:37:28.524828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0536` n `13`; crypto_alt avg `-0.0867` n `238`; crypto_major avg `-0.0252` n `8`; equity avg `0.0038` n `155`; fx avg `-0.0412` n `6`; index avg `-0.0084` n `27`; metal avg `-0.0124` n `20`; unknown avg `-0.0721` n `1238`
- 1h: commodity avg `0.0351` n `13`; crypto_alt avg `-0.0307` n `238`; crypto_major avg `-0.198` n `8`; equity avg `0.364` n `155`; fx avg `-0.0966` n `6`; index avg `0.0786` n `27`; metal avg `-0.1019` n `20`; unknown avg `1.3628` n `1212`
- 4h: commodity avg `-0.0087` n `13`; crypto_alt avg `-0.1425` n `238`; crypto_major avg `-0.0826` n `8`; equity avg `0.1603` n `155`; fx avg `-0.1122` n `6`; index avg `0.0133` n `27`; metal avg `-0.1088` n `20`; unknown avg `2.1516` n `1140`
- 24h: commodity avg `0.0635` n `13`; crypto_alt avg `0.4979` n `238`; crypto_major avg `0.4703` n `8`; equity avg `0.9627` n `154`; fx avg `0.0915` n `6`; index avg `0.1746` n `27`; metal avg `-0.2149` n `20`; unknown avg `24.6389` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
