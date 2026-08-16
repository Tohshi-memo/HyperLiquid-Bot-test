# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T00:07:29.364935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.0041` n `230`; crypto_major avg `-0.038` n `8`; equity avg `0.0092` n `114`; fx avg `-0.002` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0044` n `791`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.2153` n `230`; crypto_major avg `-0.1612` n `8`; equity avg `0.012` n `114`; fx avg `-0.0037` n `6`; index avg `0.0072` n `25`; metal avg `0.0025` n `20`; unknown avg `0.0757` n `791`
- 4h: commodity avg `-0.0467` n `12`; crypto_alt avg `-0.501` n `230`; crypto_major avg `-0.305` n `8`; equity avg `0.0141` n `114`; fx avg `-0.0023` n `6`; index avg `0.0071` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.3809` n `791`
- 24h: commodity avg `-0.132` n `12`; crypto_alt avg `0.1136` n `230`; crypto_major avg `0.021` n `8`; equity avg `0.2272` n `114`; fx avg `0.0321` n `6`; index avg `0.0143` n `25`; metal avg `-0.0305` n `20`; unknown avg `0.1337` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2214`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
