# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T04:37:21.045330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.7249` n `228`; crypto_major avg `0.8174` n `8`; equity avg `0.1449` n `74`; fx avg `0.0273` n `6`; index avg `0.0389` n `23`; metal avg `-0.0186` n `18`; unknown avg `-0.2769` n `517`
- 1h: commodity avg `0.042` n `12`; crypto_alt avg `1.2786` n `228`; crypto_major avg `0.8988` n `8`; equity avg `0.5198` n `74`; fx avg `0.0025` n `6`; index avg `0.2524` n `23`; metal avg `-0.0221` n `18`; unknown avg `-0.388` n `517`
- 4h: commodity avg `-0.1305` n `12`; crypto_alt avg `0.7726` n `228`; crypto_major avg `0.8051` n `8`; equity avg `1.3126` n `74`; fx avg `0.0009` n `6`; index avg `0.7012` n `23`; metal avg `0.2723` n `18`; unknown avg `-0.1486` n `517`
- 24h: commodity avg `-1.3146` n `12`; crypto_alt avg `0.7882` n `228`; crypto_major avg `1.4272` n `8`; equity avg `2.3129` n `74`; fx avg `-0.2958` n `6`; index avg `1.0376` n `23`; metal avg `0.1304` n `18`; unknown avg `-2.9596` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
