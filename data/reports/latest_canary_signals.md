# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T00:22:29.987679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0823` n `12`; crypto_alt avg `-0.0896` n `228`; crypto_major avg `-0.1577` n `8`; equity avg `-0.0416` n `78`; fx avg `0.0071` n `6`; index avg `-0.0051` n `23`; metal avg `0.0062` n `18`; unknown avg `96.5264` n `687`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `0.4162` n `228`; crypto_major avg `0.2334` n `8`; equity avg `0.1201` n `78`; fx avg `0.0306` n `6`; index avg `0.0535` n `23`; metal avg `0.005` n `18`; unknown avg `-0.2834` n `679`
- 4h: commodity avg `0.0205` n `12`; crypto_alt avg `0.6679` n `228`; crypto_major avg `0.5141` n `8`; equity avg `0.2735` n `78`; fx avg `0.0181` n `6`; index avg `0.0504` n `23`; metal avg `0.0603` n `18`; unknown avg `-0.2598` n `679`
- 24h: commodity avg `0.2898` n `12`; crypto_alt avg `-3.2949` n `228`; crypto_major avg `-4.3494` n `8`; equity avg `0.9428` n `78`; fx avg `-0.0849` n `6`; index avg `0.2763` n `23`; metal avg `-4.1052` n `18`; unknown avg `-0.3773` n `564`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
