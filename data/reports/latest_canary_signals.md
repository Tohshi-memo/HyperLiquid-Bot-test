# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T23:22:15.124454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0719` n `12`; crypto_alt avg `0.1114` n `228`; crypto_major avg `-0.0461` n `8`; equity avg `-0.0153` n `67`; fx avg `0.0054` n `6`; index avg `0.0359` n `23`; metal avg `-0.0435` n `18`; unknown avg `-0.1923` n `418`
- 1h: commodity avg `-0.0604` n `12`; crypto_alt avg `0.2177` n `228`; crypto_major avg `0.077` n `8`; equity avg `-0.0517` n `67`; fx avg `-0.0082` n `6`; index avg `0.1106` n `23`; metal avg `0.0227` n `18`; unknown avg `-0.292` n `418`
- 4h: commodity avg `-0.2004` n `12`; crypto_alt avg `0.338` n `228`; crypto_major avg `-0.0597` n `8`; equity avg `0.2081` n `67`; fx avg `0.0131` n `6`; index avg `0.0882` n `23`; metal avg `0.2535` n `18`; unknown avg `-0.7314` n `418`
- 24h: commodity avg `0.6491` n `12`; crypto_alt avg `-1.298` n `228`; crypto_major avg `-1.4626` n `8`; equity avg `-0.0841` n `67`; fx avg `-0.1326` n `6`; index avg `0.6903` n `23`; metal avg `-0.879` n `18`; unknown avg `0.066` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
