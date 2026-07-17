# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T02:22:32.062365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.1292` n `230`; crypto_major avg `-0.0359` n `8`; equity avg `-0.2508` n `94`; fx avg `0.0001` n `6`; index avg `-0.0189` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0388` n `768`
- 1h: commodity avg `-0.1161` n `12`; crypto_alt avg `-0.5719` n `230`; crypto_major avg `-0.523` n `8`; equity avg `-0.7932` n `94`; fx avg `-0.0145` n `6`; index avg `-0.1176` n `25`; metal avg `-0.1365` n `20`; unknown avg `0.4482` n `768`
- 4h: commodity avg `-0.0046` n `12`; crypto_alt avg `-1.2275` n `230`; crypto_major avg `-1.0794` n `8`; equity avg `-1.6823` n `94`; fx avg `-0.0119` n `6`; index avg `-0.2451` n `25`; metal avg `-0.0926` n `20`; unknown avg `-0.2713` n `768`
- 24h: commodity avg `-0.115` n `12`; crypto_alt avg `-2.2328` n `230`; crypto_major avg `-2.8531` n `8`; equity avg `-5.0521` n `94`; fx avg `-0.159` n `6`; index avg `-0.5994` n `25`; metal avg `-0.7417` n `20`; unknown avg `-0.6969` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
