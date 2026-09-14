# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T07:22:27.424764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.028` n `233`; crypto_major avg `0.0005` n `8`; equity avg `-0.0729` n `136`; fx avg `0.0103` n `6`; index avg `0.0055` n `27`; metal avg `0.0161` n `20`; unknown avg `0.2643` n `894`
- 1h: commodity avg `0.1274` n `12`; crypto_alt avg `-0.1389` n `233`; crypto_major avg `0.0047` n `8`; equity avg `-0.2327` n `136`; fx avg `0.0156` n `6`; index avg `-0.0541` n `27`; metal avg `-0.0591` n `20`; unknown avg `0.0127` n `864`
- 4h: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.0642` n `233`; crypto_major avg `0.1495` n `8`; equity avg `-0.434` n `136`; fx avg `-0.0015` n `6`; index avg `-0.0776` n `27`; metal avg `-0.1051` n `20`; unknown avg `0.2559` n `828`
- 24h: commodity avg `0.6469` n `12`; crypto_alt avg `-0.3205` n `233`; crypto_major avg `0.5274` n `8`; equity avg `-1.3599` n `136`; fx avg `0.0651` n `6`; index avg `-0.302` n `27`; metal avg `-0.2027` n `20`; unknown avg `1.2698` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
