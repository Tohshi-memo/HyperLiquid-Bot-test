# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T22:37:26.347010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.1195` n `230`; crypto_major avg `-0.085` n `8`; equity avg `0.0176` n `94`; fx avg `-0.001` n `6`; index avg `-0.0106` n `25`; metal avg `0.0108` n `20`; unknown avg `-0.099` n `768`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `-0.3521` n `230`; crypto_major avg `-0.2902` n `8`; equity avg `-0.1802` n `94`; fx avg `-0.0041` n `6`; index avg `-0.0533` n `25`; metal avg `-0.0291` n `20`; unknown avg `-0.2156` n `768`
- 4h: commodity avg `0.2127` n `12`; crypto_alt avg `-0.152` n `230`; crypto_major avg `-0.0504` n `8`; equity avg `-0.372` n `94`; fx avg `-0.0072` n `6`; index avg `-0.0476` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.3414` n `768`
- 24h: commodity avg `-0.192` n `12`; crypto_alt avg `-1.3018` n `230`; crypto_major avg `-2.296` n `8`; equity avg `-3.7173` n `94`; fx avg `-0.1767` n `6`; index avg `-0.5205` n `25`; metal avg `-0.8538` n `20`; unknown avg `-0.4684` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
