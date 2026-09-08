# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T12:52:29.365026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.061` n `12`; crypto_alt avg `0.0483` n `232`; crypto_major avg `-0.0019` n `8`; equity avg `-0.0433` n `134`; fx avg `-0.0132` n `6`; index avg `0.0295` n `26`; metal avg `-0.0027` n `20`; unknown avg `-0.0491` n `797`
- 1h: commodity avg `-0.2489` n `12`; crypto_alt avg `0.2353` n `232`; crypto_major avg `0.0854` n `8`; equity avg `0.2612` n `134`; fx avg `-0.0274` n `6`; index avg `0.0717` n `26`; metal avg `0.0156` n `20`; unknown avg `-0.0618` n `789`
- 4h: commodity avg `-0.2856` n `12`; crypto_alt avg `0.075` n `232`; crypto_major avg `-0.1278` n `8`; equity avg `0.7549` n `134`; fx avg `-0.0237` n `6`; index avg `0.1643` n `26`; metal avg `0.0735` n `20`; unknown avg `0.337` n `789`
- 24h: commodity avg `0.0753` n `12`; crypto_alt avg `-0.7238` n `232`; crypto_major avg `-1.5843` n `8`; equity avg `0.1493` n `134`; fx avg `-0.1324` n `6`; index avg `0.0254` n `26`; metal avg `0.1323` n `20`; unknown avg `-0.4938` n `710`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
