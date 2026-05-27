# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T15:07:25.306409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `0.2516` n `228`; crypto_major avg `0.0897` n `8`; equity avg `-0.3012` n `67`; fx avg `-0.0356` n `6`; index avg `-0.1022` n `23`; metal avg `-0.1011` n `18`; unknown avg `0.0311` n `418`
- 1h: commodity avg `0.3884` n `12`; crypto_alt avg `0.1192` n `228`; crypto_major avg `0.0361` n `8`; equity avg `-0.4125` n `67`; fx avg `-0.0237` n `6`; index avg `-0.3514` n `23`; metal avg `-0.2357` n `18`; unknown avg `0.1133` n `418`
- 4h: commodity avg `0.4534` n `12`; crypto_alt avg `-0.0702` n `228`; crypto_major avg `-0.9035` n `8`; equity avg `-1.1074` n `67`; fx avg `-0.0419` n `6`; index avg `-1.0291` n `23`; metal avg `-0.2053` n `18`; unknown avg `0.1159` n `418`
- 24h: commodity avg `-1.2444` n `12`; crypto_alt avg `-1.7192` n `228`; crypto_major avg `-1.5847` n `8`; equity avg `-0.3509` n `67`; fx avg `-0.0676` n `6`; index avg `-0.6252` n `23`; metal avg `-1.2161` n `18`; unknown avg `0.2806` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
