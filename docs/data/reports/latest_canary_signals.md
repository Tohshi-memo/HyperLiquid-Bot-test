# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T06:52:31.606937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.054` n `13`; crypto_alt avg `0.1658` n `239`; crypto_major avg `0.2568` n `8`; equity avg `0.2903` n `166`; fx avg `-0.0025` n `6`; index avg `0.0367` n `27`; metal avg `0.1494` n `20`; unknown avg `162.4702` n `1264`
- 1h: commodity avg `0.0116` n `13`; crypto_alt avg `-0.2762` n `239`; crypto_major avg `-0.3141` n `8`; equity avg `-0.0199` n `166`; fx avg `0.0282` n `6`; index avg `-0.0088` n `27`; metal avg `-0.0293` n `20`; unknown avg `327.1388` n `1226`
- 4h: commodity avg `0.0225` n `13`; crypto_alt avg `1.3124` n `239`; crypto_major avg `0.9303` n `8`; equity avg `0.1975` n `166`; fx avg `0.0478` n `6`; index avg `0.0336` n `27`; metal avg `-0.1756` n `20`; unknown avg `165.7739` n `1206`
- 24h: commodity avg `-1.0542` n `13`; crypto_alt avg `0.8237` n `239`; crypto_major avg `0.1735` n `8`; equity avg `4.5434` n `166`; fx avg `-0.2099` n `6`; index avg `0.6883` n `27`; metal avg `-0.2077` n `20`; unknown avg `688.1544` n `1036`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
