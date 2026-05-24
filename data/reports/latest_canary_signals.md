# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T17:52:18.023115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0691` n `228`; crypto_major avg `-0.0136` n `8`; equity avg `0.0291` n `67`; fx avg `0.0` n `6`; index avg `0.0854` n `23`; metal avg `-0.0105` n `18`; unknown avg `-0.0631` n `396`
- 1h: commodity avg `0.1304` n `12`; crypto_alt avg `0.203` n `228`; crypto_major avg `0.0854` n `8`; equity avg `0.0507` n `67`; fx avg `-0.0022` n `6`; index avg `0.06` n `23`; metal avg `-0.0608` n `18`; unknown avg `-0.0579` n `396`
- 4h: commodity avg `0.7325` n `12`; crypto_alt avg `-0.1797` n `228`; crypto_major avg `-0.4582` n `8`; equity avg `-0.2427` n `67`; fx avg `0.0083` n `6`; index avg `-0.2161` n `23`; metal avg `-0.275` n `18`; unknown avg `-0.3278` n `396`
- 24h: commodity avg `-1.2485` n `12`; crypto_alt avg `0.6126` n `228`; crypto_major avg `2.3717` n `8`; equity avg `1.6982` n `67`; fx avg `0.0897` n `6`; index avg `0.6697` n `23`; metal avg `0.5378` n `18`; unknown avg `1.1834` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
