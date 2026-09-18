# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T16:52:40.278761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.5174` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.4954` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.4271` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.4123` n `234`; crypto_major avg `-0.3796` n `8`; equity avg `0.1277` n `140`; fx avg `0.0009` n `6`; index avg `0.0196` n `26`; metal avg `-0.0019` n `20`; unknown avg `7.1297` n `926`
- 1h: commodity avg `-0.2139` n `12`; crypto_alt avg `-0.0369` n `234`; crypto_major avg `0.1841` n `8`; equity avg `0.022` n `140`; fx avg `-0.0147` n `6`; index avg `0.0041` n `26`; metal avg `0.1112` n `20`; unknown avg `11.0258` n `908`
- 4h: commodity avg `0.0415` n `12`; crypto_alt avg `1.2118` n `234`; crypto_major avg `2.5369` n `8`; equity avg `0.1098` n `140`; fx avg `-0.0493` n `6`; index avg `-0.0862` n `26`; metal avg `0.0195` n `20`; unknown avg `12.9416` n `884`
- 24h: commodity avg `-0.1675` n `12`; crypto_alt avg `5.7281` n `234`; crypto_major avg `6.2227` n `8`; equity avg `0.4449` n `140`; fx avg `0.1944` n `6`; index avg `-0.1515` n `26`; metal avg `0.2407` n `20`; unknown avg `7.6265` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
