# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T17:37:23.824443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.3024` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1871` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1035` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.7191` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0185` n `13`; crypto_alt avg `-0.2162` n `239`; crypto_major avg `-0.3132` n `8`; equity avg `-0.1582` n `168`; fx avg `-0.004` n `6`; index avg `-0.0031` n `27`; metal avg `0.005` n `20`; unknown avg `1.6209` n `1264`
- 1h: commodity avg `0.0506` n `13`; crypto_alt avg `-0.3693` n `239`; crypto_major avg `-0.8182` n `8`; equity avg `-0.2168` n `168`; fx avg `-0.0028` n `6`; index avg `0.0096` n `27`; metal avg `0.0432` n `20`; unknown avg `2.3341` n `1248`
- 4h: commodity avg `-0.2103` n `13`; crypto_alt avg `-1.8394` n `239`; crypto_major avg `-2.3138` n `8`; equity avg `-0.5947` n `168`; fx avg `-0.0523` n `6`; index avg `-0.0114` n `27`; metal avg `-0.1267` n `20`; unknown avg `2.334` n `1244`
- 24h: commodity avg `-0.508` n `13`; crypto_alt avg `0.1845` n `239`; crypto_major avg `0.6425` n `8`; equity avg `2.9605` n `168`; fx avg `-0.1443` n `6`; index avg `0.291` n `27`; metal avg `0.7708` n `20`; unknown avg `259.9737` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
