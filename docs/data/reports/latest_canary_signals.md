# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T18:22:30.995477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.2134` n `237`; crypto_major avg `-0.0911` n `8`; equity avg `-0.1847` n `154`; fx avg `-0.0044` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0098` n `20`; unknown avg `0.0993` n `1238`
- 1h: commodity avg `-0.1136` n `13`; crypto_alt avg `-0.4289` n `237`; crypto_major avg `-0.0888` n `8`; equity avg `-0.1426` n `154`; fx avg `-0.0102` n `6`; index avg `-0.0341` n `27`; metal avg `-0.0689` n `20`; unknown avg `-0.0434` n `1238`
- 4h: commodity avg `0.1239` n `13`; crypto_alt avg `0.6195` n `237`; crypto_major avg `0.9481` n `8`; equity avg `1.9393` n `154`; fx avg `0.02` n `6`; index avg `0.2292` n `27`; metal avg `0.1843` n `20`; unknown avg `633.5599` n `1166`
- 24h: commodity avg `-0.2085` n `13`; crypto_alt avg `-0.4415` n `237`; crypto_major avg `0.1104` n `8`; equity avg `0.7901` n `153`; fx avg `0.0436` n `6`; index avg `-0.0609` n `27`; metal avg `0.0825` n `20`; unknown avg `779.6048` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
