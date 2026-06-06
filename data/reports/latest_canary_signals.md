# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T05:22:20.901748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0851` n `12`; crypto_alt avg `2.1198` n `228`; crypto_major avg `1.9455` n `8`; equity avg `0.4048` n `74`; fx avg `0.0011` n `6`; index avg `0.1125` n `23`; metal avg `0.0588` n `18`; unknown avg `9.3994` n `425`
- 1h: commodity avg `-0.2918` n `12`; crypto_alt avg `0.6573` n `228`; crypto_major avg `0.9315` n `8`; equity avg `-0.0844` n `74`; fx avg `-0.0147` n `6`; index avg `-0.3437` n `23`; metal avg `-0.124` n `18`; unknown avg `3.3525` n `425`
- 4h: commodity avg `-0.4102` n `12`; crypto_alt avg `-2.789` n `228`; crypto_major avg `-1.5363` n `8`; equity avg `-1.4553` n `74`; fx avg `-0.0198` n `6`; index avg `-0.907` n `23`; metal avg `-0.7147` n `18`; unknown avg `0.0981` n `425`
- 24h: commodity avg `-1.5995` n `12`; crypto_alt avg `-7.6726` n `228`; crypto_major avg `-5.7063` n `8`; equity avg `-7.1844` n `74`; fx avg `-0.1822` n `6`; index avg `-4.4095` n `23`; metal avg `-4.3886` n `18`; unknown avg `-0.9754` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
