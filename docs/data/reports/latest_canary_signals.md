# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T16:07:22.643219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0399` n `12`; crypto_alt avg `-0.0119` n `228`; crypto_major avg `-0.0549` n `8`; equity avg `-0.0487` n `74`; fx avg `0.0259` n `6`; index avg `-0.0813` n `23`; metal avg `-0.0139` n `18`; unknown avg `-2.6889` n `516`
- 1h: commodity avg `0.1315` n `12`; crypto_alt avg `-0.0633` n `228`; crypto_major avg `0.2279` n `8`; equity avg `-0.017` n `74`; fx avg `-0.0046` n `6`; index avg `0.0216` n `23`; metal avg `0.0183` n `18`; unknown avg `-2.6745` n `516`
- 4h: commodity avg `0.3771` n `12`; crypto_alt avg `-0.3363` n `228`; crypto_major avg `-0.3354` n `8`; equity avg `0.1664` n `74`; fx avg `-0.0002` n `6`; index avg `0.03` n `23`; metal avg `-0.1295` n `18`; unknown avg `-2.5033` n `516`
- 24h: commodity avg `0.3545` n `12`; crypto_alt avg `2.2756` n `228`; crypto_major avg `2.4704` n `8`; equity avg `1.8116` n `74`; fx avg `-0.0005` n `6`; index avg `0.3018` n `23`; metal avg `0.5759` n `18`; unknown avg `-5.0526` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
