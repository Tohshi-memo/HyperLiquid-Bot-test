# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T10:37:33.585988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0289` n `13`; crypto_alt avg `-0.0778` n `239`; crypto_major avg `-0.1455` n `8`; equity avg `-0.2031` n `160`; fx avg `0.0176` n `6`; index avg `-0.0227` n `27`; metal avg `-0.0267` n `20`; unknown avg `0.0701` n `1262`
- 1h: commodity avg `0.0899` n `13`; crypto_alt avg `-0.3828` n `239`; crypto_major avg `-0.3679` n `8`; equity avg `-0.2985` n `160`; fx avg `0.0249` n `6`; index avg `-0.0381` n `27`; metal avg `-0.0527` n `20`; unknown avg `0.2217` n `1256`
- 4h: commodity avg `-0.3399` n `13`; crypto_alt avg `-0.4268` n `239`; crypto_major avg `-0.8453` n `8`; equity avg `-0.0731` n `160`; fx avg `-0.0016` n `6`; index avg `-0.0414` n `27`; metal avg `-0.2828` n `20`; unknown avg `19.9006` n `1219`
- 24h: commodity avg `-0.851` n `13`; crypto_alt avg `0.9102` n `239`; crypto_major avg `0.1638` n `8`; equity avg `4.0381` n `160`; fx avg `-0.0517` n `6`; index avg `0.437` n `27`; metal avg `0.0013` n `20`; unknown avg `5.5148` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2312`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
