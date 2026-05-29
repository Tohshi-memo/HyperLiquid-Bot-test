# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T03:07:17.982013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1013` n `12`; crypto_alt avg `0.1707` n `228`; crypto_major avg `0.2859` n `8`; equity avg `0.1195` n `69`; fx avg `0.0031` n `6`; index avg `0.0062` n `23`; metal avg `-0.1141` n `18`; unknown avg `0.415` n `417`
- 1h: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.5216` n `228`; crypto_major avg `-0.2461` n `8`; equity avg `0.0232` n `69`; fx avg `-0.0009` n `6`; index avg `0.0095` n `23`; metal avg `-0.1565` n `18`; unknown avg `-0.2241` n `417`
- 4h: commodity avg `-0.3361` n `12`; crypto_alt avg `0.0232` n `228`; crypto_major avg `-0.3231` n `8`; equity avg `-0.0193` n `69`; fx avg `0.068` n `6`; index avg `-0.0869` n `23`; metal avg `-0.0019` n `18`; unknown avg `-0.2552` n `417`
- 24h: commodity avg `0.0486` n `12`; crypto_alt avg `-1.5431` n `228`; crypto_major avg `0.1592` n `8`; equity avg `2.956` n `69`; fx avg `0.0561` n `6`; index avg `0.9817` n `23`; metal avg `1.6914` n `18`; unknown avg `0.2662` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
