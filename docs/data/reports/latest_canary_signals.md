# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T17:00:30.031084+00:00`
- Correlation status: `ready`
- Asset price records: `282`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6966` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0534` n `7`; crypto_alt avg `-0.0978` n `223`; crypto_major avg `-0.207` n `7`; equity avg `-0.0591` n `42`; fx avg `-0.003` n `4`; index avg `-0.0167` n `9`; metal avg `-0.021` n `7`; unknown avg `-0.0464` n `314`
- 1h: commodity avg `0.3666` n `7`; crypto_alt avg `0.2254` n `223`; crypto_major avg `0.229` n `7`; equity avg `-0.3243` n `42`; fx avg `-0.0311` n `4`; index avg `-0.2044` n `9`; metal avg `-0.2844` n `7`; unknown avg `0.1934` n `314`
- 4h: commodity avg `1.1133` n `7`; crypto_alt avg `0.8203` n `223`; crypto_major avg `0.8468` n `7`; equity avg `-0.1831` n `42`; fx avg `-0.0308` n `4`; index avg `0.1462` n `9`; metal avg `-0.8498` n `7`; unknown avg `-0.6884` n `314`
- 24h: commodity avg `2.3166` n `7`; crypto_alt avg `1.7968` n `223`; crypto_major avg `1.1378` n `7`; equity avg `-0.1165` n `42`; fx avg `-0.1041` n `4`; index avg `0.4801` n `9`; metal avg `-2.441` n `7`; unknown avg `-0.873` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2411`, n `278`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2356`, n `278`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.162`, n `274`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1608`, n `274`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1574`, n `274`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1566`, n `274`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `278`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `278`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `278`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1312`, n `274`, weak_sample_signal
