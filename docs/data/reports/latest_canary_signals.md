# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T04:22:27.359570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0857` n `230`; crypto_major avg `0.0065` n `8`; equity avg `-0.0119` n `114`; fx avg `0.0042` n `6`; index avg `-0.0052` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0913` n `791`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `-0.166` n `230`; crypto_major avg `-0.0313` n `8`; equity avg `0.055` n `114`; fx avg `0.0045` n `6`; index avg `0.0058` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0551` n `791`
- 4h: commodity avg `0.0699` n `12`; crypto_alt avg `-0.2954` n `230`; crypto_major avg `0.1121` n `8`; equity avg `0.1316` n `114`; fx avg `0.0002` n `6`; index avg `0.0054` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0734` n `791`
- 24h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.2095` n `230`; crypto_major avg `-0.1233` n `8`; equity avg `0.2293` n `114`; fx avg `-0.0164` n `6`; index avg `0.0104` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.0869` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2213`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
