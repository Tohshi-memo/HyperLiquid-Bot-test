# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T20:37:28.865160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.2199` n `233`; crypto_major avg `-0.0662` n `8`; equity avg `-0.034` n `134`; fx avg `-0.006` n `6`; index avg `-0.0143` n `26`; metal avg `-0.0268` n `20`; unknown avg `2.3409` n `791`
- 1h: commodity avg `0.1462` n `12`; crypto_alt avg `-0.2252` n `233`; crypto_major avg `-0.101` n `8`; equity avg `-0.1178` n `134`; fx avg `0.0002` n `6`; index avg `-0.056` n `26`; metal avg `-0.0672` n `20`; unknown avg `0.5816` n `765`
- 4h: commodity avg `0.3929` n `12`; crypto_alt avg `-1.1461` n `233`; crypto_major avg `-0.5948` n `8`; equity avg `-0.4701` n `134`; fx avg `-0.0444` n `6`; index avg `-0.0812` n `26`; metal avg `-0.2299` n `20`; unknown avg `0.3621` n `749`
- 24h: commodity avg `0.0703` n `12`; crypto_alt avg `-0.5252` n `232`; crypto_major avg `-0.2235` n `8`; equity avg `0.3117` n `134`; fx avg `-0.1027` n `6`; index avg `-0.175` n `26`; metal avg `-0.3205` n `20`; unknown avg `14.4076` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
