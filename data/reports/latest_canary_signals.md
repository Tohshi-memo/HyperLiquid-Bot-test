# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T09:37:53.491580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.049` n `13`; crypto_alt avg `-0.2363` n `239`; crypto_major avg `-0.2613` n `8`; equity avg `-0.3256` n `166`; fx avg `-0.0085` n `6`; index avg `-0.0388` n `27`; metal avg `-0.0373` n `20`; unknown avg `0.3005` n `1264`
- 1h: commodity avg `0.0614` n `13`; crypto_alt avg `0.1688` n `239`; crypto_major avg `0.2504` n `8`; equity avg `0.6226` n `166`; fx avg `-0.0471` n `6`; index avg `0.0627` n `27`; metal avg `0.1315` n `20`; unknown avg `289.4048` n `1198`
- 4h: commodity avg `-0.4356` n `13`; crypto_alt avg `0.3228` n `239`; crypto_major avg `0.1909` n `8`; equity avg `0.9538` n `166`; fx avg `-0.0227` n `6`; index avg `0.0366` n `27`; metal avg `0.0122` n `20`; unknown avg `304.3674` n `1090`
- 24h: commodity avg `-0.7316` n `13`; crypto_alt avg `1.6904` n `239`; crypto_major avg `2.0917` n `8`; equity avg `2.7526` n `166`; fx avg `0.2082` n `6`; index avg `0.169` n `27`; metal avg `0.4794` n `20`; unknown avg `0.4805` n `955`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
