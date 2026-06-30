# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T19:37:28.067539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.1808` n `228`; crypto_major avg `0.3253` n `8`; equity avg `0.0095` n `88`; fx avg `0.0112` n `6`; index avg `-0.0297` n `23`; metal avg `-0.0235` n `20`; unknown avg `0.0921` n `765`
- 1h: commodity avg `0.0595` n `12`; crypto_alt avg `0.2605` n `228`; crypto_major avg `0.5152` n `8`; equity avg `0.1785` n `88`; fx avg `0.0013` n `6`; index avg `-0.0125` n `23`; metal avg `-0.0406` n `20`; unknown avg `-0.0439` n `765`
- 4h: commodity avg `-0.1566` n `12`; crypto_alt avg `0.2329` n `228`; crypto_major avg `0.8411` n `8`; equity avg `0.7137` n `88`; fx avg `-0.0299` n `6`; index avg `0.0532` n `23`; metal avg `-0.0486` n `20`; unknown avg `-0.0629` n `765`
- 24h: commodity avg `0.1338` n `12`; crypto_alt avg `-2.2875` n `228`; crypto_major avg `-2.1387` n `8`; equity avg `1.2192` n `88`; fx avg `0.1435` n `6`; index avg `0.2664` n `23`; metal avg `0.1541` n `20`; unknown avg `7.538` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
