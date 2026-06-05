# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T18:22:32.838089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.062` n `12`; crypto_alt avg `-1.0741` n `228`; crypto_major avg `-0.9302` n `8`; equity avg `-0.534` n `74`; fx avg `0.0106` n `6`; index avg `-0.246` n `23`; metal avg `-0.2146` n `18`; unknown avg `-0.2968` n `424`
- 1h: commodity avg `0.1826` n `12`; crypto_alt avg `-0.841` n `228`; crypto_major avg `-0.8359` n `8`; equity avg `-0.8585` n `74`; fx avg `-0.023` n `6`; index avg `-0.3507` n `23`; metal avg `-0.4712` n `18`; unknown avg `-0.4093` n `424`
- 4h: commodity avg `-0.7537` n `12`; crypto_alt avg `-1.7956` n `228`; crypto_major avg `-1.9475` n `8`; equity avg `-3.0474` n `74`; fx avg `-0.1258` n `6`; index avg `-1.6023` n `23`; metal avg `-1.2491` n `18`; unknown avg `-0.2027` n `424`
- 24h: commodity avg `-1.2249` n `12`; crypto_alt avg `-8.1907` n `228`; crypto_major avg `-6.7696` n `8`; equity avg `-6.8492` n `74`; fx avg `-0.0602` n `6`; index avg `-3.875` n `23`; metal avg `-4.4658` n `18`; unknown avg `-0.8189` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
