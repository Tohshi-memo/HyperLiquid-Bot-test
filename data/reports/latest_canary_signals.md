# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T21:37:26.625612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `0.1836` n `228`; crypto_major avg `0.1415` n `8`; equity avg `0.0368` n `88`; fx avg `0.023` n `6`; index avg `0.0004` n `23`; metal avg `0.0015` n `20`; unknown avg `-0.0834` n `764`
- 1h: commodity avg `0.0694` n `12`; crypto_alt avg `0.1181` n `228`; crypto_major avg `0.0935` n `8`; equity avg `0.07` n `88`; fx avg `0.1167` n `6`; index avg `0.0065` n `23`; metal avg `0.1405` n `20`; unknown avg `-0.6906` n `764`
- 4h: commodity avg `0.1052` n `12`; crypto_alt avg `-0.234` n `228`; crypto_major avg `-0.182` n `8`; equity avg `-0.2117` n `87`; fx avg `0.1158` n `6`; index avg `-0.1706` n `23`; metal avg `-0.0246` n `20`; unknown avg `-0.7781` n `764`
- 24h: commodity avg `-0.2064` n `12`; crypto_alt avg `1.3686` n `228`; crypto_major avg `1.1338` n `8`; equity avg `-0.5958` n `87`; fx avg `0.0524` n `6`; index avg `-0.3563` n `23`; metal avg `0.5983` n `20`; unknown avg `-0.6868` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2193`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
