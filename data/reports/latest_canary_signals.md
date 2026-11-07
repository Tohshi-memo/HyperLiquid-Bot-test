# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T04:07:26.780602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `0.1982` n `239`; crypto_major avg `0.0555` n `8`; equity avg `-0.0421` n `158`; fx avg `0.008` n `6`; index avg `-0.0072` n `27`; metal avg `0.0017` n `20`; unknown avg `0.2515` n `1251`
- 1h: commodity avg `-0.0951` n `13`; crypto_alt avg `-0.2319` n `239`; crypto_major avg `-0.3547` n `8`; equity avg `0.0294` n `158`; fx avg `0.0144` n `6`; index avg `0.0096` n `27`; metal avg `-0.0091` n `20`; unknown avg `6.2335` n `1243`
- 4h: commodity avg `-0.1404` n `13`; crypto_alt avg `-0.2179` n `239`; crypto_major avg `-0.1604` n `8`; equity avg `0.0292` n `158`; fx avg `0.0111` n `6`; index avg `0.0116` n `27`; metal avg `0.0038` n `20`; unknown avg `3.1766` n `1243`
- 24h: commodity avg `-0.2969` n `13`; crypto_alt avg `0.4768` n `239`; crypto_major avg `0.1064` n `8`; equity avg `1.3723` n `158`; fx avg `-0.0432` n `6`; index avg `0.1982` n `27`; metal avg `0.2705` n `20`; unknown avg `8.2223` n `1018`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
