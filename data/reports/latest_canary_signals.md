# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T12:37:30.340649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1236` n `13`; crypto_alt avg `-0.1226` n `239`; crypto_major avg `-0.2278` n `8`; equity avg `-0.2128` n `160`; fx avg `-0.0018` n `6`; index avg `-0.0106` n `27`; metal avg `-0.0484` n `20`; unknown avg `4.8281` n `1262`
- 1h: commodity avg `-0.1899` n `13`; crypto_alt avg `0.101` n `239`; crypto_major avg `-0.1901` n `8`; equity avg `-0.205` n `160`; fx avg `0.0022` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0299` n `20`; unknown avg `1.6027` n `1248`
- 4h: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.3246` n `239`; crypto_major avg `-0.7814` n `8`; equity avg `-0.8677` n `160`; fx avg `-0.0015` n `6`; index avg `-0.0743` n `27`; metal avg `-0.2748` n `20`; unknown avg `21.979` n `1229`
- 24h: commodity avg `-0.5012` n `13`; crypto_alt avg `-0.277` n `239`; crypto_major avg `-0.9523` n `8`; equity avg `3.1422` n `160`; fx avg `-0.0235` n `6`; index avg `0.3874` n `27`; metal avg `-0.143` n `20`; unknown avg `7.8176` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2356`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
