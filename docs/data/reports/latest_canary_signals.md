# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T18:22:38.052219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1552` n `12`; crypto_alt avg `-0.0317` n `228`; crypto_major avg `-0.0402` n `8`; equity avg `-0.1052` n `86`; fx avg `-0.0007` n `6`; index avg `-0.0438` n `23`; metal avg `-0.0316` n `20`; unknown avg `-0.153` n `766`
- 1h: commodity avg `-0.1373` n `12`; crypto_alt avg `0.0095` n `228`; crypto_major avg `0.0275` n `8`; equity avg `-0.2554` n `86`; fx avg `-0.003` n `6`; index avg `-0.0622` n `23`; metal avg `-0.1085` n `20`; unknown avg `-0.0398` n `765`
- 4h: commodity avg `-0.1673` n `12`; crypto_alt avg `1.2642` n `228`; crypto_major avg `0.7968` n `8`; equity avg `-0.0608` n `86`; fx avg `-0.0431` n `6`; index avg `-0.0496` n `23`; metal avg `-0.1735` n `20`; unknown avg `0.0014` n `765`
- 24h: commodity avg `-0.6435` n `12`; crypto_alt avg `2.3686` n `228`; crypto_major avg `2.3699` n `8`; equity avg `-0.579` n `86`; fx avg `-0.0737` n `6`; index avg `-0.2877` n `23`; metal avg `0.4463` n `20`; unknown avg `0.3978` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2123`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
