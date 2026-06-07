# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T08:22:21.950244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1626` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0794` n `12`; crypto_alt avg `-0.0069` n `228`; crypto_major avg `0.0751` n `8`; equity avg `-0.0036` n `74`; fx avg `0.0` n `6`; index avg `0.1086` n `23`; metal avg `0.0257` n `18`; unknown avg `-1.7017` n `516`
- 1h: commodity avg `-0.1985` n `12`; crypto_alt avg `-0.0974` n `228`; crypto_major avg `0.2216` n `8`; equity avg `-0.0004` n `74`; fx avg `0.0166` n `6`; index avg `0.077` n `23`; metal avg `0.0306` n `18`; unknown avg `-1.7951` n `516`
- 4h: commodity avg `-0.4653` n `12`; crypto_alt avg `1.0308` n `228`; crypto_major avg `1.6973` n `8`; equity avg `0.5653` n `74`; fx avg `0.0048` n `6`; index avg `0.1466` n `23`; metal avg `0.221` n `18`; unknown avg `-1.8936` n `506`
- 24h: commodity avg `0.0456` n `12`; crypto_alt avg `2.1466` n `228`; crypto_major avg `1.8415` n `8`; equity avg `2.3706` n `74`; fx avg `0.0642` n `6`; index avg `1.1734` n `23`; metal avg `0.628` n `18`; unknown avg `0.2803` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
