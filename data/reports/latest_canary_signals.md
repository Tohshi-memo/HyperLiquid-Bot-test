# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T23:42:01.769179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2731` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5578` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2932` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.2456` n `228`; crypto_major avg `0.3971` n `8`; equity avg `0.1167` n `74`; fx avg `0.0064` n `6`; index avg `0.1313` n `23`; metal avg `0.2082` n `18`; unknown avg `-0.0511` n `516`
- 1h: commodity avg `-0.1443` n `12`; crypto_alt avg `-0.6475` n `228`; crypto_major avg `-0.2528` n `8`; equity avg `-0.2113` n `74`; fx avg `-0.0006` n `6`; index avg `0.049` n `23`; metal avg `0.2523` n `18`; unknown avg `-0.0735` n `516`
- 4h: commodity avg `-0.4213` n `12`; crypto_alt avg `2.5541` n `228`; crypto_major avg `2.8518` n `8`; equity avg `0.5586` n `74`; fx avg `-0.0404` n `6`; index avg `0.1303` n `23`; metal avg `0.294` n `18`; unknown avg `1.0337` n `516`
- 24h: commodity avg `0.1018` n `12`; crypto_alt avg `3.2068` n `228`; crypto_major avg `5.0325` n `8`; equity avg `1.3405` n `74`; fx avg `-0.0497` n `6`; index avg `0.2632` n `23`; metal avg `0.6215` n `18`; unknown avg `-4.5878` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
