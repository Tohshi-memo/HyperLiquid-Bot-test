# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T10:37:26.516750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1046` n `13`; crypto_alt avg `0.0506` n `235`; crypto_major avg `0.0552` n `8`; equity avg `0.0033` n `143`; fx avg `-0.0007` n `6`; index avg `0.0069` n `26`; metal avg `0.0087` n `20`; unknown avg `-0.0208` n `984`
- 1h: commodity avg `-0.0839` n `13`; crypto_alt avg `0.6688` n `235`; crypto_major avg `0.1155` n `8`; equity avg `0.0258` n `143`; fx avg `-0.0029` n `6`; index avg `-0.0006` n `26`; metal avg `-0.006` n `20`; unknown avg `0.03` n `982`
- 4h: commodity avg `-0.0345` n `13`; crypto_alt avg `0.1504` n `235`; crypto_major avg `-0.0381` n `8`; equity avg `0.0483` n `143`; fx avg `-0.0014` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0007` n `20`; unknown avg `2.1015` n `966`
- 24h: commodity avg `0.6048` n `13`; crypto_alt avg `-1.8593` n `235`; crypto_major avg `-2.3948` n `8`; equity avg `0.1033` n `142`; fx avg `0.025` n `6`; index avg `0.1302` n `26`; metal avg `-0.2508` n `20`; unknown avg `-0.2835` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
