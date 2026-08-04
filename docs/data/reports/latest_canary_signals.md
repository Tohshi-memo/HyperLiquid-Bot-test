# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T00:37:24.872559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.1073` n `230`; crypto_major avg `-0.1688` n `8`; equity avg `-0.4576` n `107`; fx avg `-0.0334` n `6`; index avg `-0.0915` n `25`; metal avg `-0.013` n `20`; unknown avg `0.1062` n `780`
- 1h: commodity avg `0.1684` n `12`; crypto_alt avg `-0.1522` n `230`; crypto_major avg `-0.2328` n `8`; equity avg `-0.7905` n `107`; fx avg `-0.0216` n `6`; index avg `-0.1358` n `25`; metal avg `0.0492` n `20`; unknown avg `0.1053` n `780`
- 4h: commodity avg `0.1624` n `12`; crypto_alt avg `-0.5074` n `230`; crypto_major avg `-0.8756` n `8`; equity avg `-0.4467` n `107`; fx avg `0.0176` n `6`; index avg `-0.0816` n `25`; metal avg `0.0048` n `20`; unknown avg `0.3617` n `780`
- 24h: commodity avg `0.1093` n `12`; crypto_alt avg `0.1801` n `230`; crypto_major avg `-0.046` n `8`; equity avg `1.2821` n `107`; fx avg `-0.0834` n `6`; index avg `0.1441` n `25`; metal avg `-0.1253` n `20`; unknown avg `0.091` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
