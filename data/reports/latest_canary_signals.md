# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T18:07:26.581833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.0467` n `234`; crypto_major avg `0.0388` n `8`; equity avg `0.0051` n `140`; fx avg `0.0048` n `6`; index avg `0.0118` n `26`; metal avg `-0.001` n `20`; unknown avg `0.0646` n `941`
- 1h: commodity avg `0.0461` n `12`; crypto_alt avg `-0.4303` n `234`; crypto_major avg `-0.4691` n `8`; equity avg `-0.0302` n `140`; fx avg `0.0027` n `6`; index avg `0.0112` n `26`; metal avg `0.0022` n `20`; unknown avg `1.3966` n `933`
- 4h: commodity avg `-0.0887` n `12`; crypto_alt avg `0.1246` n `234`; crypto_major avg `-0.0737` n `8`; equity avg `0.0044` n `140`; fx avg `-0.0093` n `6`; index avg `0.0221` n `26`; metal avg `-0.003` n `20`; unknown avg `6.4898` n `882`
- 24h: commodity avg `-0.0048` n `12`; crypto_alt avg `2.509` n `234`; crypto_major avg `1.0634` n `8`; equity avg `0.4587` n `140`; fx avg `0.0213` n `6`; index avg `0.1272` n `26`; metal avg `-0.1283` n `20`; unknown avg `4.3129` n `792`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
