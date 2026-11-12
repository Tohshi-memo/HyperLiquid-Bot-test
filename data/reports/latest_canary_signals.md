# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T09:22:34.535718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.046` n `13`; crypto_alt avg `0.012` n `239`; crypto_major avg `-0.027` n `8`; equity avg `0.1353` n `161`; fx avg `-0.0065` n `6`; index avg `0.016` n `27`; metal avg `0.0173` n `20`; unknown avg `-0.0559` n `1262`
- 1h: commodity avg `-0.104` n `13`; crypto_alt avg `-0.1729` n `239`; crypto_major avg `-0.2304` n `8`; equity avg `0.0862` n `161`; fx avg `-0.0124` n `6`; index avg `0.0181` n `27`; metal avg `-0.1861` n `20`; unknown avg `0.4717` n `1256`
- 4h: commodity avg `0.2519` n `13`; crypto_alt avg `-0.3001` n `239`; crypto_major avg `-0.1791` n `8`; equity avg `0.3142` n `161`; fx avg `0.0976` n `6`; index avg `0.0255` n `27`; metal avg `-0.1929` n `20`; unknown avg `60.9041` n `1206`
- 24h: commodity avg `0.1816` n `13`; crypto_alt avg `-1.5294` n `239`; crypto_major avg `-0.8378` n `8`; equity avg `-0.6488` n `161`; fx avg `-0.0621` n `6`; index avg `-0.032` n `27`; metal avg `-0.8168` n `20`; unknown avg `18.5434` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
