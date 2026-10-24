# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T11:22:29.949735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `13`; crypto_alt avg `-0.0575` n `237`; crypto_major avg `-0.0296` n `8`; equity avg `0.0006` n `152`; fx avg `-0.0007` n `6`; index avg `-0.0019` n `26`; metal avg `0.0019` n `20`; unknown avg `0.4566` n `1230`
- 1h: commodity avg `0.0207` n `13`; crypto_alt avg `0.0523` n `237`; crypto_major avg `0.1309` n `8`; equity avg `0.0378` n `152`; fx avg `0.0011` n `6`; index avg `0.0019` n `26`; metal avg `-0.0094` n `20`; unknown avg `0.0612` n `1230`
- 4h: commodity avg `0.0543` n `13`; crypto_alt avg `-0.4418` n `237`; crypto_major avg `-0.639` n `8`; equity avg `-0.1722` n `152`; fx avg `0.0071` n `6`; index avg `-0.028` n `26`; metal avg `-0.039` n `20`; unknown avg `11.9705` n `1194`
- 24h: commodity avg `0.3031` n `13`; crypto_alt avg `-2.5033` n `237`; crypto_major avg `-1.9236` n `8`; equity avg `-0.4695` n `152`; fx avg `-0.0003` n `6`; index avg `0.0021` n `26`; metal avg `-0.2393` n `20`; unknown avg `193.7726` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.2014`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
