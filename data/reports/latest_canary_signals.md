# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T05:22:26.474976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0234` n `239`; crypto_major avg `-0.0092` n `8`; equity avg `0.0233` n `158`; fx avg `-0.0005` n `6`; index avg `0.005` n `27`; metal avg `0.0041` n `20`; unknown avg `18.4556` n `1262`
- 1h: commodity avg `-0.027` n `13`; crypto_alt avg `-0.1259` n `239`; crypto_major avg `-0.0388` n `8`; equity avg `0.0197` n `158`; fx avg `0.0` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0032` n `20`; unknown avg `0.2959` n `1254`
- 4h: commodity avg `0.0057` n `13`; crypto_alt avg `-0.3298` n `239`; crypto_major avg `-0.0214` n `8`; equity avg `0.0038` n `158`; fx avg `0.0196` n `6`; index avg `-0.009` n `27`; metal avg `-0.0176` n `20`; unknown avg `-0.2454` n `1240`
- 24h: commodity avg `0.1664` n `13`; crypto_alt avg `-1.8065` n `239`; crypto_major avg `-0.5165` n `8`; equity avg `-0.0947` n `158`; fx avg `0.0144` n `6`; index avg `0.0328` n `27`; metal avg `-0.0532` n `20`; unknown avg `162.174` n `1089`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
