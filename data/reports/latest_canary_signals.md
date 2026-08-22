# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T17:52:28.310182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.3844` n `230`; crypto_major avg `0.4638` n `8`; equity avg `0.034` n `121`; fx avg `0.0029` n `6`; index avg `0.0024` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.3803` n `794`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `0.4` n `230`; crypto_major avg `0.4653` n `8`; equity avg `0.0537` n `121`; fx avg `-0.0038` n `6`; index avg `-0.0039` n `25`; metal avg `0.0024` n `20`; unknown avg `0.4233` n `794`
- 4h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.3886` n `230`; crypto_major avg `0.3339` n `8`; equity avg `-0.0155` n `121`; fx avg `0.0002` n `6`; index avg `-0.0014` n `25`; metal avg `0.0145` n `20`; unknown avg `0.5593` n `794`
- 24h: commodity avg `-0.1305` n `12`; crypto_alt avg `1.2174` n `230`; crypto_major avg `3.5763` n `8`; equity avg `-0.4809` n `121`; fx avg `0.0442` n `6`; index avg `-0.0544` n `25`; metal avg `-0.0984` n `20`; unknown avg `2.2683` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
