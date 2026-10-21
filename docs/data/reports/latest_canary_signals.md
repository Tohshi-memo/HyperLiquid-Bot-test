# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T00:35:03.067115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `13`; crypto_alt avg `0.1303` n `237`; crypto_major avg `0.0851` n `8`; equity avg `0.182` n `151`; fx avg `0.0024` n `6`; index avg `0.0296` n `26`; metal avg `0.0131` n `20`; unknown avg `-0.1966` n `1199`
- 1h: commodity avg `0.015` n `13`; crypto_alt avg `0.4089` n `237`; crypto_major avg `0.4006` n `8`; equity avg `0.6028` n `151`; fx avg `-0.0091` n `6`; index avg `0.077` n `26`; metal avg `0.0506` n `20`; unknown avg `-0.21` n `1191`
- 4h: commodity avg `0.0997` n `13`; crypto_alt avg `0.398` n `237`; crypto_major avg `0.3672` n `8`; equity avg `1.532` n `151`; fx avg `-0.0224` n `6`; index avg `0.1832` n `26`; metal avg `0.0233` n `20`; unknown avg `0.6994` n `1079`
- 24h: commodity avg `-0.0057` n `13`; crypto_alt avg `3.0001` n `237`; crypto_major avg `2.2108` n `8`; equity avg `2.5341` n `151`; fx avg `0.0293` n `6`; index avg `0.3264` n `26`; metal avg `0.1233` n `20`; unknown avg `211.8423` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
