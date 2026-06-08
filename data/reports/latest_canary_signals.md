# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T06:37:28.606397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1033` n `12`; crypto_alt avg `0.1177` n `228`; crypto_major avg `-0.0862` n `8`; equity avg `0.0753` n `74`; fx avg `-0.0268` n `6`; index avg `-0.0465` n `23`; metal avg `-0.282` n `18`; unknown avg `-0.1347` n `517`
- 1h: commodity avg `-0.1541` n `12`; crypto_alt avg `0.9927` n `228`; crypto_major avg `0.9213` n `8`; equity avg `0.0552` n `74`; fx avg `-0.081` n `6`; index avg `0.0521` n `23`; metal avg `0.6117` n `18`; unknown avg `0.0947` n `507`
- 4h: commodity avg `0.3159` n `12`; crypto_alt avg `0.0568` n `228`; crypto_major avg `-0.261` n `8`; equity avg `-0.8999` n `74`; fx avg `-0.2368` n `6`; index avg `-0.3949` n `23`; metal avg `-0.4286` n `18`; unknown avg `-0.1189` n `507`
- 24h: commodity avg `0.8125` n `12`; crypto_alt avg `0.056` n `228`; crypto_major avg `1.7537` n `8`; equity avg `0.0755` n `74`; fx avg `-0.2817` n `6`; index avg `-0.1483` n `23`; metal avg `-0.8893` n `18`; unknown avg `-5.6285` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
