# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T11:40:48.807951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.8` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `-0.14` n `228`; crypto_major avg `0.0825` n `8`; equity avg `0.1051` n `69`; fx avg `0.0002` n `6`; index avg `0.0464` n `23`; metal avg `0.0575` n `18`; unknown avg `-0.1564` n `422`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `0.1253` n `228`; crypto_major avg `0.2804` n `8`; equity avg `0.2231` n `69`; fx avg `0.0167` n `6`; index avg `-0.0396` n `23`; metal avg `0.0552` n `18`; unknown avg `0.2397` n `422`
- 4h: commodity avg `-0.2412` n `12`; crypto_alt avg `-0.2203` n `228`; crypto_major avg `-0.4773` n `8`; equity avg `0.2137` n `69`; fx avg `-0.0102` n `6`; index avg `0.1235` n `23`; metal avg `-0.2897` n `18`; unknown avg `-0.3649` n `422`
- 24h: commodity avg `-0.8054` n `12`; crypto_alt avg `-0.26` n `228`; crypto_major avg `-1.9486` n `8`; equity avg `0.7312` n `69`; fx avg `0.1432` n `6`; index avg `0.0321` n `23`; metal avg `0.6539` n `18`; unknown avg `0.0425` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
