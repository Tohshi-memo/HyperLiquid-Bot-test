# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T12:37:30.051242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.0544` n `230`; crypto_major avg `-0.052` n `8`; equity avg `-0.0237` n `100`; fx avg `-0.0093` n `6`; index avg `-0.0183` n `25`; metal avg `-0.0263` n `20`; unknown avg `0.0459` n `773`
- 1h: commodity avg `0.0994` n `12`; crypto_alt avg `0.0711` n `230`; crypto_major avg `0.044` n `8`; equity avg `0.1621` n `100`; fx avg `-0.0203` n `6`; index avg `0.0257` n `25`; metal avg `0.02` n `20`; unknown avg `0.0284` n `773`
- 4h: commodity avg `0.0734` n `12`; crypto_alt avg `-0.5861` n `230`; crypto_major avg `-0.6419` n `8`; equity avg `0.1305` n `100`; fx avg `-0.0481` n `6`; index avg `0.0387` n `25`; metal avg `0.0977` n `20`; unknown avg `0.0219` n `772`
- 24h: commodity avg `-0.3195` n `12`; crypto_alt avg `-1.0093` n `230`; crypto_major avg `-1.2521` n `8`; equity avg `-0.4341` n `100`; fx avg `-0.1826` n `6`; index avg `-0.1803` n `25`; metal avg `-0.0751` n `20`; unknown avg `0.2203` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0979`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0841`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
