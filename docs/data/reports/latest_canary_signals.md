# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T04:37:36.579572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0038` n `230`; crypto_major avg `-0.0317` n `8`; equity avg `-0.0115` n `114`; fx avg `-0.0025` n `6`; index avg `-0.0091` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0414` n `791`
- 1h: commodity avg `0.0278` n `12`; crypto_alt avg `0.1525` n `230`; crypto_major avg `-0.0116` n `8`; equity avg `0.022` n `114`; fx avg `-0.022` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0728` n `791`
- 4h: commodity avg `-0.0418` n `12`; crypto_alt avg `0.0858` n `230`; crypto_major avg `0.2435` n `8`; equity avg `0.1027` n `114`; fx avg `0.052` n `6`; index avg `0.0013` n `25`; metal avg `-0.0548` n `20`; unknown avg `0.3954` n `791`
- 24h: commodity avg `0.1724` n `12`; crypto_alt avg `0.4967` n `230`; crypto_major avg `-0.2528` n `8`; equity avg `-0.0935` n `114`; fx avg `0.1391` n `6`; index avg `-0.0366` n `25`; metal avg `0.4085` n `20`; unknown avg `-0.0236` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
