# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T08:37:34.487063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.0062` n `239`; crypto_major avg `-0.0616` n `8`; equity avg `0.1178` n `164`; fx avg `0.004` n `6`; index avg `0.0182` n `27`; metal avg `0.0304` n `20`; unknown avg `9.7787` n `1264`
- 1h: commodity avg `-0.0592` n `13`; crypto_alt avg `0.0906` n `239`; crypto_major avg `-0.0186` n `8`; equity avg `0.2197` n `164`; fx avg `0.0223` n `6`; index avg `0.0333` n `27`; metal avg `0.0215` n `20`; unknown avg `113.9389` n `1224`
- 4h: commodity avg `-0.0707` n `13`; crypto_alt avg `-0.0165` n `239`; crypto_major avg `0.3819` n `8`; equity avg `1.1179` n `164`; fx avg `0.0591` n `6`; index avg `0.1816` n `27`; metal avg `0.0892` n `20`; unknown avg `77.1671` n `1202`
- 24h: commodity avg `0.1831` n `13`; crypto_alt avg `0.108` n `239`; crypto_major avg `-0.7633` n `8`; equity avg `0.3448` n `164`; fx avg `0.0483` n `6`; index avg `0.1916` n `27`; metal avg `-0.121` n `20`; unknown avg `3.6851` n `1121`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
