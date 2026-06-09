# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T20:37:41.472063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5281` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1045` n `12`; crypto_alt avg `0.2675` n `228`; crypto_major avg `0.2427` n `8`; equity avg `0.1046` n `74`; fx avg `0.0132` n `6`; index avg `0.1324` n `23`; metal avg `0.0111` n `18`; unknown avg `0.0551` n `547`
- 1h: commodity avg `0.0952` n `12`; crypto_alt avg `0.3671` n `228`; crypto_major avg `0.1753` n `8`; equity avg `0.4578` n `74`; fx avg `-0.0408` n `6`; index avg `0.6751` n `23`; metal avg `0.0962` n `18`; unknown avg `0.2481` n `547`
- 4h: commodity avg `0.7119` n `12`; crypto_alt avg `1.6399` n `228`; crypto_major avg `1.0792` n `8`; equity avg `2.6073` n `74`; fx avg `-0.0857` n `6`; index avg `1.6832` n `23`; metal avg `0.1088` n `18`; unknown avg `0.6426` n `547`
- 24h: commodity avg `-0.7926` n `12`; crypto_alt avg `-1.3277` n `228`; crypto_major avg `-2.3493` n `8`; equity avg `-1.6838` n `74`; fx avg `0.06` n `6`; index avg `-0.7575` n `23`; metal avg `-1.3517` n `18`; unknown avg `-1.0257` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0423`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0409`, n `668`, weak_sample_signal
