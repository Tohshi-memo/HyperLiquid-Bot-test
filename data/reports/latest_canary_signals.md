# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T03:52:25.566270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0898` n `12`; crypto_alt avg `-0.0001` n `228`; crypto_major avg `-0.0095` n `8`; equity avg `0.0308` n `74`; fx avg `0.0006` n `6`; index avg `0.0126` n `23`; metal avg `-0.0189` n `18`; unknown avg `0.2593` n `516`
- 1h: commodity avg `0.0349` n `12`; crypto_alt avg `-0.0208` n `228`; crypto_major avg `0.2012` n `8`; equity avg `0.1544` n `74`; fx avg `0.0013` n `6`; index avg `0.3208` n `23`; metal avg `0.1183` n `18`; unknown avg `0.4099` n `516`
- 4h: commodity avg `-0.1184` n `12`; crypto_alt avg `1.5097` n `228`; crypto_major avg `1.5922` n `8`; equity avg `0.4626` n `74`; fx avg `-0.0012` n `6`; index avg `0.4282` n `23`; metal avg `0.4371` n `18`; unknown avg `2.2286` n `515`
- 24h: commodity avg `-0.1069` n `12`; crypto_alt avg `2.0867` n `228`; crypto_major avg `1.2251` n `8`; equity avg `1.4065` n `74`; fx avg `0.0563` n `6`; index avg `0.938` n `23`; metal avg `0.5046` n `18`; unknown avg `0.4983` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
