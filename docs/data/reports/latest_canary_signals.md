# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T15:22:28.783678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.0753` n `239`; crypto_major avg `-0.0974` n `8`; equity avg `-0.1059` n `158`; fx avg `0.0049` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0228` n `20`; unknown avg `-0.0543` n `1262`
- 1h: commodity avg `-0.0088` n `13`; crypto_alt avg `0.348` n `239`; crypto_major avg `0.0968` n `8`; equity avg `-0.1259` n `158`; fx avg `0.0047` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0369` n `20`; unknown avg `0.2519` n `1248`
- 4h: commodity avg `-0.0028` n `13`; crypto_alt avg `-0.6379` n `239`; crypto_major avg `-0.2181` n `8`; equity avg `-0.1753` n `158`; fx avg `-0.0055` n `6`; index avg `-0.0273` n `27`; metal avg `-0.0404` n `20`; unknown avg `0.7225` n `1242`
- 24h: commodity avg `0.1001` n `13`; crypto_alt avg `-1.4013` n `239`; crypto_major avg `-0.1827` n `8`; equity avg `0.0687` n `158`; fx avg `0.027` n `6`; index avg `-0.0095` n `27`; metal avg `-0.0682` n `20`; unknown avg `7.5379` n `1091`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
