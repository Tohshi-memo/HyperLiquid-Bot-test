# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T10:22:26.096789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0488` n `12`; crypto_alt avg `-0.2495` n `233`; crypto_major avg `-0.2187` n `8`; equity avg `0.073` n `136`; fx avg `-0.0106` n `6`; index avg `0.0155` n `27`; metal avg `0.0345` n `20`; unknown avg `0.1155` n `894`
- 1h: commodity avg `-0.1505` n `12`; crypto_alt avg `0.341` n `233`; crypto_major avg `0.4135` n `8`; equity avg `0.2982` n `136`; fx avg `0.0002` n `6`; index avg `0.0286` n `27`; metal avg `0.0594` n `20`; unknown avg `1.8359` n `892`
- 4h: commodity avg `0.1253` n `12`; crypto_alt avg `-0.491` n `233`; crypto_major avg `0.1513` n `8`; equity avg `-0.6137` n `136`; fx avg `-0.0156` n `6`; index avg `-0.1345` n `27`; metal avg `-0.4021` n `20`; unknown avg `5.3317` n `858`
- 24h: commodity avg `0.6496` n `12`; crypto_alt avg `0.1701` n `233`; crypto_major avg `1.755` n `8`; equity avg `-0.9353` n `136`; fx avg `0.0243` n `6`; index avg `-0.2615` n `27`; metal avg `-0.4975` n `20`; unknown avg `1.1276` n `650`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
