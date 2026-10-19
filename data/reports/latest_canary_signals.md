# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T12:22:32.440371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0606` n `13`; crypto_alt avg `0.0356` n `237`; crypto_major avg `0.133` n `8`; equity avg `0.0816` n `151`; fx avg `-0.0163` n `6`; index avg `0.0321` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.0589` n `1191`
- 1h: commodity avg `-0.1041` n `13`; crypto_alt avg `0.5774` n `237`; crypto_major avg `0.4887` n `8`; equity avg `0.4192` n `151`; fx avg `-0.0051` n `6`; index avg `0.0185` n `26`; metal avg `-0.0954` n `20`; unknown avg `0.144` n `1177`
- 4h: commodity avg `0.2805` n `13`; crypto_alt avg `-0.5774` n `237`; crypto_major avg `-0.2452` n `8`; equity avg `0.4756` n `151`; fx avg `0.0455` n `6`; index avg `0.0195` n `26`; metal avg `0.0072` n `20`; unknown avg `0.2155` n `1177`
- 24h: commodity avg `-0.254` n `13`; crypto_alt avg `-0.3331` n `237`; crypto_major avg `0.5156` n `8`; equity avg `2.8386` n `151`; fx avg `-0.038` n `6`; index avg `0.454` n `26`; metal avg `0.2055` n `20`; unknown avg `0.9545` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1976`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1488`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.132`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0581`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
