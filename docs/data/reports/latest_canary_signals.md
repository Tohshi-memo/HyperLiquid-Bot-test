# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T19:22:26.646680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `13`; crypto_alt avg `-0.0445` n `239`; crypto_major avg `-0.0217` n `8`; equity avg `0.1093` n `158`; fx avg `-0.0065` n `6`; index avg `0.0218` n `27`; metal avg `0.0112` n `20`; unknown avg `0.1134` n `1262`
- 1h: commodity avg `0.0142` n `13`; crypto_alt avg `-0.0387` n `239`; crypto_major avg `-0.1743` n `8`; equity avg `-0.0216` n `158`; fx avg `-0.0222` n `6`; index avg `0.0201` n `27`; metal avg `0.0213` n `20`; unknown avg `0.9847` n `1254`
- 4h: commodity avg `-0.1358` n `13`; crypto_alt avg `-0.2355` n `239`; crypto_major avg `-0.1826` n `8`; equity avg `0.4243` n `158`; fx avg `0.0095` n `6`; index avg `0.0595` n `27`; metal avg `0.0381` n `20`; unknown avg `1.2524` n `1194`
- 24h: commodity avg `-0.0705` n `13`; crypto_alt avg `-1.5528` n `239`; crypto_major avg `-0.3383` n `8`; equity avg `0.4654` n `158`; fx avg `0.0562` n `6`; index avg `0.0318` n `27`; metal avg `-0.0069` n `20`; unknown avg `0.0883` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
