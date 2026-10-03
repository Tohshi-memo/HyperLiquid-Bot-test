# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T05:22:26.758591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0044` n `13`; crypto_alt avg `0.0908` n `235`; crypto_major avg `0.1252` n `8`; equity avg `0.0067` n `143`; fx avg `-0.0083` n `6`; index avg `0.0058` n `26`; metal avg `-0.0092` n `20`; unknown avg `-0.1234` n `984`
- 1h: commodity avg `-0.0654` n `13`; crypto_alt avg `0.2887` n `235`; crypto_major avg `0.1396` n `8`; equity avg `0.0106` n `143`; fx avg `-0.0136` n `6`; index avg `-0.0034` n `26`; metal avg `0.0117` n `20`; unknown avg `0.1034` n `982`
- 4h: commodity avg `-0.186` n `13`; crypto_alt avg `0.1581` n `235`; crypto_major avg `-0.1948` n `8`; equity avg `-0.0314` n `143`; fx avg `-0.006` n `6`; index avg `0.0066` n `26`; metal avg `0.0234` n `20`; unknown avg `-0.3242` n `976`
- 24h: commodity avg `0.0222` n `13`; crypto_alt avg `-1.3777` n `235`; crypto_major avg `-1.9158` n `8`; equity avg `0.4261` n `142`; fx avg `-0.0828` n `6`; index avg `0.2365` n `26`; metal avg `-0.3492` n `20`; unknown avg `-0.758` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
