# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T05:37:15.001541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `0.0679` n `228`; crypto_major avg `0.0245` n `8`; equity avg `0.0161` n `65`; fx avg `0.0195` n `5`; index avg `-0.0162` n `23`; metal avg `0.0129` n `18`; unknown avg `-0.5302` n `376`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0075` n `228`; crypto_major avg `-0.0532` n `8`; equity avg `0.0231` n `65`; fx avg `0.0183` n `5`; index avg `-0.0276` n `23`; metal avg `0.0126` n `18`; unknown avg `-0.6663` n `375`
- 4h: commodity avg `0.1937` n `12`; crypto_alt avg `0.0569` n `228`; crypto_major avg `0.1147` n `8`; equity avg `0.0519` n `65`; fx avg `-0.0004` n `5`; index avg `0.1401` n `23`; metal avg `0.0904` n `18`; unknown avg `-0.6672` n `375`
- 24h: commodity avg `-0.1254` n `12`; crypto_alt avg `4.4901` n `228`; crypto_major avg `2.7192` n `8`; equity avg `3.3561` n `65`; fx avg `0.0576` n `5`; index avg `1.3098` n `23`; metal avg `-0.1216` n `18`; unknown avg `1.3462` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
