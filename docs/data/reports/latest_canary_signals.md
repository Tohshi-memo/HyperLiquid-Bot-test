# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T14:07:31.064231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4886` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.3512` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.2701` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.6328` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `2.1162` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.0876` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `0.4331` n `233`; crypto_major avg `0.4443` n `8`; equity avg `-0.0282` n `136`; fx avg `0.0093` n `6`; index avg `-0.0125` n `26`; metal avg `0.0088` n `20`; unknown avg `7.7699` n `778`
- 1h: commodity avg `0.1161` n `12`; crypto_alt avg `1.6021` n `233`; crypto_major avg `2.2037` n `8`; equity avg `-0.4291` n `136`; fx avg `0.0317` n `6`; index avg `-0.0876` n `26`; metal avg `0.0875` n `20`; unknown avg `7.7623` n `778`
- 4h: commodity avg `0.0377` n `12`; crypto_alt avg `2.5549` n `233`; crypto_major avg `3.5263` n `8`; equity avg `0.1751` n `136`; fx avg `-0.0761` n `6`; index avg `0.0263` n `26`; metal avg `0.2562` n `20`; unknown avg `5.2083` n `772`
- 24h: commodity avg `-0.0292` n `12`; crypto_alt avg `2.0284` n `233`; crypto_major avg `3.5083` n `8`; equity avg `0.459` n `136`; fx avg `-0.1212` n `6`; index avg `0.2558` n `26`; metal avg `0.1927` n `20`; unknown avg `5.7972` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
