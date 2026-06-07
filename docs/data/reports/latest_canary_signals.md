# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T01:52:22.671290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.0708` n `228`; crypto_major avg `-0.1281` n `8`; equity avg `0.0106` n `74`; fx avg `0.0021` n `6`; index avg `0.0196` n `23`; metal avg `0.0553` n `18`; unknown avg `0.046` n `516`
- 1h: commodity avg `-0.0188` n `12`; crypto_alt avg `1.6557` n `228`; crypto_major avg `1.3197` n `8`; equity avg `0.4176` n `74`; fx avg `0.004` n `6`; index avg `0.1464` n `23`; metal avg `0.2194` n `18`; unknown avg `0.9888` n `516`
- 4h: commodity avg `0.0583` n `12`; crypto_alt avg `2.3107` n `228`; crypto_major avg `1.5155` n `8`; equity avg `0.6597` n `74`; fx avg `-0.0184` n `6`; index avg `0.0478` n `23`; metal avg `0.2886` n `18`; unknown avg `0.5762` n `515`
- 24h: commodity avg `0.177` n `12`; crypto_alt avg `0.9343` n `228`; crypto_major avg `-0.0059` n `8`; equity avg `0.9316` n `74`; fx avg `0.0359` n `6`; index avg `0.4686` n `23`; metal avg `-0.0402` n `18`; unknown avg `1.0556` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
