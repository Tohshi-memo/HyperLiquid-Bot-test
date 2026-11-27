# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T12:37:29.877670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `13`; crypto_alt avg `0.0386` n `239`; crypto_major avg `-0.1253` n `8`; equity avg `0.0204` n `168`; fx avg `-0.0056` n `6`; index avg `0.0006` n `27`; metal avg `-0.0348` n `20`; unknown avg `0.5054` n `1263`
- 1h: commodity avg `-0.1635` n `13`; crypto_alt avg `0.1441` n `239`; crypto_major avg `-0.2502` n `8`; equity avg `-0.2309` n `168`; fx avg `0.0294` n `6`; index avg `-0.0074` n `27`; metal avg `-0.1493` n `20`; unknown avg `0.0849` n `1251`
- 4h: commodity avg `-0.2799` n `13`; crypto_alt avg `0.0666` n `239`; crypto_major avg `-0.0741` n `8`; equity avg `-0.3975` n `168`; fx avg `0.0222` n `6`; index avg `-0.0261` n `27`; metal avg `-0.1631` n `20`; unknown avg `198.5679` n `1169`
- 24h: commodity avg `-0.0354` n `13`; crypto_alt avg `1.8038` n `239`; crypto_major avg `2.5519` n `8`; equity avg `3.1679` n `168`; fx avg `-0.0782` n `6`; index avg `0.2539` n `27`; metal avg `1.0078` n `20`; unknown avg `78.1514` n `1023`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
