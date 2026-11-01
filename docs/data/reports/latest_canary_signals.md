# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T04:22:29.511498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.1577` n `238`; crypto_major avg `0.1339` n `8`; equity avg `0.0443` n `156`; fx avg `-0.0006` n `6`; index avg `0.0047` n `27`; metal avg `-0.0026` n `20`; unknown avg `0.3638` n `1262`
- 1h: commodity avg `0.035` n `13`; crypto_alt avg `0.1463` n `238`; crypto_major avg `0.0038` n `8`; equity avg `0.0716` n `156`; fx avg `-0.0022` n `6`; index avg `0.003` n `27`; metal avg `0.002` n `20`; unknown avg `1.3309` n `1246`
- 4h: commodity avg `-0.0038` n `13`; crypto_alt avg `0.3083` n `238`; crypto_major avg `0.13` n `8`; equity avg `0.1634` n `156`; fx avg `0.0035` n `6`; index avg `-0.0034` n `27`; metal avg `0.0067` n `20`; unknown avg `2.4345` n `1226`
- 24h: commodity avg `-0.03` n `13`; crypto_alt avg `0.0482` n `238`; crypto_major avg `-0.0008` n `8`; equity avg `0.1302` n `156`; fx avg `0.0008` n `6`; index avg `-0.0124` n `27`; metal avg `0.0577` n `20`; unknown avg `2.9645` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
