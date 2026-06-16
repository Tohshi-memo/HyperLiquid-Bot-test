# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T04:37:34.923829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.3528` n `228`; crypto_major avg `-0.2505` n `8`; equity avg `-0.0332` n `77`; fx avg `-0.0043` n `6`; index avg `-0.141` n `23`; metal avg `-0.0451` n `18`; unknown avg `0.2715` n `687`
- 1h: commodity avg `-0.0435` n `12`; crypto_alt avg `-0.4207` n `228`; crypto_major avg `-0.24` n `8`; equity avg `0.0132` n `77`; fx avg `0.0097` n `6`; index avg `-0.1636` n `23`; metal avg `-0.063` n `18`; unknown avg `0.8773` n `687`
- 4h: commodity avg `-0.4239` n `12`; crypto_alt avg `-0.8844` n `228`; crypto_major avg `-0.3817` n `8`; equity avg `0.1313` n `77`; fx avg `-0.0239` n `6`; index avg `-0.0997` n `23`; metal avg `-0.01` n `18`; unknown avg `0.2169` n `671`
- 24h: commodity avg `0.3435` n `12`; crypto_alt avg `0.0321` n `228`; crypto_major avg `1.735` n `8`; equity avg `1.0847` n `76`; fx avg `-0.0779` n `6`; index avg `0.5069` n `23`; metal avg `-0.3923` n `18`; unknown avg `0.8982` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
