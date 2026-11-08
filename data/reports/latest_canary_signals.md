# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T16:07:56.520651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `13`; crypto_alt avg `-0.0366` n `239`; crypto_major avg `0.003` n `8`; equity avg `0.011` n `158`; fx avg `0.0201` n `6`; index avg `-0.0012` n `27`; metal avg `0.0028` n `20`; unknown avg `0.3271` n `1242`
- 1h: commodity avg `0.0004` n `13`; crypto_alt avg `0.1404` n `239`; crypto_major avg `0.0091` n `8`; equity avg `-0.0523` n `158`; fx avg `0.029` n `6`; index avg `-0.0045` n `27`; metal avg `-0.017` n `20`; unknown avg `0.0068` n `1242`
- 4h: commodity avg `0.0213` n `13`; crypto_alt avg `-0.4667` n `239`; crypto_major avg `-0.0908` n `8`; equity avg `-0.0803` n `158`; fx avg `0.0208` n `6`; index avg `-0.0179` n `27`; metal avg `-0.04` n `20`; unknown avg `1.0426` n `1234`
- 24h: commodity avg `0.0935` n `13`; crypto_alt avg `-1.1513` n `239`; crypto_major avg `0.0836` n `8`; equity avg `0.205` n `158`; fx avg `0.07` n `6`; index avg `-0.0237` n `27`; metal avg `-0.0523` n `20`; unknown avg `8.4183` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
