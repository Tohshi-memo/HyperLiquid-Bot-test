# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T23:37:29.801034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1057` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1035` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9366` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0817` n `13`; crypto_alt avg `-0.6077` n `239`; crypto_major avg `-0.7262` n `8`; equity avg `-0.2965` n `158`; fx avg `-0.0075` n `6`; index avg `-0.0702` n `27`; metal avg `-0.0362` n `20`; unknown avg `-0.248` n `1262`
- 1h: commodity avg `-0.1663` n `13`; crypto_alt avg `1.1036` n `239`; crypto_major avg `1.102` n `8`; equity avg `0.4313` n `158`; fx avg `-0.0091` n `6`; index avg `0.0583` n `27`; metal avg `0.1653` n `20`; unknown avg `2.0428` n `1238`
- 4h: commodity avg `0.0433` n `13`; crypto_alt avg `-1.6536` n `239`; crypto_major avg `-2.0624` n `8`; equity avg `-1.0432` n `158`; fx avg `-0.0343` n `6`; index avg `-0.1258` n `27`; metal avg `0.0411` n `20`; unknown avg `3.5642` n `1178`
- 24h: commodity avg `-0.0693` n `13`; crypto_alt avg `-2.9275` n `239`; crypto_major avg `-2.2112` n `8`; equity avg `-0.4684` n `158`; fx avg `0.0315` n `6`; index avg `-0.0974` n `27`; metal avg `0.0307` n `20`; unknown avg `0.1901` n `1002`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
