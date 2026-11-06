# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T14:07:26.693562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0467` n `13`; crypto_alt avg `-0.3189` n `239`; crypto_major avg `-0.3851` n `8`; equity avg `-0.3773` n `158`; fx avg `0.0024` n `6`; index avg `-0.0804` n `27`; metal avg `-0.1116` n `20`; unknown avg `111.3464` n `1251`
- 1h: commodity avg `-0.0761` n `13`; crypto_alt avg `-0.2369` n `239`; crypto_major avg `-0.3001` n `8`; equity avg `-0.105` n `158`; fx avg `-0.041` n `6`; index avg `-0.0141` n `27`; metal avg `-0.2194` n `20`; unknown avg `150.9063` n `1253`
- 4h: commodity avg `0.114` n `13`; crypto_alt avg `-0.0629` n `239`; crypto_major avg `-0.3201` n `8`; equity avg `0.1103` n `158`; fx avg `0.0349` n `6`; index avg `-0.0145` n `27`; metal avg `-0.2056` n `20`; unknown avg `266.8141` n `1176`
- 24h: commodity avg `0.4893` n `13`; crypto_alt avg `-2.6323` n `239`; crypto_major avg `-4.8782` n `8`; equity avg `-3.6832` n `158`; fx avg `-0.0397` n `6`; index avg `-0.5711` n `27`; metal avg `-0.7137` n `20`; unknown avg `89.767` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
