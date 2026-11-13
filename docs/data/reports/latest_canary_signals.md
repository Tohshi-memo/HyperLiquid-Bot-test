# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T00:37:27.724625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `13`; crypto_alt avg `-0.2728` n `239`; crypto_major avg `-0.3955` n `8`; equity avg `-0.3804` n `162`; fx avg `0.0025` n `6`; index avg `-0.0277` n `27`; metal avg `-0.0179` n `20`; unknown avg `-0.2722` n `1261`
- 1h: commodity avg `-0.0797` n `13`; crypto_alt avg `-0.1576` n `239`; crypto_major avg `-0.1801` n `8`; equity avg `-0.002` n `162`; fx avg `0.0056` n `6`; index avg `0.015` n `27`; metal avg `0.0289` n `20`; unknown avg `0.4748` n `1253`
- 4h: commodity avg `-0.0688` n `13`; crypto_alt avg `0.3268` n `239`; crypto_major avg `0.1353` n `8`; equity avg `1.0942` n `162`; fx avg `-0.0084` n `6`; index avg `0.1276` n `27`; metal avg `0.0754` n `20`; unknown avg `192.8008` n `1193`
- 24h: commodity avg `0.8215` n `13`; crypto_alt avg `-1.2394` n `239`; crypto_major avg `-2.1094` n `8`; equity avg `-0.3985` n `162`; fx avg `-0.0821` n `6`; index avg `0.0774` n `27`; metal avg `-0.5952` n `20`; unknown avg `51.0858` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
