# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T06:37:32.801476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `13`; crypto_alt avg `0.1716` n `239`; crypto_major avg `0.2609` n `8`; equity avg `0.0667` n `166`; fx avg `0.0117` n `6`; index avg `0.0055` n `27`; metal avg `0.0055` n `20`; unknown avg `0.0474` n `1259`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `0.5325` n `239`; crypto_major avg `0.6334` n `8`; equity avg `0.1822` n `166`; fx avg `0.0106` n `6`; index avg `0.0189` n `27`; metal avg `0.0428` n `20`; unknown avg `0.9874` n `1231`
- 4h: commodity avg `-0.0635` n `13`; crypto_alt avg `-0.1922` n `239`; crypto_major avg `-0.6984` n `8`; equity avg `-0.1915` n `166`; fx avg `0.0017` n `6`; index avg `-0.0302` n `27`; metal avg `-0.0585` n `20`; unknown avg `0.618` n `1223`
- 24h: commodity avg `-0.0464` n `13`; crypto_alt avg `2.8003` n `239`; crypto_major avg `3.9447` n `8`; equity avg `1.2167` n `166`; fx avg `0.0769` n `6`; index avg `0.1518` n `27`; metal avg `0.1263` n `20`; unknown avg `422.2007` n `1074`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
