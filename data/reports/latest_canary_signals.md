# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T04:37:39.074954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `0.076` n `231`; crypto_major avg `0.0254` n `8`; equity avg `-0.0056` n `127`; fx avg `0.0125` n `6`; index avg `0.0073` n `26`; metal avg `0.0036` n `20`; unknown avg `-0.0184` n `793`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0456` n `231`; crypto_major avg `-0.0073` n `8`; equity avg `0.041` n `127`; fx avg `0.0125` n `6`; index avg `0.0127` n `26`; metal avg `0.0068` n `20`; unknown avg `-0.0638` n `793`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `-0.2154` n `231`; crypto_major avg `-0.013` n `8`; equity avg `0.1118` n `127`; fx avg `0.0149` n `6`; index avg `0.046` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.2724` n `793`
- 24h: commodity avg `-0.1271` n `12`; crypto_alt avg `-1.5142` n `231`; crypto_major avg `-2.1441` n `8`; equity avg `-1.7945` n `127`; fx avg `-0.0741` n `6`; index avg `-0.1731` n `26`; metal avg `-0.2209` n `20`; unknown avg `-0.3156` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
