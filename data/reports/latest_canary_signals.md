# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T15:52:26.209399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.2822` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.116` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5441` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.1158` n `228`; crypto_major avg `-0.1738` n `8`; equity avg `-0.0026` n `86`; fx avg `0.0099` n `6`; index avg `0.0161` n `23`; metal avg `0.0628` n `20`; unknown avg `-0.3035` n `765`
- 1h: commodity avg `0.3325` n `12`; crypto_alt avg `-0.5979` n `228`; crypto_major avg `-0.5759` n `8`; equity avg `-0.3801` n `86`; fx avg `0.0511` n `6`; index avg `-0.0495` n `23`; metal avg `0.1996` n `20`; unknown avg `-0.5063` n `765`
- 4h: commodity avg `0.3349` n `12`; crypto_alt avg `-2.2473` n `228`; crypto_major avg `-2.7811` n `8`; equity avg `-2.4461` n `86`; fx avg `0.0832` n `6`; index avg `-0.237` n `23`; metal avg `0.5011` n `20`; unknown avg `0.9462` n `765`
- 24h: commodity avg `0.3497` n `12`; crypto_alt avg `-1.7572` n `228`; crypto_major avg `-1.7221` n `8`; equity avg `-1.1009` n `86`; fx avg `0.0761` n `6`; index avg `0.2679` n `23`; metal avg `0.2016` n `20`; unknown avg `0.3151` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
