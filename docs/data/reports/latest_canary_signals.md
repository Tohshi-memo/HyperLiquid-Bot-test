# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T00:52:23.757504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `13`; crypto_alt avg `-0.2472` n `239`; crypto_major avg `-0.3069` n `8`; equity avg `0.3222` n `161`; fx avg `0.0065` n `6`; index avg `0.0439` n `27`; metal avg `-0.034` n `20`; unknown avg `18.8711` n `1261`
- 1h: commodity avg `0.0413` n `13`; crypto_alt avg `0.077` n `239`; crypto_major avg `-0.1806` n `8`; equity avg `0.3084` n `161`; fx avg `-0.0502` n `6`; index avg `0.0603` n `27`; metal avg `-0.0507` n `20`; unknown avg `0.6244` n `1247`
- 4h: commodity avg `-0.0228` n `13`; crypto_alt avg `0.5941` n `239`; crypto_major avg `-0.1768` n `8`; equity avg `0.8663` n `161`; fx avg `-0.0536` n `6`; index avg `0.1234` n `27`; metal avg `-0.0246` n `20`; unknown avg `1.7234` n `1227`
- 24h: commodity avg `0.0756` n `13`; crypto_alt avg `-0.4434` n `239`; crypto_major avg `-2.5887` n `8`; equity avg `-0.2408` n `161`; fx avg `-0.1971` n `6`; index avg `0.0299` n `27`; metal avg `-0.5255` n `20`; unknown avg `21.2749` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.263`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
