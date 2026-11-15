# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T04:52:23.872867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2596` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.2554` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.7395` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0153` n `13`; crypto_alt avg `0.2218` n `239`; crypto_major avg `0.1931` n `8`; equity avg `0.0204` n `162`; fx avg `-0.005` n `6`; index avg `-0.0047` n `27`; metal avg `0.0341` n `20`; unknown avg `58.3848` n `1261`
- 1h: commodity avg `0.0357` n `13`; crypto_alt avg `0.2146` n `239`; crypto_major avg `0.2244` n `8`; equity avg `-0.0334` n `162`; fx avg `-0.0018` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0059` n `20`; unknown avg `0.388` n `1247`
- 4h: commodity avg `0.0483` n `13`; crypto_alt avg `2.5616` n `239`; crypto_major avg `3.3079` n `8`; equity avg `0.5684` n `162`; fx avg `0.0153` n `6`; index avg `0.0268` n `27`; metal avg `0.0525` n `20`; unknown avg `35.9506` n `1240`
- 24h: commodity avg `0.0663` n `13`; crypto_alt avg `-5.0606` n `239`; crypto_major avg `-3.5024` n `8`; equity avg `-0.6544` n `162`; fx avg `0.0415` n `6`; index avg `-0.0676` n `27`; metal avg `-0.4241` n `20`; unknown avg `47.0749` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
