# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T09:37:27.716428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1273` n `12`; crypto_alt avg `0.0785` n `233`; crypto_major avg `0.0986` n `8`; equity avg `0.0889` n `136`; fx avg `0.0086` n `6`; index avg `-0.0001` n `27`; metal avg `0.0094` n `20`; unknown avg `1.5649` n `894`
- 1h: commodity avg `-0.0549` n `12`; crypto_alt avg `-0.3614` n `233`; crypto_major avg `-0.1353` n `8`; equity avg `-0.3011` n `136`; fx avg `0.0051` n `6`; index avg `-0.0708` n `27`; metal avg `-0.2545` n `20`; unknown avg `4.6449` n `892`
- 4h: commodity avg `0.1349` n `12`; crypto_alt avg `-0.4648` n `233`; crypto_major avg `0.0526` n `8`; equity avg `-0.8088` n `136`; fx avg `-0.0053` n `6`; index avg `-0.1524` n `27`; metal avg `-0.4756` n `20`; unknown avg `5.362` n `832`
- 24h: commodity avg `0.6698` n `12`; crypto_alt avg `-0.0704` n `233`; crypto_major avg `1.4271` n `8`; equity avg `-1.1845` n `136`; fx avg `0.032` n `6`; index avg `-0.2915` n `27`; metal avg `-0.5525` n `20`; unknown avg `0.923` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
