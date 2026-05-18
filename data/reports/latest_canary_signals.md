# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T11:22:17.612015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.11` n `12`; crypto_alt avg `0.0967` n `228`; crypto_major avg `0.0597` n `8`; equity avg `-0.0134` n `66`; fx avg `0.0035` n `5`; index avg `-0.1238` n `23`; metal avg `0.0062` n `18`; unknown avg `-0.1301` n `383`
- 1h: commodity avg `0.0104` n `12`; crypto_alt avg `0.1853` n `228`; crypto_major avg `-0.0176` n `8`; equity avg `-0.2952` n `66`; fx avg `0.0083` n `5`; index avg `-0.2003` n `23`; metal avg `-0.0702` n `18`; unknown avg `-0.0991` n `383`
- 4h: commodity avg `0.0829` n `12`; crypto_alt avg `-0.0754` n `228`; crypto_major avg `-0.0229` n `8`; equity avg `0.1012` n `66`; fx avg `0.0248` n `5`; index avg `-0.0025` n `23`; metal avg `0.0375` n `18`; unknown avg `-0.3036` n `383`
- 24h: commodity avg `0.8498` n `12`; crypto_alt avg `-3.1543` n `228`; crypto_major avg `-1.9533` n `8`; equity avg `-0.2781` n `65`; fx avg `0.0905` n `5`; index avg `-0.1102` n `23`; metal avg `-0.1128` n `18`; unknown avg `-0.7399` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
