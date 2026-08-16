# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T04:47:39.539188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0503` n `12`; crypto_alt avg `0.0599` n `230`; crypto_major avg `0.0296` n `8`; equity avg `-0.0153` n `114`; fx avg `0.0004` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0461` n `791`
- 1h: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.08` n `230`; crypto_major avg `-0.0247` n `8`; equity avg `-0.0285` n `114`; fx avg `0.0078` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0411` n `791`
- 4h: commodity avg `0.0268` n `12`; crypto_alt avg `-0.2019` n `230`; crypto_major avg `0.0861` n `8`; equity avg `0.1383` n `114`; fx avg `0.0073` n `6`; index avg `0.0047` n `25`; metal avg `0.0129` n `20`; unknown avg `-0.0357` n `791`
- 24h: commodity avg `-0.0813` n `12`; crypto_alt avg `-0.1313` n `230`; crypto_major avg `-0.0902` n `8`; equity avg `0.2206` n `114`; fx avg `-0.0113` n `6`; index avg `0.0229` n `25`; metal avg `0.01` n `20`; unknown avg `-0.1143` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
