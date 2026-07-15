# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T08:52:26.317114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0627` n `12`; crypto_alt avg `0.0268` n `230`; crypto_major avg `0.1197` n `8`; equity avg `0.0767` n `93`; fx avg `-0.0129` n `6`; index avg `0.0172` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.0619` n `767`
- 1h: commodity avg `-0.1619` n `12`; crypto_alt avg `0.1029` n `230`; crypto_major avg `0.2247` n `8`; equity avg `-0.1853` n `93`; fx avg `0.0003` n `6`; index avg `-0.0302` n `25`; metal avg `0.0844` n `20`; unknown avg `-0.0307` n `767`
- 4h: commodity avg `-0.0885` n `12`; crypto_alt avg `-0.1721` n `230`; crypto_major avg `-0.0684` n `8`; equity avg `-0.3281` n `93`; fx avg `-0.0159` n `6`; index avg `-0.1005` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.1307` n `747`
- 24h: commodity avg `-0.2062` n `12`; crypto_alt avg `1.4953` n `230`; crypto_major avg `3.1009` n `8`; equity avg `1.1332` n `92`; fx avg `0.0266` n `6`; index avg `0.4114` n `25`; metal avg `0.3417` n `20`; unknown avg `0.2265` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
