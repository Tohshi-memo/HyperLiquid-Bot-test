# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T05:07:26.609702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `13`; crypto_alt avg `0.1213` n `239`; crypto_major avg `0.1054` n `8`; equity avg `0.0292` n `158`; fx avg `0.0012` n `6`; index avg `-0.0044` n `27`; metal avg `0.0022` n `20`; unknown avg `-0.0636` n `1258`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `-0.2498` n `239`; crypto_major avg `-0.0818` n `8`; equity avg `-0.041` n `158`; fx avg `-0.001` n `6`; index avg `-0.0114` n `27`; metal avg `-0.0078` n `20`; unknown avg `-0.448` n `1250`
- 4h: commodity avg `0.0103` n `13`; crypto_alt avg `-0.5623` n `239`; crypto_major avg `-0.0551` n `8`; equity avg `-0.0263` n `158`; fx avg `0.0209` n `6`; index avg `-0.0163` n `27`; metal avg `-0.0198` n `20`; unknown avg `-0.3471` n `1240`
- 24h: commodity avg `0.131` n `13`; crypto_alt avg `-1.8198` n `239`; crypto_major avg `-0.465` n `8`; equity avg `-0.1538` n `158`; fx avg `0.0115` n `6`; index avg `0.0243` n `27`; metal avg `-0.0557` n `20`; unknown avg `162.0788` n `1089`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
