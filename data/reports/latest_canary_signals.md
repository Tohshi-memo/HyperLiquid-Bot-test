# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T16:52:27.102646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.1157` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.7637` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.6949` n `12`; crypto_alt avg `-0.6342` n `228`; crypto_major avg `-0.3195` n `8`; equity avg `-0.629` n `74`; fx avg `-0.015` n `6`; index avg `-0.4325` n `23`; metal avg `-0.4594` n `18`; unknown avg `-0.1701` n `547`
- 1h: commodity avg `0.3596` n `12`; crypto_alt avg `-0.8474` n `228`; crypto_major avg `-0.4873` n `8`; equity avg `-2.251` n `74`; fx avg `-0.0143` n `6`; index avg `-1.331` n `23`; metal avg `-0.7745` n `18`; unknown avg `-0.4134` n `547`
- 4h: commodity avg `-0.6655` n `12`; crypto_alt avg `-2.3057` n `228`; crypto_major avg `-2.5261` n `8`; equity avg `-5.6418` n `74`; fx avg `-0.0571` n `6`; index avg `-3.4299` n `23`; metal avg `-2.716` n `18`; unknown avg `1.1326` n `545`
- 24h: commodity avg `-0.9016` n `12`; crypto_alt avg `-3.5722` n `228`; crypto_major avg `-3.7247` n `8`; equity avg `-5.2677` n `74`; fx avg `0.1026` n `6`; index avg `-3.1289` n `23`; metal avg `-2.2793` n `18`; unknown avg `-1.7021` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
