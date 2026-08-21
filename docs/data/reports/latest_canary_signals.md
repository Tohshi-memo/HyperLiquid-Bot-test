# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T06:07:32.165697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `0.3431` n `230`; crypto_major avg `0.3377` n `8`; equity avg `0.028` n `121`; fx avg `0.0267` n `6`; index avg `0.0159` n `25`; metal avg `-0.0299` n `20`; unknown avg `0.0253` n `777`
- 1h: commodity avg `0.0451` n `12`; crypto_alt avg `0.7742` n `230`; crypto_major avg `0.7489` n `8`; equity avg `-0.067` n `121`; fx avg `0.0433` n `6`; index avg `-0.0075` n `25`; metal avg `0.0272` n `20`; unknown avg `0.0281` n `777`
- 4h: commodity avg `-0.1058` n `12`; crypto_alt avg `1.2371` n `230`; crypto_major avg `0.8512` n `8`; equity avg `-0.0577` n `121`; fx avg `0.0549` n `6`; index avg `0.0208` n `25`; metal avg `0.1108` n `20`; unknown avg `0.0622` n `777`
- 24h: commodity avg `0.273` n `12`; crypto_alt avg `6.7607` n `230`; crypto_major avg `7.7548` n `8`; equity avg `-0.5369` n `121`; fx avg `-0.0044` n `6`; index avg `-0.103` n `25`; metal avg `0.5519` n `20`; unknown avg `2.7725` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
