# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T00:07:25.383565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `-0.2707` n `239`; crypto_major avg `-0.4595` n `8`; equity avg `0.0325` n `164`; fx avg `-0.0307` n `6`; index avg `0.0056` n `27`; metal avg `-0.0033` n `20`; unknown avg `1.34` n `1253`
- 1h: commodity avg `0.0405` n `13`; crypto_alt avg `0.5474` n `239`; crypto_major avg `0.289` n `8`; equity avg `0.5002` n `164`; fx avg `-0.0361` n `6`; index avg `0.0415` n `27`; metal avg `0.0709` n `20`; unknown avg `1.6954` n `1255`
- 4h: commodity avg `-0.1051` n `13`; crypto_alt avg `0.4054` n `239`; crypto_major avg `0.1558` n `8`; equity avg `0.9157` n `164`; fx avg `-0.0292` n `6`; index avg `0.1261` n `27`; metal avg `0.1477` n `20`; unknown avg `2.3305` n `1221`
- 24h: commodity avg `-0.2564` n `13`; crypto_alt avg `-1.3075` n `239`; crypto_major avg `-2.43` n `8`; equity avg `-1.9028` n `164`; fx avg `-0.1303` n `6`; index avg `-0.1302` n `27`; metal avg `-1.0068` n `20`; unknown avg `130.8847` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
