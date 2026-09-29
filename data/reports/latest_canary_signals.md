# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T21:37:31.301238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `-0.0631` n `234`; crypto_major avg `-0.0471` n `8`; equity avg `0.0149` n `142`; fx avg `0.011` n `6`; index avg `-0.001` n `26`; metal avg `-0.005` n `20`; unknown avg `0.1401` n `962`
- 1h: commodity avg `0.1075` n `12`; crypto_alt avg `-0.2098` n `234`; crypto_major avg `-0.1902` n `8`; equity avg `0.0615` n `142`; fx avg `-0.0001` n `6`; index avg `-0.0111` n `26`; metal avg `0.0123` n `20`; unknown avg `2.5495` n `956`
- 4h: commodity avg `-0.2483` n `12`; crypto_alt avg `0.7212` n `234`; crypto_major avg `0.3814` n `8`; equity avg `0.2174` n `142`; fx avg `0.0137` n `6`; index avg `0.0909` n `26`; metal avg `0.2927` n `20`; unknown avg `2.1866` n `896`
- 24h: commodity avg `-1.0086` n `12`; crypto_alt avg `1.0439` n `234`; crypto_major avg `-0.2296` n `8`; equity avg `0.7294` n `142`; fx avg `-0.1641` n `6`; index avg `0.0672` n `26`; metal avg `0.2831` n `20`; unknown avg `3098.9237` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1953`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
