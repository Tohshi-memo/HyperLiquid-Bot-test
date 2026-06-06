# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T06:07:25.011767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.7669` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.5262` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.9057` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `0.4241` n `228`; crypto_major avg `0.2471` n `8`; equity avg `0.1003` n `74`; fx avg `0.0024` n `6`; index avg `0.0939` n `23`; metal avg `0.0463` n `18`; unknown avg `0.0993` n `415`
- 1h: commodity avg `0.059` n `12`; crypto_alt avg `3.2634` n `228`; crypto_major avg `2.8259` n `8`; equity avg `0.9202` n `74`; fx avg `-0.003` n `6`; index avg `0.3876` n `23`; metal avg `0.2997` n `18`; unknown avg `0.2497` n `415`
- 4h: commodity avg `-0.2316` n `12`; crypto_alt avg `-1.2896` n `228`; crypto_major avg `-0.3764` n `8`; equity avg `-0.2323` n `74`; fx avg `-0.0024` n `6`; index avg `-0.2047` n `23`; metal avg `-0.3627` n `18`; unknown avg `-0.4331` n `415`
- 24h: commodity avg `-1.412` n `12`; crypto_alt avg `-5.1137` n `228`; crypto_major avg `-3.4987` n `8`; equity avg `-6.477` n `74`; fx avg `-0.1812` n `6`; index avg `-4.1268` n `23`; metal avg `-3.9476` n `18`; unknown avg `-0.7256` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
