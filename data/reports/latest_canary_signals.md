# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T13:37:32.686527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0876` n `13`; crypto_alt avg `0.3555` n `234`; crypto_major avg `0.3399` n `8`; equity avg `-0.0463` n `142`; fx avg `-0.0074` n `6`; index avg `0.0044` n `26`; metal avg `-0.0862` n `20`; unknown avg `118.206` n `975`
- 1h: commodity avg `0.0867` n `13`; crypto_alt avg `-0.2095` n `234`; crypto_major avg `-0.2263` n `8`; equity avg `-0.2184` n `142`; fx avg `-0.015` n `6`; index avg `-0.0593` n `26`; metal avg `-0.2048` n `20`; unknown avg `4.4137` n `973`
- 4h: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.698` n `234`; crypto_major avg `-0.0667` n `8`; equity avg `-0.2953` n `142`; fx avg `-0.0606` n `6`; index avg `-0.0083` n `26`; metal avg `0.0791` n `20`; unknown avg `2.2557` n `967`
- 24h: commodity avg `-0.1928` n `13`; crypto_alt avg `-1.3447` n `234`; crypto_major avg `-0.5309` n `8`; equity avg `-0.0071` n `142`; fx avg `0.0364` n `6`; index avg `0.0504` n `26`; metal avg `-0.2203` n `20`; unknown avg `772.1335` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
