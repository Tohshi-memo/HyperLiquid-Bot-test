# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T23:07:25.498593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `13`; crypto_alt avg `-0.1638` n `239`; crypto_major avg `-0.1063` n `8`; equity avg `-0.3614` n `165`; fx avg `-0.0069` n `6`; index avg `-0.0441` n `27`; metal avg `-0.0225` n `20`; unknown avg `0.3631` n `1252`
- 1h: commodity avg `0.0187` n `13`; crypto_alt avg `0.4788` n `239`; crypto_major avg `0.6769` n `8`; equity avg `-0.0886` n `165`; fx avg `-0.0093` n `6`; index avg `-0.0116` n `27`; metal avg `0.0184` n `20`; unknown avg `1.2816` n `1254`
- 4h: commodity avg `-0.0082` n `13`; crypto_alt avg `-0.3955` n `239`; crypto_major avg `-0.8787` n `8`; equity avg `-2.0066` n `165`; fx avg `-0.0366` n `6`; index avg `-0.1185` n `27`; metal avg `-0.3866` n `20`; unknown avg `1.8177` n `1226`
- 24h: commodity avg `0.1239` n `13`; crypto_alt avg `-0.483` n `239`; crypto_major avg `-0.216` n `8`; equity avg `-3.8096` n `165`; fx avg `-0.0416` n `6`; index avg `-0.2703` n `27`; metal avg `-0.9128` n `20`; unknown avg `6.1897` n `1166`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
