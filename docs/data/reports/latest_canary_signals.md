# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T17:52:25.386539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `13`; crypto_alt avg `0.1053` n `239`; crypto_major avg `0.0965` n `8`; equity avg `0.0226` n `158`; fx avg `-0.0008` n `6`; index avg `-0.0005` n `27`; metal avg `0.0139` n `20`; unknown avg `-0.1621` n `1262`
- 1h: commodity avg `0.0061` n `13`; crypto_alt avg `-0.2091` n `239`; crypto_major avg `-0.0738` n `8`; equity avg `0.0078` n `158`; fx avg `0.0007` n `6`; index avg `0.0073` n `27`; metal avg `0.0144` n `20`; unknown avg `0.2371` n `1224`
- 4h: commodity avg `0.0242` n `13`; crypto_alt avg `-0.4696` n `239`; crypto_major avg `-0.3462` n `8`; equity avg `-0.1466` n `158`; fx avg `0.0453` n `6`; index avg `-0.0035` n `27`; metal avg `-0.0178` n `20`; unknown avg `-0.1068` n `1202`
- 24h: commodity avg `0.0739` n `13`; crypto_alt avg `-2.224` n `239`; crypto_major avg `-0.4756` n `8`; equity avg `0.0562` n `158`; fx avg `0.078` n `6`; index avg `-0.0319` n `27`; metal avg `-0.0328` n `20`; unknown avg `12.1803` n `1054`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
