# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T19:22:30.719159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `-0.2552` n `228`; crypto_major avg `-0.2279` n `8`; equity avg `0.1573` n `88`; fx avg `-0.0105` n `6`; index avg `0.0054` n `23`; metal avg `-0.0347` n `20`; unknown avg `-0.1061` n `765`
- 1h: commodity avg `0.112` n `12`; crypto_alt avg `-0.2254` n `228`; crypto_major avg `-0.1175` n `8`; equity avg `0.1601` n `88`; fx avg `-0.0075` n `6`; index avg `0.0112` n `23`; metal avg `-0.0355` n `20`; unknown avg `-0.3721` n `765`
- 4h: commodity avg `-0.2076` n `12`; crypto_alt avg `0.1921` n `228`; crypto_major avg `0.6476` n `8`; equity avg `0.7784` n `88`; fx avg `-0.0437` n `6`; index avg `0.1009` n `23`; metal avg `0.0218` n `20`; unknown avg `-0.1405` n `765`
- 24h: commodity avg `0.1304` n `12`; crypto_alt avg `-2.4822` n `228`; crypto_major avg `-2.4058` n `8`; equity avg `1.1901` n `88`; fx avg `0.1335` n `6`; index avg `0.3148` n `23`; metal avg `0.2392` n `20`; unknown avg `8.0519` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
