# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T23:37:23.825583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0013` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.2626` n `230`; crypto_major avg `-0.1483` n `8`; equity avg `0.0443` n `121`; fx avg `0.0048` n `6`; index avg `0.0082` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0316` n `794`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.3273` n `230`; crypto_major avg `-0.4139` n `8`; equity avg `0.0693` n `121`; fx avg `0.0228` n `6`; index avg `0.0183` n `25`; metal avg `-0.0124` n `20`; unknown avg `0.0859` n `794`
- 4h: commodity avg `0.0845` n `12`; crypto_alt avg `-1.3778` n `230`; crypto_major avg `-0.9873` n `8`; equity avg `0.1056` n `121`; fx avg `0.0461` n `6`; index avg `0.014` n `25`; metal avg `0.0006` n `20`; unknown avg `0.2194` n `794`
- 24h: commodity avg `0.055` n `12`; crypto_alt avg `-2.3452` n `230`; crypto_major avg `-0.2787` n `8`; equity avg `-0.3598` n `121`; fx avg `0.113` n `6`; index avg `-0.0524` n `25`; metal avg `-0.0716` n `20`; unknown avg `2.9914` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
