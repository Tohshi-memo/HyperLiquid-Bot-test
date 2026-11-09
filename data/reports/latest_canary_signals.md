# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T13:52:32.260234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `13`; crypto_alt avg `-0.0367` n `239`; crypto_major avg `0.0498` n `8`; equity avg `0.1743` n `158`; fx avg `0.016` n `6`; index avg `0.0219` n `27`; metal avg `0.052` n `20`; unknown avg `1.0379` n `1263`
- 1h: commodity avg `0.0664` n `13`; crypto_alt avg `-0.124` n `239`; crypto_major avg `-0.3735` n `8`; equity avg `0.1466` n `158`; fx avg `0.0018` n `6`; index avg `0.0257` n `27`; metal avg `0.078` n `20`; unknown avg `19.7452` n `1257`
- 4h: commodity avg `-0.3925` n `13`; crypto_alt avg `1.1921` n `239`; crypto_major avg `0.3068` n `8`; equity avg `0.9216` n `158`; fx avg `-0.0258` n `6`; index avg `0.1223` n `27`; metal avg `0.1519` n `20`; unknown avg `1.2541` n `1251`
- 24h: commodity avg `-0.4494` n `13`; crypto_alt avg `0.1765` n `239`; crypto_major avg `-3.0822` n `8`; equity avg `0.4129` n `158`; fx avg `-0.1105` n `6`; index avg `0.0897` n `27`; metal avg `0.4166` n `20`; unknown avg `1.1806` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
