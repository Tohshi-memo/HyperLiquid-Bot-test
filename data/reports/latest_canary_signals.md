# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T13:07:25.808238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1248` n `13`; crypto_alt avg `-0.2456` n `239`; crypto_major avg `-0.1996` n `8`; equity avg `-0.0382` n `165`; fx avg `0.0117` n `6`; index avg `-0.0116` n `27`; metal avg `0.0072` n `20`; unknown avg `159.5026` n `1252`
- 1h: commodity avg `-0.0162` n `13`; crypto_alt avg `0.1179` n `239`; crypto_major avg `0.3017` n `8`; equity avg `0.0615` n `165`; fx avg `0.0542` n `6`; index avg `-0.0198` n `27`; metal avg `0.0435` n `20`; unknown avg `161.6002` n `1258`
- 4h: commodity avg `0.2103` n `13`; crypto_alt avg `-1.163` n `239`; crypto_major avg `-0.9556` n `8`; equity avg `-1.0003` n `165`; fx avg `0.0831` n `6`; index avg `-0.1368` n `27`; metal avg `0.0406` n `20`; unknown avg `8.0022` n `1246`
- 24h: commodity avg `-0.3906` n `13`; crypto_alt avg `-4.684` n `239`; crypto_major avg `-4.3546` n `8`; equity avg `-8.5201` n `165`; fx avg `-0.0224` n `6`; index avg `-0.871` n `27`; metal avg `-1.2799` n `20`; unknown avg `25.4884` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
