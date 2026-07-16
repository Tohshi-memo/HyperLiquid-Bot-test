# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T19:52:27.410200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `-0.0116` n `230`; crypto_major avg `-0.0496` n `8`; equity avg `0.0201` n `94`; fx avg `0.0088` n `6`; index avg `0.0236` n `25`; metal avg `0.0668` n `20`; unknown avg `-0.0636` n `768`
- 1h: commodity avg `0.0484` n `12`; crypto_alt avg `-0.0801` n `230`; crypto_major avg `-0.0189` n `8`; equity avg `-0.2032` n `94`; fx avg `0.0078` n `6`; index avg `-0.0471` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.1093` n `768`
- 4h: commodity avg `0.0262` n `12`; crypto_alt avg `-0.746` n `230`; crypto_major avg `-1.2248` n `8`; equity avg `-0.9641` n `94`; fx avg `-0.0121` n `6`; index avg `-0.2696` n `25`; metal avg `-0.3459` n `20`; unknown avg `-0.0267` n `768`
- 24h: commodity avg `-0.3495` n `12`; crypto_alt avg `-0.7662` n `230`; crypto_major avg `-1.7944` n `8`; equity avg `-3.8231` n `94`; fx avg `-0.1492` n `6`; index avg `-0.5636` n `25`; metal avg `-0.796` n `20`; unknown avg `-0.3736` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
