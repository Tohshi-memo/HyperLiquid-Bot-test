# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T03:22:20.628542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1054` n `12`; crypto_alt avg `-0.1022` n `228`; crypto_major avg `-0.1611` n `8`; equity avg `0.0436` n `74`; fx avg `-0.0152` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0268` n `18`; unknown avg `0.0579` n `425`
- 1h: commodity avg `0.0558` n `12`; crypto_alt avg `-0.689` n `228`; crypto_major avg `-0.3592` n `8`; equity avg `-0.2066` n `74`; fx avg `-0.0208` n `6`; index avg `-0.0674` n `23`; metal avg `-0.2133` n `18`; unknown avg `0.6642` n `425`
- 4h: commodity avg `0.1601` n `12`; crypto_alt avg `-1.1911` n `228`; crypto_major avg `-0.7275` n `8`; equity avg `-1.5641` n `74`; fx avg `-0.0465` n `6`; index avg `-0.5931` n `23`; metal avg `-0.4586` n `18`; unknown avg `1.0345` n `425`
- 24h: commodity avg `-1.1124` n `12`; crypto_alt avg `-5.5947` n `228`; crypto_major avg `-4.8774` n `8`; equity avg `-6.8351` n `74`; fx avg `-0.2204` n `6`; index avg `-4.1103` n `23`; metal avg `-3.9437` n `18`; unknown avg `0.0252` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
