# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T09:22:30.406956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.167` n `228`; crypto_major avg `0.2123` n `8`; equity avg `0.0433` n `88`; fx avg `-0.0062` n `6`; index avg `-0.0025` n `23`; metal avg `-0.0123` n `20`; unknown avg `0.0361` n `764`
- 1h: commodity avg `0.015` n `12`; crypto_alt avg `0.09` n `228`; crypto_major avg `0.1233` n `8`; equity avg `-0.1108` n `88`; fx avg `-0.0215` n `6`; index avg `-0.0145` n `23`; metal avg `-0.1206` n `20`; unknown avg `-0.0054` n `764`
- 4h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.6815` n `228`; crypto_major avg `0.7662` n `8`; equity avg `0.6998` n `88`; fx avg `-0.0027` n `6`; index avg `0.1508` n `23`; metal avg `0.0186` n `20`; unknown avg `1.1919` n `732`
- 24h: commodity avg `-0.3984` n `12`; crypto_alt avg `-0.0901` n `228`; crypto_major avg `-0.3204` n `8`; equity avg `0.3325` n `88`; fx avg `0.0288` n `6`; index avg `0.0642` n `23`; metal avg `-0.3064` n `20`; unknown avg `-0.2195` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
