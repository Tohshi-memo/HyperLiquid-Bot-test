# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T14:22:29.487609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.2012` n `228`; crypto_major avg `-0.3268` n `8`; equity avg `-0.0037` n `74`; fx avg `-0.0026` n `6`; index avg `0.0538` n `23`; metal avg `-0.2003` n `18`; unknown avg `5.6021` n `643`
- 1h: commodity avg `0.7691` n `12`; crypto_alt avg `-0.426` n `228`; crypto_major avg `-0.249` n `8`; equity avg `-0.0472` n `74`; fx avg `0.0082` n `6`; index avg `0.2668` n `23`; metal avg `-0.4267` n `18`; unknown avg `14.1986` n `643`
- 4h: commodity avg `1.3919` n `12`; crypto_alt avg `-0.7596` n `228`; crypto_major avg `-0.085` n `8`; equity avg `-0.6336` n `74`; fx avg `-0.028` n `6`; index avg `0.1013` n `23`; metal avg `-0.7769` n `18`; unknown avg `15.9746` n `643`
- 24h: commodity avg `-1.2763` n `12`; crypto_alt avg `1.4077` n `228`; crypto_major avg `2.0006` n `8`; equity avg `2.4793` n `74`; fx avg `0.0268` n `6`; index avg `1.7588` n `23`; metal avg `2.3629` n `18`; unknown avg `23.0221` n `514`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
