# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T19:52:26.047095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.037` n `13`; crypto_alt avg `-0.0266` n `239`; crypto_major avg `-0.0611` n `8`; equity avg `-0.0169` n `158`; fx avg `0.0021` n `6`; index avg `-0.0011` n `27`; metal avg `0.0009` n `20`; unknown avg `0.753` n `1262`
- 1h: commodity avg `0.0257` n `13`; crypto_alt avg `-0.3461` n `239`; crypto_major avg `-0.1565` n `8`; equity avg `-0.0472` n `158`; fx avg `-0.0038` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0096` n `20`; unknown avg `1.0535` n `1256`
- 4h: commodity avg `0.0532` n `13`; crypto_alt avg `0.1295` n `239`; crypto_major avg `0.1832` n `8`; equity avg `0.1611` n `158`; fx avg `-0.0055` n `6`; index avg `0.0182` n `27`; metal avg `0.0016` n `20`; unknown avg `0.5964` n `1217`
- 24h: commodity avg `-0.0182` n `13`; crypto_alt avg `-1.4693` n `239`; crypto_major avg `-0.5786` n `8`; equity avg `0.2716` n `158`; fx avg `-0.0003` n `6`; index avg `0.0373` n `27`; metal avg `0.0438` n `20`; unknown avg `0.1564` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
