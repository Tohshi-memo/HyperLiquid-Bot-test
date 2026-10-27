# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T01:37:41.467424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0654` n `13`; crypto_alt avg `0.117` n `237`; crypto_major avg `0.1201` n `8`; equity avg `0.1033` n `154`; fx avg `-0.0072` n `6`; index avg `0.0178` n `27`; metal avg `0.091` n `20`; unknown avg `9.0464` n `1238`
- 1h: commodity avg `-0.1343` n `13`; crypto_alt avg `-0.4338` n `237`; crypto_major avg `-0.2158` n `8`; equity avg `-0.0223` n `154`; fx avg `-0.0072` n `6`; index avg `0.0255` n `27`; metal avg `0.0307` n `20`; unknown avg `0.6451` n `1236`
- 4h: commodity avg `-0.1171` n `13`; crypto_alt avg `0.0857` n `237`; crypto_major avg `0.4339` n `8`; equity avg `0.4127` n `154`; fx avg `-0.0041` n `6`; index avg `0.1481` n `27`; metal avg `-0.0061` n `20`; unknown avg `-0.0372` n `1208`
- 24h: commodity avg `-0.0254` n `13`; crypto_alt avg `0.5496` n `237`; crypto_major avg `0.8878` n `8`; equity avg `1.8959` n `153`; fx avg `-0.0489` n `6`; index avg `0.1143` n `27`; metal avg `0.069` n `20`; unknown avg `998.3012` n `1004`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
