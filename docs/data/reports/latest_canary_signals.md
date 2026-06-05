# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T20:22:22.357830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `2.4662` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.2754` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `2.0634` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `1.0515` n `228`; crypto_major avg `1.1215` n `8`; equity avg `0.0287` n `74`; fx avg `-0.0051` n `6`; index avg `-0.1118` n `23`; metal avg `0.0296` n `18`; unknown avg `1.3767` n `425`
- 1h: commodity avg `-0.0258` n `12`; crypto_alt avg `2.7008` n `228`; crypto_major avg `2.2496` n `8`; equity avg `0.1862` n `74`; fx avg `-0.0001` n `6`; index avg `-0.1382` n `23`; metal avg `-0.2166` n `18`; unknown avg `2.6626` n `425`
- 4h: commodity avg `-0.079` n `12`; crypto_alt avg `-0.564` n `228`; crypto_major avg `-1.0758` n `8`; equity avg `-1.758` n `74`; fx avg `-0.051` n `6`; index avg `-1.8918` n `23`; metal avg `-0.8306` n `18`; unknown avg `-0.5241` n `424`
- 24h: commodity avg `-1.6075` n `12`; crypto_alt avg `-7.8657` n `228`; crypto_major avg `-6.3301` n `8`; equity avg `-6.5405` n `74`; fx avg `-0.0511` n `6`; index avg `-4.5471` n `23`; metal avg `-4.8112` n `18`; unknown avg `-1.0551` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
