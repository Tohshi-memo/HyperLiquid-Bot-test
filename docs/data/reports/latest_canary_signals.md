# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T01:07:28.343786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `13`; crypto_alt avg `-0.1687` n `239`; crypto_major avg `-0.1826` n `8`; equity avg `0.1308` n `161`; fx avg `0.0115` n `6`; index avg `-0.0035` n `27`; metal avg `0.0224` n `20`; unknown avg `-0.0236` n `1257`
- 1h: commodity avg `0.0567` n `13`; crypto_alt avg `-0.1866` n `239`; crypto_major avg `-0.4251` n `8`; equity avg `0.4518` n `161`; fx avg `-0.0091` n `6`; index avg `0.0455` n `27`; metal avg `-0.0354` n `20`; unknown avg `19.1536` n `1255`
- 4h: commodity avg `0.0188` n `13`; crypto_alt avg `0.2234` n `239`; crypto_major avg `-0.5323` n `8`; equity avg `0.8232` n `161`; fx avg `-0.0398` n `6`; index avg `0.0948` n `27`; metal avg `0.0267` n `20`; unknown avg `1.3522` n `1243`
- 24h: commodity avg `0.0917` n `13`; crypto_alt avg `-0.6954` n `239`; crypto_major avg `-3.0392` n `8`; equity avg `-0.0491` n `161`; fx avg `-0.1904` n `6`; index avg `0.0367` n `27`; metal avg `-0.6465` n `20`; unknown avg `21.0425` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.266`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
