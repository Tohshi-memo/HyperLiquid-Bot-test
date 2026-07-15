# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T09:52:28.629013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `-0.1425` n `230`; crypto_major avg `-0.2179` n `8`; equity avg `-0.0067` n `93`; fx avg `0.0042` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0253` n `20`; unknown avg `-0.0469` n `767`
- 1h: commodity avg `0.1551` n `12`; crypto_alt avg `0.0827` n `230`; crypto_major avg `0.0001` n `8`; equity avg `0.0111` n `93`; fx avg `0.0004` n `6`; index avg `-0.0128` n `25`; metal avg `-0.1131` n `20`; unknown avg `-0.0798` n `767`
- 4h: commodity avg `0.0849` n `12`; crypto_alt avg `-0.0278` n `230`; crypto_major avg `-0.0518` n `8`; equity avg `-0.151` n `93`; fx avg `0.0304` n `6`; index avg `-0.072` n `25`; metal avg `-0.0513` n `20`; unknown avg `-0.1673` n `747`
- 24h: commodity avg `-0.1057` n `12`; crypto_alt avg `1.7011` n `230`; crypto_major avg `3.2871` n `8`; equity avg `1.1552` n `92`; fx avg `0.0295` n `6`; index avg `0.409` n `25`; metal avg `0.2054` n `20`; unknown avg `0.2505` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
