# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T23:07:21.763889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.2671` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.25` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.9348` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2499` n `12`; crypto_alt avg `-0.0709` n `228`; crypto_major avg `0.0314` n `8`; equity avg `0.0342` n `74`; fx avg `0.0011` n `6`; index avg `-0.0327` n `23`; metal avg `-0.0143` n `18`; unknown avg `-0.3449` n `425`
- 1h: commodity avg `0.6408` n `12`; crypto_alt avg `0.3212` n `228`; crypto_major avg `0.4984` n `8`; equity avg `-0.334` n `74`; fx avg `-0.0077` n `6`; index avg `-0.1743` n `23`; metal avg `-0.0667` n `18`; unknown avg `0.1722` n `425`
- 4h: commodity avg `0.2976` n `12`; crypto_alt avg `3.9892` n `228`; crypto_major avg `3.2324` n `8`; equity avg `-0.0176` n `74`; fx avg `0.0062` n `6`; index avg `-0.1606` n `23`; metal avg `-0.0347` n `18`; unknown avg `4.1613` n `425`
- 24h: commodity avg `-1.2861` n `12`; crypto_alt avg `-6.0687` n `228`; crypto_major avg `-5.4439` n `8`; equity avg `-5.9801` n `74`; fx avg `-0.0486` n `6`; index avg `-4.2124` n `23`; metal avg `-4.4536` n `18`; unknown avg `-1.3697` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
