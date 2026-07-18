# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T08:52:28.862033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0707` n `230`; crypto_major avg `-0.0667` n `8`; equity avg `-0.0336` n `96`; fx avg `0.013` n `6`; index avg `0.0197` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0052` n `769`
- 1h: commodity avg `0.0196` n `12`; crypto_alt avg `-0.0163` n `230`; crypto_major avg `-0.0178` n `8`; equity avg `-0.0662` n `96`; fx avg `0.0078` n `6`; index avg `0.0627` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0714` n `769`
- 4h: commodity avg `0.06` n `12`; crypto_alt avg `-0.2047` n `230`; crypto_major avg `-0.0177` n `8`; equity avg `-0.1071` n `96`; fx avg `0.0017` n `6`; index avg `0.0257` n `25`; metal avg `0.019` n `20`; unknown avg `-0.055` n `737`
- 24h: commodity avg `0.7973` n `12`; crypto_alt avg `-0.0684` n `230`; crypto_major avg `0.6117` n `8`; equity avg `1.8753` n `96`; fx avg `0.018` n `6`; index avg `0.3141` n `25`; metal avg `0.2716` n `20`; unknown avg `0.3029` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
