# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T19:07:34.153041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0259` n `12`; crypto_alt avg `-0.1318` n `230`; crypto_major avg `-0.1118` n `8`; equity avg `-0.0793` n `92`; fx avg `-0.0029` n `6`; index avg `0.0014` n `25`; metal avg `-0.028` n `20`; unknown avg `-0.068` n `766`
- 1h: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.0474` n `230`; crypto_major avg `0.0925` n `8`; equity avg `-0.1906` n `92`; fx avg `-0.0029` n `6`; index avg `0.0023` n `25`; metal avg `0.0377` n `20`; unknown avg `-0.0197` n `766`
- 4h: commodity avg `0.6771` n `12`; crypto_alt avg `-1.4553` n `230`; crypto_major avg `-1.098` n `8`; equity avg `-1.2691` n `92`; fx avg `-0.0143` n `6`; index avg `-0.1963` n `25`; metal avg `-0.1915` n `20`; unknown avg `-0.065` n `766`
- 24h: commodity avg `0.661` n `12`; crypto_alt avg `-2.4398` n `230`; crypto_major avg `-3.24` n `8`; equity avg `-3.2762` n `92`; fx avg `-0.1006` n `6`; index avg `-0.5995` n `25`; metal avg `-0.5502` n `20`; unknown avg `-0.2704` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
