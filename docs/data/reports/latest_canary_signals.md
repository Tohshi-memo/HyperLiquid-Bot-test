# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T16:07:27.575350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.1555` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.9371` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.7659` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0804` n `12`; crypto_alt avg `0.2476` n `234`; crypto_major avg `0.3633` n `8`; equity avg `0.004` n `140`; fx avg `-0.025` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0358` n `914`
- 1h: commodity avg `-0.0405` n `12`; crypto_alt avg `0.518` n `234`; crypto_major avg `0.201` n `8`; equity avg `0.0841` n `140`; fx avg `-0.0249` n `6`; index avg `-0.0324` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.0` n `914`
- 4h: commodity avg `0.2158` n `12`; crypto_alt avg `1.8474` n `234`; crypto_major avg `2.9817` n `8`; equity avg `0.0446` n `140`; fx avg `-0.0594` n `6`; index avg `-0.1173` n `26`; metal avg `-0.1738` n `20`; unknown avg `1.3158` n `884`
- 24h: commodity avg `0.1633` n `12`; crypto_alt avg `6.1426` n `234`; crypto_major avg `6.2632` n `8`; equity avg `0.6369` n `140`; fx avg `0.2093` n `6`; index avg `-0.1326` n `26`; metal avg `0.083` n `20`; unknown avg `2.231` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
