# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T21:37:30.253032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.0474` n `230`; crypto_major avg `0.0089` n `8`; equity avg `0.0236` n `114`; fx avg `-0.0069` n `6`; index avg `0.0079` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0445` n `791`
- 1h: commodity avg `0.007` n `12`; crypto_alt avg `0.0401` n `230`; crypto_major avg `-0.0168` n `8`; equity avg `0.022` n `114`; fx avg `-0.0229` n `6`; index avg `0.014` n `25`; metal avg `0.0204` n `20`; unknown avg `-0.1762` n `791`
- 4h: commodity avg `-0.0935` n `12`; crypto_alt avg `-0.1805` n `230`; crypto_major avg `-0.3046` n `8`; equity avg `0.1119` n `114`; fx avg `0.0047` n `6`; index avg `0.0481` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.3522` n `791`
- 24h: commodity avg `0.1561` n `12`; crypto_alt avg `0.1325` n `230`; crypto_major avg `-1.0142` n `8`; equity avg `-0.5341` n `114`; fx avg `0.0686` n `6`; index avg `-0.0762` n `25`; metal avg `0.2259` n `20`; unknown avg `-0.0625` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
