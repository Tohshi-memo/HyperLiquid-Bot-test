# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T10:37:35.718561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `13`; crypto_alt avg `0.0008` n `239`; crypto_major avg `0.0446` n `8`; equity avg `0.1359` n `162`; fx avg `-0.0027` n `6`; index avg `0.0061` n `27`; metal avg `0.0061` n `20`; unknown avg `0.5586` n `1261`
- 1h: commodity avg `-0.0461` n `13`; crypto_alt avg `0.2594` n `239`; crypto_major avg `0.2731` n `8`; equity avg `0.0328` n `162`; fx avg `-0.009` n `6`; index avg `0.0019` n `27`; metal avg `0.043` n `20`; unknown avg `0.7276` n `1255`
- 4h: commodity avg `0.0022` n `13`; crypto_alt avg `0.1942` n `239`; crypto_major avg `0.3202` n `8`; equity avg `0.705` n `162`; fx avg `0.0463` n `6`; index avg `0.0657` n `27`; metal avg `-0.1605` n `20`; unknown avg `3.3178` n `1237`
- 24h: commodity avg `-0.142` n `13`; crypto_alt avg `-1.7251` n `239`; crypto_major avg `-0.9352` n `8`; equity avg `-0.5345` n `162`; fx avg `-0.0866` n `6`; index avg `-0.0058` n `27`; metal avg `-0.8648` n `20`; unknown avg `2.9488` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
