# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T02:46:02.745017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `13`; crypto_alt avg `0.0169` n `239`; crypto_major avg `-0.0074` n `8`; equity avg `0.012` n `158`; fx avg `-0.0126` n `6`; index avg `0.0067` n `27`; metal avg `0.0076` n `20`; unknown avg `-0.0434` n `1262`
- 1h: commodity avg `0.1765` n `13`; crypto_alt avg `0.2042` n `239`; crypto_major avg `0.1134` n `8`; equity avg `0.5369` n `158`; fx avg `-0.0605` n `6`; index avg `0.0386` n `27`; metal avg `0.0312` n `20`; unknown avg `-0.0738` n `1254`
- 4h: commodity avg `-0.0283` n `13`; crypto_alt avg `1.8125` n `239`; crypto_major avg `1.0302` n `8`; equity avg `1.6988` n `158`; fx avg `-0.0955` n `6`; index avg `0.2569` n `27`; metal avg `0.6359` n `20`; unknown avg `1.9193` n `1228`
- 24h: commodity avg `0.0364` n `13`; crypto_alt avg `-1.0292` n `239`; crypto_major avg `-1.5593` n `8`; equity avg `0.9608` n `158`; fx avg `-0.092` n `6`; index avg `0.1016` n `27`; metal avg `0.537` n `20`; unknown avg `1.3186` n `992`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
