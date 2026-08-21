# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T15:52:29.811949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5915` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.1022` n `230`; crypto_major avg `-0.0085` n `8`; equity avg `0.2788` n `121`; fx avg `0.0041` n `6`; index avg `0.0515` n `25`; metal avg `0.0273` n `20`; unknown avg `0.071` n `793`
- 1h: commodity avg `0.0311` n `12`; crypto_alt avg `-0.0749` n `230`; crypto_major avg `-0.1004` n `8`; equity avg `0.4761` n `121`; fx avg `0.0082` n `6`; index avg `0.1185` n `25`; metal avg `0.1076` n `20`; unknown avg `-0.0553` n `793`
- 4h: commodity avg `0.0594` n `12`; crypto_alt avg `1.458` n `230`; crypto_major avg `1.3822` n `8`; equity avg `-0.2093` n `121`; fx avg `0.004` n `6`; index avg `-0.0086` n `23`; metal avg `-0.0669` n `18`; unknown avg `0.1288` n `774`
- 24h: commodity avg `0.2101` n `12`; crypto_alt avg `7.433` n `230`; crypto_major avg `5.1018` n `8`; equity avg `1.4527` n `121`; fx avg `-0.0955` n `6`; index avg `0.1772` n `25`; metal avg `0.5578` n `20`; unknown avg `2.4181` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2409`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
