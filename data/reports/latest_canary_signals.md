# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T23:22:27.086673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.4378` n `230`; crypto_major avg `-0.4009` n `8`; equity avg `-0.2188` n `94`; fx avg `0.0089` n `6`; index avg `-0.0137` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.2619` n `768`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `-1.0309` n `230`; crypto_major avg `-0.9434` n `8`; equity avg `-0.4952` n `94`; fx avg `0.016` n `6`; index avg `-0.031` n `25`; metal avg `0.004` n `20`; unknown avg `-0.3138` n `768`
- 4h: commodity avg `0.1278` n `12`; crypto_alt avg `-1.0082` n `230`; crypto_major avg `-0.9941` n `8`; equity avg `-0.6486` n `94`; fx avg `-0.0032` n `6`; index avg `0.002` n `25`; metal avg `-0.0618` n `20`; unknown avg `-0.3792` n `768`
- 24h: commodity avg `-0.1682` n `12`; crypto_alt avg `-2.1286` n `230`; crypto_major avg `-3.1004` n `8`; equity avg `-4.3356` n `94`; fx avg `-0.1381` n `6`; index avg `-0.5738` n `25`; metal avg `-0.8512` n `20`; unknown avg `-0.5818` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
