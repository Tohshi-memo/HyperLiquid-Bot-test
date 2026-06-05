# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T00:22:20.964269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.1625` n `228`; crypto_major avg `-0.1854` n `8`; equity avg `-0.3756` n `74`; fx avg `0.0592` n `6`; index avg `-0.1648` n `23`; metal avg `-0.2476` n `18`; unknown avg `0.0836` n `424`
- 1h: commodity avg `0.0989` n `12`; crypto_alt avg `0.4412` n `228`; crypto_major avg `0.4097` n `8`; equity avg `-0.7054` n `74`; fx avg `0.049` n `6`; index avg `-0.4684` n `23`; metal avg `-0.4774` n `18`; unknown avg `0.9677` n `424`
- 4h: commodity avg `0.0516` n `12`; crypto_alt avg `-1.3376` n `228`; crypto_major avg `-0.6415` n `8`; equity avg `-1.2227` n `74`; fx avg `0.0698` n `6`; index avg `-0.6901` n `23`; metal avg `-0.5862` n `18`; unknown avg `0.1272` n `424`
- 24h: commodity avg `-0.4701` n `12`; crypto_alt avg `-6.6755` n `228`; crypto_major avg `-4.1163` n `8`; equity avg `-1.2534` n `73`; fx avg `0.1747` n `6`; index avg `-0.3274` n `23`; metal avg `0.118` n `18`; unknown avg `-1.5479` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
