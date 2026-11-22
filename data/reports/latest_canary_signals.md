# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T17:37:29.299261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `13`; crypto_alt avg `0.087` n `239`; crypto_major avg `0.1766` n `8`; equity avg `0.0364` n `166`; fx avg `0.0` n `6`; index avg `0.0036` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.5801` n `1263`
- 1h: commodity avg `-0.0031` n `13`; crypto_alt avg `-0.0678` n `239`; crypto_major avg `-0.1627` n `8`; equity avg `0.1455` n `166`; fx avg `0.0013` n `6`; index avg `0.012` n `27`; metal avg `0.0043` n `20`; unknown avg `163.862` n `1253`
- 4h: commodity avg `-0.0277` n `13`; crypto_alt avg `0.1295` n `239`; crypto_major avg `0.3939` n `8`; equity avg `0.0754` n `166`; fx avg `0.0105` n `6`; index avg `0.004` n `27`; metal avg `0.0706` n `20`; unknown avg `162.558` n `1231`
- 24h: commodity avg `-0.0443` n `13`; crypto_alt avg `0.917` n `239`; crypto_major avg `1.0666` n `8`; equity avg `1.0818` n `166`; fx avg `0.0084` n `6`; index avg `0.1723` n `27`; metal avg `0.0721` n `20`; unknown avg `187.6335` n `1066`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
