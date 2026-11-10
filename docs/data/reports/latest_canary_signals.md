# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T21:22:27.899818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.1631` n `239`; crypto_major avg `-0.1263` n `8`; equity avg `-0.1466` n `160`; fx avg `-0.0095` n `6`; index avg `-0.0152` n `27`; metal avg `-0.0006` n `20`; unknown avg `0.3371` n `1262`
- 1h: commodity avg `-0.026` n `13`; crypto_alt avg `-0.1067` n `239`; crypto_major avg `0.0918` n `8`; equity avg `0.3519` n `160`; fx avg `-0.0114` n `6`; index avg `0.0311` n `27`; metal avg `-0.0198` n `20`; unknown avg `1.1727` n `1240`
- 4h: commodity avg `0.2022` n `13`; crypto_alt avg `0.4846` n `239`; crypto_major avg `1.0288` n `8`; equity avg `1.0198` n `160`; fx avg `0.0203` n `6`; index avg `0.1011` n `27`; metal avg `0.1251` n `20`; unknown avg `19.342` n `1232`
- 24h: commodity avg `-0.0011` n `13`; crypto_alt avg `-1.3556` n `239`; crypto_major avg `-2.4426` n `8`; equity avg `-1.1537` n `160`; fx avg `-0.1015` n `6`; index avg `-0.1638` n `27`; metal avg `-0.6314` n `20`; unknown avg `20.3345` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2588`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
