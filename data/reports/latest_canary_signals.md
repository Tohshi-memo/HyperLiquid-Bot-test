# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T01:07:21.027205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1619` n `12`; crypto_alt avg `-0.3045` n `228`; crypto_major avg `-0.4317` n `8`; equity avg `0.6804` n `69`; fx avg `0.0195` n `6`; index avg `-0.1354` n `23`; metal avg `-0.2603` n `18`; unknown avg `-0.1886` n `421`
- 1h: commodity avg `0.2589` n `12`; crypto_alt avg `0.3216` n `228`; crypto_major avg `0.1741` n `8`; equity avg `0.912` n `69`; fx avg `0.0645` n `6`; index avg `0.0578` n `23`; metal avg `-0.255` n `18`; unknown avg `-0.1601` n `421`
- 4h: commodity avg `0.6648` n `12`; crypto_alt avg `1.4947` n `228`; crypto_major avg `0.6976` n `8`; equity avg `0.6971` n `69`; fx avg `0.0727` n `6`; index avg `0.1434` n `23`; metal avg `0.1654` n `18`; unknown avg `0.5934` n `421`
- 24h: commodity avg `1.014` n `12`; crypto_alt avg `1.124` n `228`; crypto_major avg `0.1047` n `8`; equity avg `1.3183` n `69`; fx avg `0.0403` n `6`; index avg `0.2915` n `23`; metal avg `0.0174` n `18`; unknown avg `2.0524` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2836`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2548`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
