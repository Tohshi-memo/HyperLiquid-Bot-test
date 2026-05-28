# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T05:52:26.536933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0965` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.1779` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.0241` n `228`; crypto_major avg `0.0082` n `8`; equity avg `0.1944` n `67`; fx avg `-0.0079` n `6`; index avg `0.0418` n `23`; metal avg `0.2696` n `18`; unknown avg `-0.2241` n `419`
- 1h: commodity avg `-0.1941` n `12`; crypto_alt avg `-0.4898` n `228`; crypto_major avg `-0.1922` n `8`; equity avg `0.8293` n `67`; fx avg `0.0135` n `6`; index avg `0.3192` n `23`; metal avg `0.8067` n `18`; unknown avg `-0.6575` n `419`
- 4h: commodity avg `0.4696` n `12`; crypto_alt avg `-2.7178` n `228`; crypto_major avg `-1.6269` n `8`; equity avg `-0.8395` n `67`; fx avg `-0.1013` n `6`; index avg `-0.449` n `23`; metal avg `-0.3021` n `18`; unknown avg `-0.8455` n `419`
- 24h: commodity avg `0.2522` n `12`; crypto_alt avg `-4.977` n `228`; crypto_major avg `-3.6136` n `8`; equity avg `-1.2357` n `67`; fx avg `-0.1287` n `6`; index avg `-1.0337` n `23`; metal avg `-1.8351` n `18`; unknown avg `-1.8752` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
