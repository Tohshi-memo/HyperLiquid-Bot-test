# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T17:22:27.538423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `0.1473` n `239`; crypto_major avg `0.1102` n `8`; equity avg `-0.0228` n `166`; fx avg `-0.0001` n `6`; index avg `0.0054` n `27`; metal avg `0.0076` n `20`; unknown avg `-0.0169` n `1260`
- 1h: commodity avg `0.0272` n `13`; crypto_alt avg `0.2424` n `239`; crypto_major avg `0.4719` n `8`; equity avg `0.048` n `166`; fx avg `0.013` n `6`; index avg `0.0157` n `27`; metal avg `0.052` n `20`; unknown avg `368.5782` n `1258`
- 4h: commodity avg `0.0035` n `13`; crypto_alt avg `1.1414` n `239`; crypto_major avg `1.412` n `8`; equity avg `0.5272` n `166`; fx avg `0.0087` n `6`; index avg `0.0498` n `27`; metal avg `0.0771` n `20`; unknown avg `-0.5506` n `1248`
- 24h: commodity avg `0.4166` n `13`; crypto_alt avg `1.5319` n `239`; crypto_major avg `1.8364` n `8`; equity avg `0.466` n `166`; fx avg `-0.1276` n `6`; index avg `0.0103` n `27`; metal avg `0.2301` n `20`; unknown avg `570.6618` n `1142`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
