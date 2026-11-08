# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T12:22:25.879751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.2198` n `239`; crypto_major avg `-0.0602` n `8`; equity avg `0.013` n `158`; fx avg `-0.0024` n `6`; index avg `-0.0099` n `27`; metal avg `-0.0013` n `20`; unknown avg `0.708` n `1262`
- 1h: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.3271` n `239`; crypto_major avg `-0.081` n `8`; equity avg `-0.0283` n `158`; fx avg `-0.0045` n `6`; index avg `-0.0177` n `27`; metal avg `0.0041` n `20`; unknown avg `0.5557` n `1250`
- 4h: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.1454` n `239`; crypto_major avg `0.1615` n `8`; equity avg `0.171` n `158`; fx avg `-0.0028` n `6`; index avg `-0.0474` n `27`; metal avg `0.0043` n `20`; unknown avg `219.4176` n `1170`
- 24h: commodity avg `0.0891` n `13`; crypto_alt avg `-1.3413` n `239`; crypto_major avg `-0.2674` n `8`; equity avg `0.2042` n `158`; fx avg `0.0127` n `6`; index avg `0.0236` n `27`; metal avg `-0.0259` n `20`; unknown avg `5.902` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
