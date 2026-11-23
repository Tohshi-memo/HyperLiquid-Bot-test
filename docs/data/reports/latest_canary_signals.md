# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T11:37:27.521156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.1082` n `239`; crypto_major avg `0.199` n `8`; equity avg `-0.0029` n `166`; fx avg `0.0038` n `6`; index avg `0.003` n `27`; metal avg `-0.0292` n `20`; unknown avg `158.0274` n `1266`
- 1h: commodity avg `-0.1859` n `13`; crypto_alt avg `0.1457` n `239`; crypto_major avg `0.2491` n `8`; equity avg `-0.0475` n `166`; fx avg `-0.0035` n `6`; index avg `0.0028` n `27`; metal avg `0.0291` n `20`; unknown avg `0.1833` n `1264`
- 4h: commodity avg `-0.3665` n `13`; crypto_alt avg `0.1735` n `239`; crypto_major avg `0.5071` n `8`; equity avg `0.5498` n `166`; fx avg `-0.0607` n `6`; index avg `0.0647` n `27`; metal avg `-0.0733` n `20`; unknown avg `389.2125` n `1108`
- 24h: commodity avg `-0.9738` n `13`; crypto_alt avg `0.7917` n `239`; crypto_major avg `1.2297` n `8`; equity avg `1.9585` n `166`; fx avg `0.2004` n `6`; index avg `0.1369` n `27`; metal avg `0.3924` n `20`; unknown avg `-0.1168` n `1061`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
