# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T01:07:26.463409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8652` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5142` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0868` n `13`; crypto_alt avg `0.2973` n `239`; crypto_major avg `0.2756` n `8`; equity avg `0.2657` n `158`; fx avg `0.0114` n `6`; index avg `0.0705` n `27`; metal avg `0.0279` n `20`; unknown avg `1.2252` n `1258`
- 1h: commodity avg `-0.0151` n `13`; crypto_alt avg `1.3417` n `239`; crypto_major avg `1.0315` n `8`; equity avg `0.7775` n `158`; fx avg `0.0179` n `6`; index avg `0.146` n `27`; metal avg `0.3121` n `20`; unknown avg `1.4991` n `1256`
- 4h: commodity avg `-0.0759` n `13`; crypto_alt avg `-0.5637` n `239`; crypto_major avg `-1.4617` n `8`; equity avg `-0.205` n `158`; fx avg `-0.0413` n `6`; index avg `0.0525` n `27`; metal avg `0.4035` n `20`; unknown avg `2.0243` n `1210`
- 24h: commodity avg `-0.1059` n `13`; crypto_alt avg `-1.9888` n `239`; crypto_major avg `-1.9154` n `8`; equity avg `-0.2256` n `158`; fx avg `-0.0092` n `6`; index avg `-0.0051` n `27`; metal avg `0.3723` n `20`; unknown avg `0.5019` n `1000`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
