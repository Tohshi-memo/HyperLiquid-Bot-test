# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T08:07:25.401050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7658` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.1331` n `228`; crypto_major avg `-0.1948` n `8`; equity avg `-0.1019` n `74`; fx avg `-0.0025` n `6`; index avg `-0.048` n `23`; metal avg `-0.0225` n `18`; unknown avg `0.2264` n `425`
- 1h: commodity avg `-0.0336` n `12`; crypto_alt avg `0.6335` n `228`; crypto_major avg `0.4694` n `8`; equity avg `-0.3609` n `74`; fx avg `0.0048` n `6`; index avg `-0.1036` n `23`; metal avg `-0.0286` n `18`; unknown avg `0.2874` n `425`
- 4h: commodity avg `-0.3602` n `12`; crypto_alt avg `1.236` n `228`; crypto_major avg `1.3005` n `8`; equity avg `-0.4653` n `74`; fx avg `-0.0202` n `6`; index avg `-0.3664` n `23`; metal avg `0.1121` n `18`; unknown avg `0.5959` n `415`
- 24h: commodity avg `-1.3701` n `12`; crypto_alt avg `-3.7778` n `228`; crypto_major avg `-3.3741` n `8`; equity avg `-6.7841` n `74`; fx avg `-0.2468` n `6`; index avg `-4.2068` n `23`; metal avg `-4.1107` n `18`; unknown avg `0.4308` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
