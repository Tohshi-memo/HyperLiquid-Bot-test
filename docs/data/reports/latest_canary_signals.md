# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T21:22:27.105127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `13`; crypto_alt avg `-0.1071` n `239`; crypto_major avg `-0.0452` n `8`; equity avg `-0.0125` n `158`; fx avg `0.0042` n `6`; index avg `-0.0158` n `27`; metal avg `0.0134` n `20`; unknown avg `3.662` n `1262`
- 1h: commodity avg `0.0115` n `13`; crypto_alt avg `-0.1464` n `239`; crypto_major avg `-0.2425` n `8`; equity avg `-0.2677` n `158`; fx avg `-0.0102` n `6`; index avg `-0.0628` n `27`; metal avg `0.0023` n `20`; unknown avg `1.232` n `1232`
- 4h: commodity avg `-0.1441` n `13`; crypto_alt avg `0.1448` n `239`; crypto_major avg `-0.1135` n `8`; equity avg `-0.1474` n `158`; fx avg `-0.0281` n `6`; index avg `-0.0547` n `27`; metal avg `0.0259` n `20`; unknown avg `13.4145` n `1164`
- 24h: commodity avg `-0.0837` n `13`; crypto_alt avg `-1.0781` n `239`; crypto_major avg `-0.0894` n `8`; equity avg `0.1096` n `158`; fx avg `0.0459` n `6`; index avg `-0.0524` n `27`; metal avg `-0.0107` n `20`; unknown avg `-0.0728` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
