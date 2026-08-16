# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T23:37:30.780642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0543` n `230`; crypto_major avg `-0.0469` n `8`; equity avg `-0.0195` n `114`; fx avg `-0.0052` n `6`; index avg `0.0055` n `25`; metal avg `-0.0585` n `20`; unknown avg `-0.0238` n `791`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.1416` n `230`; crypto_major avg `0.115` n `8`; equity avg `-0.0043` n `114`; fx avg `0.0041` n `6`; index avg `0.0002` n `25`; metal avg `-0.0424` n `20`; unknown avg `0.213` n `791`
- 4h: commodity avg `-0.1546` n `12`; crypto_alt avg `-0.8453` n `230`; crypto_major avg `-0.7383` n `8`; equity avg `-0.0295` n `114`; fx avg `-0.0061` n `6`; index avg `0.0105` n `25`; metal avg `-0.0547` n `20`; unknown avg `0.8802` n `791`
- 24h: commodity avg `-0.0719` n `12`; crypto_alt avg `-0.6355` n `230`; crypto_major avg `-0.4546` n `8`; equity avg `0.2426` n `114`; fx avg `-0.0115` n `6`; index avg `0.0466` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0046` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
