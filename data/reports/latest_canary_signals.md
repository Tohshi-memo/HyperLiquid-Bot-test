# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T06:52:26.202247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.4923` n `230`; crypto_major avg `0.0175` n `8`; equity avg `0.1235` n `121`; fx avg `0.0024` n `6`; index avg `0.0077` n `25`; metal avg `0.0147` n `20`; unknown avg `0.0868` n `794`
- 1h: commodity avg `-0.0178` n `12`; crypto_alt avg `0.3494` n `230`; crypto_major avg `0.3762` n `8`; equity avg `0.0804` n `121`; fx avg `-0.0011` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0477` n `20`; unknown avg `-0.162` n `778`
- 4h: commodity avg `0.0665` n `12`; crypto_alt avg `-2.3697` n `230`; crypto_major avg `-1.0211` n `8`; equity avg `-0.3282` n `121`; fx avg `0.017` n `6`; index avg `-0.0383` n `25`; metal avg `-0.1113` n `20`; unknown avg `0.0729` n `777`
- 24h: commodity avg `0.1381` n `12`; crypto_alt avg `6.6792` n `230`; crypto_major avg `7.0485` n `8`; equity avg `-0.2855` n `121`; fx avg `0.0114` n `6`; index avg `-0.0758` n `25`; metal avg `-0.0194` n `20`; unknown avg `1.4219` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
