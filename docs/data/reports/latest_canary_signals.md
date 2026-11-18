# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T04:52:25.929301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0762` n `13`; crypto_alt avg `-0.133` n `239`; crypto_major avg `-0.0875` n `8`; equity avg `-0.0922` n `163`; fx avg `0.0011` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0031` n `20`; unknown avg `1.0745` n `1266`
- 1h: commodity avg `-0.0613` n `13`; crypto_alt avg `-0.4936` n `239`; crypto_major avg `-0.2011` n `8`; equity avg `-0.0921` n `163`; fx avg `-0.0006` n `6`; index avg `-0.003` n `27`; metal avg `-0.094` n `20`; unknown avg `5.3419` n `1254`
- 4h: commodity avg `-0.3001` n `13`; crypto_alt avg `-0.7908` n `239`; crypto_major avg `-0.598` n `8`; equity avg `-1.6293` n `163`; fx avg `-0.0213` n `6`; index avg `-0.1558` n `27`; metal avg `-0.3937` n `20`; unknown avg `4.2556` n `1254`
- 24h: commodity avg `0.1616` n `13`; crypto_alt avg `-0.615` n `239`; crypto_major avg `-0.1349` n `8`; equity avg `-0.4471` n `163`; fx avg `-0.0861` n `6`; index avg `-0.0506` n `27`; metal avg `-0.8799` n `20`; unknown avg `262.6696` n `1073`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
