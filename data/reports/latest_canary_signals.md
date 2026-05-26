# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T05:52:15.751311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0548` n `12`; crypto_alt avg `-0.2688` n `228`; crypto_major avg `-0.1669` n `8`; equity avg `-0.0655` n `67`; fx avg `-0.0076` n `6`; index avg `-0.042` n `23`; metal avg `-0.2726` n `18`; unknown avg `-0.8756` n `407`
- 1h: commodity avg `0.0451` n `12`; crypto_alt avg `0.3183` n `228`; crypto_major avg `0.2543` n `8`; equity avg `-0.0847` n `67`; fx avg `-0.0265` n `6`; index avg `-0.0626` n `23`; metal avg `-0.0931` n `18`; unknown avg `-0.7034` n `407`
- 4h: commodity avg `-0.0535` n `12`; crypto_alt avg `0.7006` n `228`; crypto_major avg `0.4691` n `8`; equity avg `0.1521` n `67`; fx avg `-0.0445` n `6`; index avg `0.0582` n `23`; metal avg `-0.0147` n `18`; unknown avg `-0.7965` n `407`
- 24h: commodity avg `0.6385` n `12`; crypto_alt avg `-0.4352` n `228`; crypto_major avg `-1.0651` n `8`; equity avg `-0.6535` n `67`; fx avg `-0.0671` n `6`; index avg `-0.0169` n `23`; metal avg `-0.3364` n `18`; unknown avg `0.3562` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1837`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
