# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T06:22:32.566952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.121` n `12`; crypto_alt avg `0.007` n `228`; crypto_major avg `0.0562` n `8`; equity avg `0.0481` n `77`; fx avg `0.017` n `6`; index avg `0.0189` n `23`; metal avg `0.0675` n `18`; unknown avg `0.4629` n `687`
- 1h: commodity avg `0.1988` n `12`; crypto_alt avg `0.1874` n `228`; crypto_major avg `0.1753` n `8`; equity avg `-0.0069` n `77`; fx avg `-0.0042` n `6`; index avg `0.1549` n `23`; metal avg `-0.1888` n `18`; unknown avg `0.7083` n `647`
- 4h: commodity avg `-0.0751` n `12`; crypto_alt avg `0.5704` n `228`; crypto_major avg `0.8684` n `8`; equity avg `0.4084` n `77`; fx avg `-0.0144` n `6`; index avg `0.0565` n `23`; metal avg `0.3075` n `18`; unknown avg `0.8557` n `639`
- 24h: commodity avg `0.4545` n `12`; crypto_alt avg `0.3085` n `228`; crypto_major avg `2.3913` n `8`; equity avg `1.2897` n `76`; fx avg `-0.1076` n `6`; index avg `0.4707` n `23`; metal avg `-0.1491` n `18`; unknown avg `1.6175` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
