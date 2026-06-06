# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T00:07:23.477186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.615` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6088` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.2632` n `12`; crypto_alt avg `0.7659` n `228`; crypto_major avg `0.848` n `8`; equity avg `0.2945` n `74`; fx avg `-0.0012` n `6`; index avg `0.2289` n `23`; metal avg `0.0223` n `18`; unknown avg `0.5342` n `425`
- 1h: commodity avg `0.0628` n `12`; crypto_alt avg `-0.21` n `228`; crypto_major avg `-0.1674` n `8`; equity avg `-0.1736` n `74`; fx avg `-0.0012` n `6`; index avg `0.1903` n `23`; metal avg `-0.1497` n `18`; unknown avg `0.1633` n `425`
- 4h: commodity avg `0.4328` n `12`; crypto_alt avg `1.8323` n `228`; crypto_major avg `1.7611` n `8`; equity avg `0.1461` n `74`; fx avg `0.01` n `6`; index avg `0.2951` n `23`; metal avg `0.1523` n `18`; unknown avg `1.2206` n `425`
- 24h: commodity avg `-1.2589` n `12`; crypto_alt avg `-6.1245` n `228`; crypto_major avg `-5.3151` n `8`; equity avg `-5.6523` n `74`; fx avg `-0.0468` n `6`; index avg `-3.6737` n `23`; metal avg `-4.3707` n `18`; unknown avg `-1.4982` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
