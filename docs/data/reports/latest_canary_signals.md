# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T19:37:30.036440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `0.1742` n `230`; crypto_major avg `0.2146` n `8`; equity avg `0.0187` n `121`; fx avg `0.0025` n `6`; index avg `0.0005` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0182` n `794`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.1665` n `230`; crypto_major avg `0.0233` n `8`; equity avg `0.0398` n `121`; fx avg `0.0102` n `6`; index avg `-0.0052` n `25`; metal avg `0.0011` n `20`; unknown avg `0.2083` n `794`
- 4h: commodity avg `0.0473` n `12`; crypto_alt avg `0.9191` n `230`; crypto_major avg `1.4474` n `8`; equity avg `0.1259` n `121`; fx avg `0.0302` n `6`; index avg `-0.0058` n `25`; metal avg `0.0069` n `20`; unknown avg `1.2637` n `794`
- 24h: commodity avg `0.0149` n `12`; crypto_alt avg `1.7784` n `230`; crypto_major avg `4.2119` n `8`; equity avg `-0.3855` n `121`; fx avg `0.057` n `6`; index avg `-0.0498` n `25`; metal avg `-0.0935` n `20`; unknown avg `1.9977` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
