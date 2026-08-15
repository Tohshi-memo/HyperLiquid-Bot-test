# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T14:37:26.889815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.0116` n `230`; crypto_major avg `0.0701` n `8`; equity avg `0.0078` n `114`; fx avg `0.0009` n `6`; index avg `-0.0002` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0051` n `791`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.0378` n `230`; crypto_major avg `-0.0504` n `8`; equity avg `0.0302` n `114`; fx avg `-0.0002` n `6`; index avg `-0.0019` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.008` n `791`
- 4h: commodity avg `0.0503` n `12`; crypto_alt avg `-0.0047` n `230`; crypto_major avg `0.1319` n `8`; equity avg `0.0522` n `114`; fx avg `-0.0049` n `6`; index avg `0.0196` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0383` n `791`
- 24h: commodity avg `-0.0825` n `12`; crypto_alt avg `1.1917` n `230`; crypto_major avg `0.5031` n `8`; equity avg `-0.3746` n `114`; fx avg `0.0862` n `6`; index avg `-0.0608` n `25`; metal avg `-0.0165` n `20`; unknown avg `0.0235` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
