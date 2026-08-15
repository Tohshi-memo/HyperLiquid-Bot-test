# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T04:07:29.645487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.0965` n `230`; crypto_major avg `-0.0118` n `8`; equity avg `0.0373` n `114`; fx avg `-0.0051` n `6`; index avg `0.0031` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.0021` n `791`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `-0.1048` n `230`; crypto_major avg `-0.0727` n `8`; equity avg `0.0643` n `114`; fx avg `-0.0344` n `6`; index avg `0.0013` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.017` n `791`
- 4h: commodity avg `-0.0532` n `12`; crypto_alt avg `-0.0002` n `230`; crypto_major avg `0.2117` n `8`; equity avg `0.1397` n `114`; fx avg `0.0526` n `6`; index avg `0.0077` n `25`; metal avg `-0.03` n `20`; unknown avg `0.2821` n `791`
- 24h: commodity avg `0.1516` n `12`; crypto_alt avg `0.3959` n `230`; crypto_major avg `-0.2671` n `8`; equity avg `-0.024` n `114`; fx avg `0.1613` n `6`; index avg `-0.0192` n `25`; metal avg `0.4051` n `20`; unknown avg `0.0312` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
