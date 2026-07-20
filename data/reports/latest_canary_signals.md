# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T20:37:41.736540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `0.1671` n `230`; crypto_major avg `0.1869` n `8`; equity avg `0.0314` n `98`; fx avg `0.0014` n `6`; index avg `0.0105` n `25`; metal avg `0.0147` n `20`; unknown avg `0.0121` n `770`
- 1h: commodity avg `-0.025` n `12`; crypto_alt avg `0.4369` n `230`; crypto_major avg `0.4881` n `8`; equity avg `-0.1919` n `98`; fx avg `-0.0089` n `6`; index avg `-0.0525` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.052` n `770`
- 4h: commodity avg `0.1239` n `12`; crypto_alt avg `0.2543` n `230`; crypto_major avg `-0.0092` n `8`; equity avg `-1.1436` n `98`; fx avg `-0.0136` n `6`; index avg `-0.2109` n `25`; metal avg `-0.1042` n `20`; unknown avg `-0.1501` n `770`
- 24h: commodity avg `-0.4009` n `12`; crypto_alt avg `1.7411` n `230`; crypto_major avg `1.3317` n `8`; equity avg `-0.3402` n `98`; fx avg `-0.2251` n `6`; index avg `0.0164` n `25`; metal avg `0.1069` n `20`; unknown avg `0.3101` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.094`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `666`, weak_sample_signal
