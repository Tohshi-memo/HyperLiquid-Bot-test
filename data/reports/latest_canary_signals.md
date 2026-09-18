# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T14:22:34.565865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.7895` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.4291` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.4042` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.3771` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.1019` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `0.4464` n `234`; crypto_major avg `0.6073` n `8`; equity avg `0.2644` n `140`; fx avg `0.0176` n `6`; index avg `0.0198` n `26`; metal avg `0.0207` n `20`; unknown avg `7.8368` n `928`
- 1h: commodity avg `0.1349` n `12`; crypto_alt avg `0.8953` n `234`; crypto_major avg `2.2368` n `8`; equity avg `-0.1674` n `140`; fx avg `0.0282` n `6`; index avg `-0.0663` n `26`; metal avg `-0.1403` n `20`; unknown avg `10.9732` n `904`
- 4h: commodity avg `0.4119` n `12`; crypto_alt avg `0.6871` n `234`; crypto_major avg `2.1903` n `8`; equity avg `-0.5992` n `140`; fx avg `-0.0134` n `6`; index avg `-0.1367` n `26`; metal avg `-0.2388` n `20`; unknown avg `13.6665` n `895`
- 24h: commodity avg `0.2417` n `12`; crypto_alt avg `5.6307` n `234`; crypto_major avg `5.6442` n `8`; equity avg `0.6216` n `140`; fx avg `0.2579` n `6`; index avg `-0.0826` n `26`; metal avg `-0.0134` n `20`; unknown avg `8.6008` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
