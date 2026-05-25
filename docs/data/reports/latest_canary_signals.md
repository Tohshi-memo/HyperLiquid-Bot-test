# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T07:52:19.243793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1222` n `12`; crypto_alt avg `0.082` n `228`; crypto_major avg `0.1922` n `8`; equity avg `0.0267` n `67`; fx avg `0.0033` n `6`; index avg `-0.0147` n `23`; metal avg `0.083` n `18`; unknown avg `0.1445` n `397`
- 1h: commodity avg `0.0462` n `12`; crypto_alt avg `0.0174` n `228`; crypto_major avg `0.1378` n `8`; equity avg `0.0627` n `67`; fx avg `0.0058` n `6`; index avg `-0.0272` n `23`; metal avg `0.2089` n `18`; unknown avg `0.0618` n `397`
- 4h: commodity avg `0.3516` n `12`; crypto_alt avg `1.0406` n `228`; crypto_major avg `0.843` n `8`; equity avg `0.1293` n `67`; fx avg `0.0561` n `6`; index avg `0.1561` n `23`; metal avg `0.2011` n `18`; unknown avg `0.2895` n `387`
- 24h: commodity avg `0.2126` n `12`; crypto_alt avg `0.1926` n `228`; crypto_major avg `0.3177` n `8`; equity avg `0.4915` n `67`; fx avg `-0.0069` n `6`; index avg `-0.1192` n `23`; metal avg `0.5097` n `18`; unknown avg `0.1112` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
