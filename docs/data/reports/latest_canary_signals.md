# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T00:37:29.457912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `13`; crypto_alt avg `0.0191` n `239`; crypto_major avg `-0.1339` n `8`; equity avg `-0.1022` n `158`; fx avg `-0.0033` n `6`; index avg `-0.0269` n `27`; metal avg `-0.0132` n `20`; unknown avg `5.2371` n `1264`
- 1h: commodity avg `-0.0407` n `13`; crypto_alt avg `-0.1275` n `239`; crypto_major avg `0.049` n `8`; equity avg `-0.4047` n `158`; fx avg `0.0147` n `6`; index avg `-0.1302` n `27`; metal avg `0.0922` n `20`; unknown avg `1.1534` n `1252`
- 4h: commodity avg `-0.1384` n `13`; crypto_alt avg `0.3258` n `239`; crypto_major avg `0.3963` n `8`; equity avg `-0.311` n `158`; fx avg `0.0107` n `6`; index avg `-0.1013` n `27`; metal avg `0.0344` n `20`; unknown avg `0.8025` n `1154`
- 24h: commodity avg `-1.8561` n `13`; crypto_alt avg `3.0494` n `239`; crypto_major avg `3.6907` n `8`; equity avg `-0.5893` n `158`; fx avg `0.0481` n `6`; index avg `0.1485` n `27`; metal avg `1.4426` n `20`; unknown avg `31.2363` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2644`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
