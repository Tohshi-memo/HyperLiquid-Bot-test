# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T09:52:31.360860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.5796` n `233`; crypto_major avg `0.5959` n `8`; equity avg `0.1369` n `136`; fx avg `-0.0139` n `6`; index avg `0.0092` n `27`; metal avg `-0.006` n `20`; unknown avg `0.5443` n `894`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `0.2891` n `233`; crypto_major avg `0.5504` n `8`; equity avg `-0.1077` n `136`; fx avg `-0.0119` n `6`; index avg `-0.0488` n `27`; metal avg `-0.2088` n `20`; unknown avg `5.5987` n `892`
- 4h: commodity avg `0.0967` n `12`; crypto_alt avg `0.2199` n `233`; crypto_major avg `0.7586` n `8`; equity avg `-0.5891` n `136`; fx avg `-0.0288` n `6`; index avg `-0.1269` n `27`; metal avg `-0.4246` n `20`; unknown avg `5.2103` n `832`
- 24h: commodity avg `0.6744` n `12`; crypto_alt avg `0.4746` n `233`; crypto_major avg `1.9732` n `8`; equity avg `-1.0643` n `136`; fx avg `0.0187` n `6`; index avg `-0.2904` n `27`; metal avg `-0.5615` n `20`; unknown avg `0.9228` n `650`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
