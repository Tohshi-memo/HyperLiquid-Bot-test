# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T13:22:36.156935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1055` n `12`; crypto_alt avg `-0.0298` n `232`; crypto_major avg `-0.0534` n `8`; equity avg `0.133` n `128`; fx avg `0.0045` n `6`; index avg `0.0141` n `26`; metal avg `0.0258` n `20`; unknown avg `-0.1363` n `794`
- 1h: commodity avg `0.032` n `12`; crypto_alt avg `-0.6158` n `232`; crypto_major avg `-0.4514` n `8`; equity avg `-0.3137` n `128`; fx avg `0.0167` n `6`; index avg `-0.0445` n `26`; metal avg `-0.1053` n `20`; unknown avg `-0.1335` n `792`
- 4h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.5508` n `232`; crypto_major avg `-0.3497` n `8`; equity avg `-0.4573` n `128`; fx avg `0.0326` n `6`; index avg `-0.0844` n `26`; metal avg `-0.0874` n `20`; unknown avg `0.143` n `791`
- 24h: commodity avg `0.541` n `12`; crypto_alt avg `-1.4584` n `231`; crypto_major avg `-1.8161` n `8`; equity avg `-0.6877` n `128`; fx avg `-0.1025` n `6`; index avg `-0.1338` n `26`; metal avg `-0.318` n `20`; unknown avg `-0.1201` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
