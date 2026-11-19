# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T05:07:30.736207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0384` n `13`; crypto_alt avg `-0.1185` n `239`; crypto_major avg `0.0199` n `8`; equity avg `0.1568` n `164`; fx avg `0.014` n `6`; index avg `0.018` n `27`; metal avg `0.1082` n `20`; unknown avg `4.2805` n `1260`
- 1h: commodity avg `0.0577` n `13`; crypto_alt avg `-0.3675` n `239`; crypto_major avg `0.1282` n `8`; equity avg `-0.2697` n `164`; fx avg `0.0252` n `6`; index avg `-0.0369` n `27`; metal avg `0.0781` n `20`; unknown avg `-0.101` n `1256`
- 4h: commodity avg `0.0523` n `13`; crypto_alt avg `0.3244` n `239`; crypto_major avg `0.5631` n `8`; equity avg `-0.3593` n `164`; fx avg `0.0` n `6`; index avg `-0.0145` n `27`; metal avg `-0.1718` n `20`; unknown avg `2.5758` n `1237`
- 24h: commodity avg `0.2596` n `13`; crypto_alt avg `0.7281` n `239`; crypto_major avg `-0.4043` n `8`; equity avg `0.0959` n `164`; fx avg `-0.0763` n `6`; index avg `0.1091` n `27`; metal avg `-0.4068` n `20`; unknown avg `217.6482` n `1117`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
