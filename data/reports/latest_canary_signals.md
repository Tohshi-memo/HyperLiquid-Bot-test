# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T15:22:23.017173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `0.6092` n `228`; crypto_major avg `0.3219` n `8`; equity avg `-0.1903` n `67`; fx avg `0.0074` n `6`; index avg `-0.0206` n `23`; metal avg `0.0102` n `18`; unknown avg `-0.138` n `418`
- 1h: commodity avg `0.5916` n `12`; crypto_alt avg `1.2555` n `228`; crypto_major avg `0.7529` n `8`; equity avg `-0.3761` n `67`; fx avg `-0.0562` n `6`; index avg `-0.1821` n `23`; metal avg `-0.3384` n `18`; unknown avg `-0.1043` n `418`
- 4h: commodity avg `0.469` n `12`; crypto_alt avg `0.4156` n `228`; crypto_major avg `-0.5392` n `8`; equity avg `-1.2972` n `67`; fx avg `-0.0404` n `6`; index avg `-1.0373` n `23`; metal avg `-0.0804` n `18`; unknown avg `-0.1945` n `418`
- 24h: commodity avg `-1.168` n `12`; crypto_alt avg `-1.0549` n `228`; crypto_major avg `-1.2342` n `8`; equity avg `-0.6218` n `67`; fx avg `-0.0551` n `6`; index avg `-0.5965` n `23`; metal avg `-1.1818` n `18`; unknown avg `0.486` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
