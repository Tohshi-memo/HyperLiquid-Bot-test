# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T10:22:41.454676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0382` n `13`; crypto_alt avg `-0.2788` n `239`; crypto_major avg `-0.3382` n `8`; equity avg `0.0627` n `165`; fx avg `-0.0115` n `6`; index avg `0.0052` n `27`; metal avg `0.0155` n `20`; unknown avg `-0.0824` n `1260`
- 1h: commodity avg `-0.1364` n `13`; crypto_alt avg `-0.3854` n `239`; crypto_major avg `-0.3688` n `8`; equity avg `-0.3625` n `165`; fx avg `-0.0157` n `6`; index avg `-0.065` n `27`; metal avg `-0.0468` n `20`; unknown avg `191.5255` n `1254`
- 4h: commodity avg `-0.5499` n `13`; crypto_alt avg `-0.3197` n `239`; crypto_major avg `-0.56` n `8`; equity avg `-0.6772` n `165`; fx avg `-0.0731` n `6`; index avg `-0.0381` n `27`; metal avg `0.0853` n `20`; unknown avg `43.868` n `1192`
- 24h: commodity avg `-0.6531` n `13`; crypto_alt avg `-3.579` n `239`; crypto_major avg `-3.1923` n `8`; equity avg `-7.8202` n `165`; fx avg `-0.1046` n `6`; index avg `-0.8145` n `27`; metal avg `-1.3969` n `20`; unknown avg `52.1924` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
