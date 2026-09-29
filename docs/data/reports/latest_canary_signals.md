# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T19:07:37.521666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `0.1865` n `234`; crypto_major avg `0.1155` n `8`; equity avg `0.0058` n `142`; fx avg `-0.0088` n `6`; index avg `0.007` n `26`; metal avg `0.0173` n `20`; unknown avg `1.9833` n `960`
- 1h: commodity avg `-0.0817` n `12`; crypto_alt avg `1.0699` n `234`; crypto_major avg `0.7249` n `8`; equity avg `0.1337` n `142`; fx avg `-0.0059` n `6`; index avg `0.0646` n `26`; metal avg `0.1248` n `20`; unknown avg `3.4659` n `960`
- 4h: commodity avg `-0.3454` n `12`; crypto_alt avg `-0.738` n `234`; crypto_major avg `-0.308` n `8`; equity avg `-0.2343` n `142`; fx avg `-0.0589` n `6`; index avg `0.0312` n `26`; metal avg `0.161` n `20`; unknown avg `11.3227` n `950`
- 24h: commodity avg `-0.7595` n `12`; crypto_alt avg `1.0426` n `234`; crypto_major avg `-0.2639` n `8`; equity avg `0.51` n `142`; fx avg `-0.1809` n `6`; index avg `0.0541` n `26`; metal avg `0.1052` n `20`; unknown avg `1.445` n `788`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
