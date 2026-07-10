# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T23:37:25.325929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0084` n `229`; crypto_major avg `-0.045` n `8`; equity avg `-0.008` n `92`; fx avg `-0.0021` n `6`; index avg `0.0009` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.025` n `765`
- 1h: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.0308` n `229`; crypto_major avg `0.0047` n `8`; equity avg `0.0264` n `92`; fx avg `0.0269` n `6`; index avg `-0.0134` n `25`; metal avg `0.0079` n `20`; unknown avg `0.2256` n `765`
- 4h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.2677` n `229`; crypto_major avg `-0.0244` n `8`; equity avg `-0.0687` n `92`; fx avg `-0.0068` n `6`; index avg `-0.002` n `25`; metal avg `0.1003` n `20`; unknown avg `-0.5265` n `765`
- 24h: commodity avg `-0.256` n `12`; crypto_alt avg `1.2603` n `229`; crypto_major avg `1.1447` n `8`; equity avg `-0.7789` n `92`; fx avg `-0.1779` n `6`; index avg `0.0115` n `25`; metal avg `0.1448` n `20`; unknown avg `-0.2185` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
