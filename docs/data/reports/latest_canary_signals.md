# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T10:07:26.050983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0633` n `13`; crypto_alt avg `-0.275` n `239`; crypto_major avg `-0.3007` n `8`; equity avg `0.0726` n `158`; fx avg `0.006` n `6`; index avg `0.0067` n `27`; metal avg `0.0125` n `20`; unknown avg `0.6356` n `1259`
- 1h: commodity avg `0.2315` n `13`; crypto_alt avg `-0.0321` n `239`; crypto_major avg `-0.7604` n `8`; equity avg `0.2532` n `158`; fx avg `-0.0145` n `6`; index avg `0.0052` n `27`; metal avg `-0.0133` n `20`; unknown avg `0.7015` n `1257`
- 4h: commodity avg `0.073` n `13`; crypto_alt avg `0.1948` n `239`; crypto_major avg `-0.7749` n `8`; equity avg `-0.057` n `158`; fx avg `0.044` n `6`; index avg `-0.0099` n `27`; metal avg `-0.15` n `20`; unknown avg `171.6401` n `1127`
- 24h: commodity avg `0.0166` n `13`; crypto_alt avg `-1.8368` n `239`; crypto_major avg `-3.5563` n `8`; equity avg `-0.4139` n `158`; fx avg `-0.0894` n `6`; index avg `-0.0324` n `27`; metal avg `0.2743` n `20`; unknown avg `0.9902` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
