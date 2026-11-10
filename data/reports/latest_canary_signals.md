# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T15:22:33.974668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.036` n `13`; crypto_alt avg `-0.2125` n `239`; crypto_major avg `-0.2149` n `8`; equity avg `-0.3415` n `160`; fx avg `-0.0184` n `6`; index avg `-0.034` n `27`; metal avg `0.0133` n `20`; unknown avg `-0.0616` n `1262`
- 1h: commodity avg `0.2551` n `13`; crypto_alt avg `1.0858` n `239`; crypto_major avg `0.7024` n `8`; equity avg `1.8501` n `160`; fx avg `-0.0427` n `6`; index avg `0.1517` n `27`; metal avg `-0.0013` n `20`; unknown avg `2.2882` n `1256`
- 4h: commodity avg `-0.1555` n `13`; crypto_alt avg `1.2678` n `239`; crypto_major avg `-0.0498` n `8`; equity avg `0.3805` n `160`; fx avg `-0.0416` n `6`; index avg `0.04` n `27`; metal avg `-0.1003` n `20`; unknown avg `2.3255` n `1250`
- 24h: commodity avg `-0.5153` n `13`; crypto_alt avg `-0.0697` n `239`; crypto_major avg `-1.8313` n `8`; equity avg `0.6152` n `160`; fx avg `-0.0391` n `6`; index avg `0.0654` n `27`; metal avg `-0.2635` n `20`; unknown avg `1.5665` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2251`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
