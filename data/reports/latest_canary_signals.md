# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T02:22:23.043281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2432` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.4633` n `230`; crypto_major avg `-0.5651` n `8`; equity avg `0.0116` n `121`; fx avg `0.008` n `6`; index avg `0.0037` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.1553` n `794`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `-1.493` n `230`; crypto_major avg `-1.2363` n `8`; equity avg `0.0273` n `121`; fx avg `0.0162` n `6`; index avg `0.0069` n `25`; metal avg `-0.0052` n `20`; unknown avg `3.466` n `794`
- 4h: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.7609` n `230`; crypto_major avg `-0.0255` n `8`; equity avg `0.2167` n `121`; fx avg `0.0566` n `6`; index avg `0.0325` n `25`; metal avg `0.0118` n `20`; unknown avg `2.5702` n `794`
- 24h: commodity avg `0.0833` n `12`; crypto_alt avg `-4.8604` n `230`; crypto_major avg `-1.2748` n `8`; equity avg `-0.2375` n `121`; fx avg `0.1139` n `6`; index avg `-0.0349` n `25`; metal avg `-0.0286` n `20`; unknown avg `3.672` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
