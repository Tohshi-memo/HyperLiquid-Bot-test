# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T08:37:27.614692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `0.0487` n `230`; crypto_major avg `-0.071` n `8`; equity avg `0.0185` n `114`; fx avg `-0.0105` n `6`; index avg `0.0008` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0054` n `791`
- 1h: commodity avg `0.0531` n `12`; crypto_alt avg `0.0544` n `230`; crypto_major avg `-0.0956` n `8`; equity avg `0.0047` n `114`; fx avg `0.0022` n `6`; index avg `-0.0102` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0499` n `791`
- 4h: commodity avg `-0.1395` n `12`; crypto_alt avg `0.1117` n `230`; crypto_major avg `-0.2435` n `8`; equity avg `-0.0308` n `114`; fx avg `-0.0048` n `6`; index avg `-0.0127` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.0776` n `759`
- 24h: commodity avg `-0.1501` n `12`; crypto_alt avg `0.8234` n `230`; crypto_major avg `-0.1188` n `8`; equity avg `-0.4197` n `114`; fx avg `0.174` n `6`; index avg `-0.1056` n `25`; metal avg `0.2152` n `20`; unknown avg `-0.0997` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
