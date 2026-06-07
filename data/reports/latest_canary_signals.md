# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T22:52:24.794975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.7332` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.2465` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.8718` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.721` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0393` n `12`; crypto_alt avg `-0.3116` n `228`; crypto_major avg `-0.1977` n `8`; equity avg `-0.0345` n `74`; fx avg `-0.0062` n `6`; index avg `-0.04` n `23`; metal avg `0.0042` n `18`; unknown avg `0.1056` n `516`
- 1h: commodity avg `-0.4291` n `12`; crypto_alt avg `2.3962` n `228`; crypto_major avg `2.3041` n `8`; equity avg `0.4323` n `74`; fx avg `-0.014` n `6`; index avg `-0.1143` n `23`; metal avg `0.0576` n `18`; unknown avg `0.5275` n `516`
- 4h: commodity avg `-0.0292` n `12`; crypto_alt avg `1.2856` n `228`; crypto_major avg `1.5691` n `8`; equity avg `0.1666` n `74`; fx avg `-0.0293` n `6`; index avg `-0.0019` n `23`; metal avg `-0.1519` n `18`; unknown avg `0.7058` n `516`
- 24h: commodity avg `0.1609` n `12`; crypto_alt avg `3.7675` n `228`; crypto_major avg `5.2532` n `8`; equity avg `1.7562` n `74`; fx avg `-0.0627` n `6`; index avg `0.2138` n `23`; metal avg `0.3713` n `18`; unknown avg `-4.4267` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
