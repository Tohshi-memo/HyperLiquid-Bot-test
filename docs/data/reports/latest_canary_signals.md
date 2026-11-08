# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T15:37:24.041623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0306` n `239`; crypto_major avg `0.1099` n `8`; equity avg `0.0013` n `158`; fx avg `0.0012` n `6`; index avg `-0.0009` n `27`; metal avg `-0.0001` n `20`; unknown avg `3.3648` n `1262`
- 1h: commodity avg `0.046` n `13`; crypto_alt avg `0.145` n `239`; crypto_major avg `0.0064` n `8`; equity avg `-0.1716` n `158`; fx avg `0.0069` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0326` n `20`; unknown avg `1.4163` n `1254`
- 4h: commodity avg `0.0019` n `13`; crypto_alt avg `-0.4107` n `239`; crypto_major avg `0.0087` n `8`; equity avg `-0.1765` n `158`; fx avg `-0.0069` n `6`; index avg `-0.0298` n `27`; metal avg `-0.0407` n `20`; unknown avg `0.6377` n `1242`
- 24h: commodity avg `0.1001` n `13`; crypto_alt avg `-1.2096` n `239`; crypto_major avg `0.081` n `8`; equity avg `0.1876` n `158`; fx avg `0.0399` n `6`; index avg `-0.0211` n `27`; metal avg `-0.0644` n `20`; unknown avg `7.5811` n `1091`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
