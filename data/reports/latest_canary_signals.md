# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T17:22:29.221519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1186` n `13`; crypto_alt avg `0.0072` n `239`; crypto_major avg `-0.041` n `8`; equity avg `0.2084` n `158`; fx avg `-0.0044` n `6`; index avg `0.0305` n `27`; metal avg `-0.0011` n `20`; unknown avg `12.408` n `1255`
- 1h: commodity avg `0.0081` n `13`; crypto_alt avg `0.509` n `239`; crypto_major avg `0.5154` n `8`; equity avg `0.7208` n `158`; fx avg `-0.0147` n `6`; index avg `0.0704` n `27`; metal avg `-0.0432` n `20`; unknown avg `72.8956` n `1255`
- 4h: commodity avg `-0.1854` n `13`; crypto_alt avg `0.3302` n `239`; crypto_major avg `0.1753` n `8`; equity avg `-0.4311` n `158`; fx avg `-0.0307` n `6`; index avg `0.0275` n `27`; metal avg `-0.0829` n `20`; unknown avg `72.5501` n `1243`
- 24h: commodity avg `0.1162` n `13`; crypto_alt avg `2.7932` n `239`; crypto_major avg `-0.1813` n `8`; equity avg `1.8571` n `158`; fx avg `-0.1109` n `6`; index avg `0.156` n `27`; metal avg `-0.3184` n `20`; unknown avg `58.1869` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
