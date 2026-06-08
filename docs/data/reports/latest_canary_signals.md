# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T01:37:25.028539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1221` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5957` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.2221` n `228`; crypto_major avg `-0.1926` n `8`; equity avg `-0.3388` n `74`; fx avg `-0.0323` n `6`; index avg `-0.0712` n `23`; metal avg `-0.0452` n `18`; unknown avg `-0.0001` n `517`
- 1h: commodity avg `0.3467` n `12`; crypto_alt avg `-1.3261` n `228`; crypto_major avg `-1.3723` n `8`; equity avg `-1.2973` n `74`; fx avg `-0.051` n `6`; index avg `-0.595` n `23`; metal avg `-0.87` n `18`; unknown avg `0.1797` n `517`
- 4h: commodity avg `-0.0732` n `12`; crypto_alt avg `1.4323` n `228`; crypto_major avg `1.8976` n `8`; equity avg `0.3019` n `74`; fx avg `-0.0781` n `6`; index avg `-0.0114` n `23`; metal avg `-0.2245` n `18`; unknown avg `0.2405` n `516`
- 24h: commodity avg `0.3624` n `12`; crypto_alt avg `0.3613` n `228`; crypto_major avg `2.9352` n `8`; equity avg `0.9062` n `74`; fx avg `-0.1146` n `6`; index avg `0.2247` n `23`; metal avg `-0.1397` n `18`; unknown avg `-5.2637` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
