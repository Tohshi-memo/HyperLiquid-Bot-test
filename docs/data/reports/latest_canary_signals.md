# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T04:22:16.582340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1368` n `12`; crypto_alt avg `-0.2891` n `228`; crypto_major avg `-0.2648` n `8`; equity avg `-0.0389` n `67`; fx avg `-0.0058` n `6`; index avg `-0.0271` n `23`; metal avg `-0.0094` n `18`; unknown avg `0.8347` n `418`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.7546` n `228`; crypto_major avg `-0.6018` n `8`; equity avg `-0.1652` n `67`; fx avg `-0.02` n `6`; index avg `-0.1006` n `23`; metal avg `-0.1951` n `18`; unknown avg `0.4381` n `418`
- 4h: commodity avg `-0.5103` n `12`; crypto_alt avg `-1.0272` n `228`; crypto_major avg `-0.3793` n `8`; equity avg `0.0262` n `67`; fx avg `-0.0767` n `6`; index avg `-0.0031` n `23`; metal avg `-0.5316` n `18`; unknown avg `0.3674` n `418`
- 24h: commodity avg `-0.256` n `12`; crypto_alt avg `-1.1181` n `228`; crypto_major avg `-0.553` n `8`; equity avg `0.517` n `67`; fx avg `-0.0776` n `6`; index avg `0.8632` n `23`; metal avg `-0.2138` n `18`; unknown avg `0.4747` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
