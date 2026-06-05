# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T17:07:22.365911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `2.4123` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.2014` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.9371` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.6408` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1254` n `12`; crypto_alt avg `0.2806` n `228`; crypto_major avg `0.2596` n `8`; equity avg `-0.099` n `74`; fx avg `-0.004` n `6`; index avg `0.024` n `23`; metal avg `0.1909` n `18`; unknown avg `0.0848` n `424`
- 1h: commodity avg `-0.333` n `12`; crypto_alt avg `2.3316` n `228`; crypto_major avg `1.8684` n `8`; equity avg `-0.5439` n `74`; fx avg `-0.0009` n `6`; index avg `-0.454` n `23`; metal avg `0.2276` n `18`; unknown avg `1.5416` n `424`
- 4h: commodity avg `-1.0751` n `12`; crypto_alt avg `-0.9772` n `228`; crypto_major avg `-1.8009` n `8`; equity avg `-3.738` n `74`; fx avg `-0.1646` n `6`; index avg `-2.0404` n `23`; metal avg `-2.2034` n `18`; unknown avg `-0.7592` n `424`
- 24h: commodity avg `-1.4702` n `12`; crypto_alt avg `-7.5812` n `228`; crypto_major avg `-5.7611` n `8`; equity avg `-5.9536` n `74`; fx avg `-0.0484` n `6`; index avg `-3.08` n `23`; metal avg `-3.9301` n `18`; unknown avg `-1.772` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
