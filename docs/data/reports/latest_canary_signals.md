# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T05:37:24.377625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `13`; crypto_alt avg `0.0667` n `239`; crypto_major avg `0.1061` n `8`; equity avg `0.0841` n `166`; fx avg `-0.0042` n `6`; index avg `0.0022` n `27`; metal avg `0.0846` n `20`; unknown avg `268.9724` n `1264`
- 1h: commodity avg `0.0264` n `13`; crypto_alt avg `0.4506` n `239`; crypto_major avg `0.4948` n `8`; equity avg `0.354` n `166`; fx avg `-0.0244` n `6`; index avg `0.0339` n `27`; metal avg `0.1645` n `20`; unknown avg `10.8145` n `1256`
- 4h: commodity avg `0.0614` n `13`; crypto_alt avg `1.0116` n `239`; crypto_major avg `1.062` n `8`; equity avg `0.6083` n `166`; fx avg `0.0498` n `6`; index avg `-0.0552` n `27`; metal avg `0.1688` n `20`; unknown avg `167.5861` n `1237`
- 24h: commodity avg `-0.2729` n `13`; crypto_alt avg `2.7414` n `239`; crypto_major avg `3.7902` n `8`; equity avg `2.5491` n `166`; fx avg `0.2147` n `6`; index avg `0.2114` n `27`; metal avg `0.5994` n `20`; unknown avg `294.2191` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
