# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T16:37:29.895713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.8766` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.8532` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.8203` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.117` n `12`; crypto_alt avg `0.1077` n `234`; crypto_major avg `0.1533` n `8`; equity avg `-0.0449` n `140`; fx avg `-0.0099` n `6`; index avg `-0.0052` n `26`; metal avg `0.0457` n `20`; unknown avg `0.5773` n `922`
- 1h: commodity avg `-0.2081` n `12`; crypto_alt avg `0.5139` n `234`; crypto_major avg `0.4698` n `8`; equity avg `-0.0684` n `140`; fx avg `-0.0081` n `6`; index avg `-0.0272` n `26`; metal avg `0.1287` n `20`; unknown avg `4.7667` n `908`
- 4h: commodity avg `-0.0129` n `12`; crypto_alt avg `1.7067` n `234`; crypto_major avg `2.8403` n `8`; equity avg `0.02` n `140`; fx avg `-0.0421` n `6`; index avg `-0.101` n `26`; metal avg `-0.0363` n `20`; unknown avg `5.0976` n `884`
- 24h: commodity avg `-0.0906` n `12`; crypto_alt avg `6.3425` n `234`; crypto_major avg `6.7688` n `8`; equity avg `0.4609` n `140`; fx avg `0.1971` n `6`; index avg `-0.1465` n `26`; metal avg `0.2349` n `20`; unknown avg `3.8246` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
