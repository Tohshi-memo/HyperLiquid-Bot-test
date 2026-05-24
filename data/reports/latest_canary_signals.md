# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T18:37:16.866838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.1407` n `228`; crypto_major avg `-0.0328` n `8`; equity avg `-0.0234` n `67`; fx avg `0.0014` n `6`; index avg `-0.0064` n `23`; metal avg `0.0026` n `18`; unknown avg `-0.0611` n `396`
- 1h: commodity avg `0.0465` n `12`; crypto_alt avg `-0.1813` n `228`; crypto_major avg `-0.179` n `8`; equity avg `0.0124` n `67`; fx avg `-0.0083` n `6`; index avg `0.0767` n `23`; metal avg `0.0098` n `18`; unknown avg `-0.122` n `396`
- 4h: commodity avg `0.0311` n `12`; crypto_alt avg `0.5018` n `228`; crypto_major avg `0.1579` n `8`; equity avg `0.1317` n `67`; fx avg `0.0054` n `6`; index avg `-0.0063` n `23`; metal avg `0.0893` n `18`; unknown avg `-0.3862` n `396`
- 24h: commodity avg `-0.4616` n `12`; crypto_alt avg `-0.6199` n `228`; crypto_major avg `1.3356` n `8`; equity avg `1.0779` n `67`; fx avg `0.0816` n `6`; index avg `0.2062` n `23`; metal avg `0.4667` n `18`; unknown avg `0.7665` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
