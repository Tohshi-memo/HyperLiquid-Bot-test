# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T09:22:26.734717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.5414` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.2692` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.2101` n `231`; crypto_major avg `0.3595` n `8`; equity avg `0.0221` n `127`; fx avg `0.0035` n `6`; index avg `-0.0057` n `26`; metal avg `0.0269` n `20`; unknown avg `-0.0641` n `792`
- 1h: commodity avg `0.1044` n `12`; crypto_alt avg `0.6922` n `231`; crypto_major avg `0.9316` n `8`; equity avg `0.0483` n `127`; fx avg `0.0091` n `6`; index avg `-0.0121` n `26`; metal avg `-0.0517` n `20`; unknown avg `-0.0825` n `792`
- 4h: commodity avg `0.0274` n `12`; crypto_alt avg `2.1903` n `231`; crypto_major avg `2.2966` n `8`; equity avg `0.8282` n `127`; fx avg `-0.012` n `6`; index avg `0.0761` n `26`; metal avg `-0.2448` n `20`; unknown avg `0.2447` n `775`
- 24h: commodity avg `0.5394` n `12`; crypto_alt avg `2.5698` n `231`; crypto_major avg `3.1393` n `8`; equity avg `2.1163` n `127`; fx avg `-0.0875` n `6`; index avg `0.2995` n `26`; metal avg `-0.3426` n `20`; unknown avg `0.5593` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
