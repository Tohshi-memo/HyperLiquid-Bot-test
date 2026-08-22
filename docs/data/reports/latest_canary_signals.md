# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T20:52:25.443920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.0392` n `230`; crypto_major avg `0.0212` n `8`; equity avg `-0.0006` n `121`; fx avg `0.0064` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.009` n `794`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.1029` n `230`; crypto_major avg `0.1858` n `8`; equity avg `0.0471` n `121`; fx avg `0.0166` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.0316` n `794`
- 4h: commodity avg `0.0647` n `12`; crypto_alt avg `0.0111` n `230`; crypto_major avg `0.9536` n `8`; equity avg `0.1575` n `121`; fx avg `0.0331` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0015` n `20`; unknown avg `1.2946` n `794`
- 24h: commodity avg `0.0403` n `12`; crypto_alt avg `0.72` n `230`; crypto_major avg `3.8379` n `8`; equity avg `-0.3627` n `121`; fx avg `0.0865` n `6`; index avg `-0.0405` n `25`; metal avg `-0.0555` n `20`; unknown avg `3.2065` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
