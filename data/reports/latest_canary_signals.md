# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T23:52:28.609193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.012` n `13`; crypto_alt avg `0.3169` n `239`; crypto_major avg `0.2972` n `8`; equity avg `-0.0484` n `164`; fx avg `-0.0102` n `6`; index avg `-0.0087` n `27`; metal avg `-0.031` n `20`; unknown avg `0.2601` n `1265`
- 1h: commodity avg `0.0416` n `13`; crypto_alt avg `1.5408` n `239`; crypto_major avg `1.4479` n `8`; equity avg `1.1577` n `164`; fx avg `-0.0084` n `6`; index avg `0.1253` n `27`; metal avg `0.1651` n `20`; unknown avg `2.6542` n `1263`
- 4h: commodity avg `-0.1442` n `13`; crypto_alt avg `0.7639` n `239`; crypto_major avg `0.6004` n `8`; equity avg `1.1182` n `164`; fx avg `0.0042` n `6`; index avg `0.1336` n `27`; metal avg `0.1934` n `20`; unknown avg `162.9441` n `1219`
- 24h: commodity avg `-0.2511` n `13`; crypto_alt avg `-1.0772` n `239`; crypto_major avg `-2.0038` n `8`; equity avg `-1.7735` n `164`; fx avg `-0.1455` n `6`; index avg `-0.1138` n `27`; metal avg `-1.0742` n `20`; unknown avg `72.168` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
