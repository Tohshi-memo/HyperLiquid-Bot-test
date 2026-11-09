# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T10:52:33.437467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0736` n `13`; crypto_alt avg `0.0402` n `239`; crypto_major avg `0.1202` n `8`; equity avg `-0.11` n `158`; fx avg `0.0023` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0189` n `20`; unknown avg `0.3798` n `1263`
- 1h: commodity avg `-0.1461` n `13`; crypto_alt avg `-0.277` n `239`; crypto_major avg `-0.3474` n `8`; equity avg `-0.0007` n `158`; fx avg `0.0096` n `6`; index avg `0.0066` n `27`; metal avg `-0.0066` n `20`; unknown avg `0.1714` n `1257`
- 4h: commodity avg `0.0914` n `13`; crypto_alt avg `0.4435` n `239`; crypto_major avg `-0.4244` n `8`; equity avg `0.2985` n `158`; fx avg `0.0768` n `6`; index avg `0.0326` n `27`; metal avg `-0.0673` n `20`; unknown avg `170.7311` n `1129`
- 24h: commodity avg `-0.1611` n `13`; crypto_alt avg `-1.7698` n `239`; crypto_major avg `-3.6065` n `8`; equity avg `-0.4328` n `158`; fx avg `-0.091` n `6`; index avg `-0.0383` n `27`; metal avg `0.2479` n `20`; unknown avg `0.4614` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
