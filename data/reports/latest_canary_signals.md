# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T18:37:17.426753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0718` n `12`; crypto_alt avg `0.0477` n `228`; crypto_major avg `0.0221` n `8`; equity avg `0.0113` n `69`; fx avg `-0.0002` n `6`; index avg `0.0056` n `23`; metal avg `0.0004` n `18`; unknown avg `-0.1963` n `421`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `0.5012` n `228`; crypto_major avg `0.503` n `8`; equity avg `0.048` n `69`; fx avg `-0.0009` n `6`; index avg `0.0463` n `23`; metal avg `0.0108` n `18`; unknown avg `-0.1306` n `421`
- 4h: commodity avg `-0.4327` n `12`; crypto_alt avg `0.1565` n `228`; crypto_major avg `0.5783` n `8`; equity avg `-0.1312` n `69`; fx avg `-0.0178` n `6`; index avg `-0.1447` n `23`; metal avg `0.0278` n `18`; unknown avg `-0.2583` n `421`
- 24h: commodity avg `0.0953` n `12`; crypto_alt avg `1.0707` n `228`; crypto_major avg `2.247` n `8`; equity avg `0.9322` n `69`; fx avg `-0.0064` n `6`; index avg `0.1056` n `23`; metal avg `-0.1677` n `18`; unknown avg `0.1976` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
