# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T18:52:16.551949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0795` n `12`; crypto_alt avg `-0.1825` n `228`; crypto_major avg `-0.0664` n `8`; equity avg `-0.033` n `67`; fx avg `0.0` n `6`; index avg `0.0096` n `23`; metal avg `-0.018` n `18`; unknown avg `-0.2302` n `396`
- 1h: commodity avg `0.1132` n `12`; crypto_alt avg `-0.2949` n `228`; crypto_major avg `-0.2319` n `8`; equity avg `-0.0498` n `67`; fx avg `-0.0083` n `6`; index avg `0.0009` n `23`; metal avg `0.0023` n `18`; unknown avg `-0.2874` n `396`
- 4h: commodity avg `0.1362` n `12`; crypto_alt avg `0.1475` n `228`; crypto_major avg `0.0305` n `8`; equity avg `0.034` n `67`; fx avg `0.0054` n `6`; index avg `-0.0315` n `23`; metal avg `0.0365` n `18`; unknown avg `-0.6152` n `396`
- 24h: commodity avg `-0.4833` n `12`; crypto_alt avg `-0.6505` n `228`; crypto_major avg `1.3519` n `8`; equity avg `1.1318` n `67`; fx avg `0.0809` n `6`; index avg `0.3478` n `23`; metal avg `0.4485` n `18`; unknown avg `0.3161` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
