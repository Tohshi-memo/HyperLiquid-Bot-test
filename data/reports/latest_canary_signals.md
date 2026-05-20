# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T14:07:22.041119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1079` n `12`; crypto_alt avg `0.0244` n `228`; crypto_major avg `-0.0124` n `8`; equity avg `-0.0341` n `66`; fx avg `0.0012` n `6`; index avg `-0.009` n `23`; metal avg `-0.0088` n `18`; unknown avg `0.4496` n `384`
- 1h: commodity avg `0.3151` n `12`; crypto_alt avg `-0.3644` n `228`; crypto_major avg `0.0007` n `8`; equity avg `-0.3649` n `66`; fx avg `0.0003` n `6`; index avg `0.1471` n `23`; metal avg `-0.2261` n `18`; unknown avg `0.3244` n `384`
- 4h: commodity avg `-0.1004` n `12`; crypto_alt avg `-0.1019` n `228`; crypto_major avg `0.2535` n `8`; equity avg `-0.272` n `66`; fx avg `0.0405` n `6`; index avg `0.2577` n `23`; metal avg `-0.4258` n `18`; unknown avg `2.2133` n `384`
- 24h: commodity avg `-0.4974` n `12`; crypto_alt avg `0.882` n `228`; crypto_major avg `0.9542` n `8`; equity avg `2.0889` n `66`; fx avg `-0.0535` n `6`; index avg `1.1762` n `23`; metal avg `0.035` n `18`; unknown avg `1.6523` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
