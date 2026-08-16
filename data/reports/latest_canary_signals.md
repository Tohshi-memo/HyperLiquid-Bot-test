# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T04:52:26.224108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0446` n `12`; crypto_alt avg `0.0722` n `230`; crypto_major avg `0.047` n `8`; equity avg `0.0179` n `114`; fx avg `-0.0041` n `6`; index avg `0.0036` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0192` n `791`
- 1h: commodity avg `-0.0201` n `12`; crypto_alt avg `-0.0679` n `230`; crypto_major avg `-0.0073` n `8`; equity avg `0.0047` n `114`; fx avg `0.0033` n `6`; index avg `0.0001` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0565` n `791`
- 4h: commodity avg `0.0326` n `12`; crypto_alt avg `-0.1925` n `230`; crypto_major avg `0.1034` n `8`; equity avg `0.1717` n `114`; fx avg `0.0028` n `6`; index avg `0.0114` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0199` n `791`
- 24h: commodity avg `-0.0755` n `12`; crypto_alt avg `-0.1257` n `230`; crypto_major avg `-0.0727` n `8`; equity avg `0.254` n `114`; fx avg `-0.0159` n `6`; index avg `0.0297` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0723` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2217`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
