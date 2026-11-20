# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T13:52:39.960088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0476` n `13`; crypto_alt avg `0.5843` n `239`; crypto_major avg `0.8223` n `8`; equity avg `0.7428` n `165`; fx avg `-0.0053` n `6`; index avg `0.0826` n `27`; metal avg `0.1399` n `20`; unknown avg `3.9553` n `1262`
- 1h: commodity avg `0.1123` n `13`; crypto_alt avg `-0.1607` n `239`; crypto_major avg `-0.0181` n `8`; equity avg `0.1484` n `165`; fx avg `0.0061` n `6`; index avg `0.0194` n `27`; metal avg `0.0098` n `20`; unknown avg `159.1096` n `1258`
- 4h: commodity avg `0.5579` n `13`; crypto_alt avg `-1.0073` n `239`; crypto_major avg `-0.7411` n `8`; equity avg `-0.1668` n `165`; fx avg `0.0357` n `6`; index avg `-0.0225` n `27`; metal avg `0.0815` n `20`; unknown avg `17.6866` n `1250`
- 24h: commodity avg `-0.2365` n `13`; crypto_alt avg `-4.5013` n `239`; crypto_major avg `-4.1765` n `8`; equity avg `-7.9722` n `165`; fx avg `-0.029` n `6`; index avg `-0.7919` n `27`; metal avg `-1.2163` n `20`; unknown avg `29.0493` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
