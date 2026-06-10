# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T15:37:32.199503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5595` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8912` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.8168` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0644` n `12`; crypto_alt avg `0.1005` n `228`; crypto_major avg `0.2515` n `8`; equity avg `-0.0437` n `74`; fx avg `-0.0035` n `6`; index avg `-0.0958` n `23`; metal avg `0.0207` n `18`; unknown avg `-0.0247` n `548`
- 1h: commodity avg `-0.3151` n `12`; crypto_alt avg `0.5408` n `228`; crypto_major avg `0.6223` n `8`; equity avg `-1.1945` n `74`; fx avg `-0.0063` n `6`; index avg `-0.9981` n `23`; metal avg `-0.3894` n `18`; unknown avg `0.1535` n `548`
- 4h: commodity avg `-0.3262` n `12`; crypto_alt avg `2.3974` n `228`; crypto_major avg `2.2333` n `8`; equity avg `1.4211` n `74`; fx avg `-0.0129` n `6`; index avg `0.2692` n `23`; metal avg `0.3421` n `18`; unknown avg `1.5894` n `547`
- 24h: commodity avg `1.0114` n `12`; crypto_alt avg `1.5641` n `228`; crypto_major avg `0.4271` n `8`; equity avg `0.2408` n `74`; fx avg `-0.0684` n `6`; index avg `-0.2608` n `23`; metal avg `-1.2686` n `18`; unknown avg `-0.1454` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
