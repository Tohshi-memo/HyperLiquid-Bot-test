# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T05:37:29.649296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `13`; crypto_alt avg `0.0142` n `239`; crypto_major avg `0.0955` n `8`; equity avg `0.0046` n `158`; fx avg `-0.001` n `6`; index avg `0.0013` n `27`; metal avg `0.0033` n `20`; unknown avg `73.179` n `1261`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `0.0134` n `239`; crypto_major avg `0.0778` n `8`; equity avg `-0.0781` n `158`; fx avg `-0.0012` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0024` n `20`; unknown avg `73.5388` n `1251`
- 4h: commodity avg `-0.0881` n `13`; crypto_alt avg `-0.3228` n `239`; crypto_major avg `-0.2972` n `8`; equity avg `0.0433` n `158`; fx avg `-0.0003` n `6`; index avg `0.0026` n `27`; metal avg `-0.0041` n `20`; unknown avg `-0.3618` n `1233`
- 24h: commodity avg `-0.219` n `13`; crypto_alt avg `0.5236` n `239`; crypto_major avg `0.2438` n `8`; equity avg `1.1569` n `158`; fx avg `-0.0746` n `6`; index avg `0.1233` n `27`; metal avg `0.251` n `20`; unknown avg `8.5208` n `1010`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
