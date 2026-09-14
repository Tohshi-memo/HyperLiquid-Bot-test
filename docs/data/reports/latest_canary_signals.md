# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T08:22:32.377101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1088` n `12`; crypto_alt avg `0.0414` n `233`; crypto_major avg `0.0533` n `8`; equity avg `-0.0543` n `136`; fx avg `-0.0165` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0366` n `20`; unknown avg `23.8312` n `894`
- 1h: commodity avg `0.1052` n `12`; crypto_alt avg `-0.1473` n `233`; crypto_major avg `0.0986` n `8`; equity avg `-0.361` n `136`; fx avg `-0.0356` n `6`; index avg `-0.037` n `27`; metal avg `-0.1492` n `20`; unknown avg `8.3056` n `892`
- 4h: commodity avg `0.1114` n `12`; crypto_alt avg `-0.0682` n `233`; crypto_major avg `0.3427` n `8`; equity avg `-0.6908` n `136`; fx avg `-0.0108` n `6`; index avg `-0.0893` n `27`; metal avg `-0.2147` n `20`; unknown avg `0.5859` n `832`
- 24h: commodity avg `0.7693` n `12`; crypto_alt avg `-0.0025` n `233`; crypto_major avg `1.0274` n `8`; equity avg `-1.4551` n `136`; fx avg `0.0268` n `6`; index avg `-0.3106` n `27`; metal avg `-0.3324` n `20`; unknown avg `0.904` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
