# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T16:22:27.801158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `13`; crypto_alt avg `0.2313` n `239`; crypto_major avg `0.3427` n `8`; equity avg `0.0668` n `166`; fx avg `0.0002` n `6`; index avg `0.0034` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.076` n `1259`
- 1h: commodity avg `0.0043` n `13`; crypto_alt avg `0.4789` n `239`; crypto_major avg `0.4549` n `8`; equity avg `-0.0021` n `166`; fx avg `0.0149` n `6`; index avg `-0.0006` n `27`; metal avg `0.0356` n `20`; unknown avg `161.1381` n `1245`
- 4h: commodity avg `-0.0279` n `13`; crypto_alt avg `0.3511` n `239`; crypto_major avg `0.4401` n `8`; equity avg `-0.0508` n `166`; fx avg `0.0195` n `6`; index avg `0.048` n `27`; metal avg `0.0208` n `20`; unknown avg `152.3773` n `1239`
- 24h: commodity avg `-0.0019` n `13`; crypto_alt avg `1.2853` n `239`; crypto_major avg `1.6746` n `8`; equity avg `0.9773` n `166`; fx avg `0.0145` n `6`; index avg `0.1691` n `27`; metal avg `0.108` n `20`; unknown avg `0.8854` n `1072`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
