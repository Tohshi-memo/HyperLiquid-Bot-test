# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T03:22:24.922802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `13`; crypto_alt avg `-0.1436` n `237`; crypto_major avg `-0.0856` n `8`; equity avg `-0.2162` n `151`; fx avg `-0.0126` n `6`; index avg `-0.0575` n `26`; metal avg `-0.0151` n `20`; unknown avg `9.7028` n `1198`
- 1h: commodity avg `0.1165` n `13`; crypto_alt avg `0.381` n `237`; crypto_major avg `0.2959` n `8`; equity avg `-0.065` n `151`; fx avg `0.0231` n `6`; index avg `-0.0461` n `26`; metal avg `0.0551` n `20`; unknown avg `9.7108` n `1196`
- 4h: commodity avg `0.1633` n `13`; crypto_alt avg `0.0297` n `237`; crypto_major avg `-0.1768` n `8`; equity avg `-0.5022` n `151`; fx avg `-0.0016` n `6`; index avg `-0.1215` n `26`; metal avg `0.1095` n `20`; unknown avg `7.7874` n `1190`
- 24h: commodity avg `0.2665` n `13`; crypto_alt avg `0.127` n `237`; crypto_major avg `-0.4027` n `8`; equity avg `-0.8412` n `151`; fx avg `-0.017` n `6`; index avg `-0.1442` n `26`; metal avg `-0.2163` n `20`; unknown avg `5.2693` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
