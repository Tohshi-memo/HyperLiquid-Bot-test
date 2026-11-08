# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T11:22:27.557437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0542` n `13`; crypto_alt avg `0.3976` n `239`; crypto_major avg `0.3701` n `8`; equity avg `0.1028` n `158`; fx avg `0.0012` n `6`; index avg `0.0052` n `27`; metal avg `0.0087` n `20`; unknown avg `-0.182` n `1262`
- 1h: commodity avg `0.0224` n `13`; crypto_alt avg `0.4616` n `239`; crypto_major avg `0.4104` n `8`; equity avg `0.0741` n `158`; fx avg `0.008` n `6`; index avg `0.0048` n `27`; metal avg `0.0037` n `20`; unknown avg `-0.1019` n `1256`
- 4h: commodity avg `0.0261` n `13`; crypto_alt avg `0.1295` n `239`; crypto_major avg `0.26` n `8`; equity avg `0.2345` n `158`; fx avg `0.0041` n `6`; index avg `0.004` n `27`; metal avg `0.0081` n `20`; unknown avg `220.9339` n `1160`
- 24h: commodity avg `0.0914` n `13`; crypto_alt avg `-0.8328` n `239`; crypto_major avg `-0.1813` n `8`; equity avg `0.1934` n `158`; fx avg `0.055` n `6`; index avg `0.0395` n `27`; metal avg `-0.0339` n `20`; unknown avg `5.6027` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
