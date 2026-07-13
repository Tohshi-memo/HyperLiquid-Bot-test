# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T11:22:29.065435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.0119` n `230`; crypto_major avg `-0.0374` n `8`; equity avg `-0.0457` n `92`; fx avg `-0.0174` n `6`; index avg `-0.0203` n `25`; metal avg `-0.0571` n `20`; unknown avg `0.0178` n `766`
- 1h: commodity avg `0.058` n `12`; crypto_alt avg `0.0963` n `230`; crypto_major avg `0.1163` n `8`; equity avg `0.1005` n `92`; fx avg `0.0244` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0464` n `20`; unknown avg `0.0275` n `766`
- 4h: commodity avg `-0.1211` n `12`; crypto_alt avg `0.3379` n `230`; crypto_major avg `0.0727` n `8`; equity avg `0.4577` n `92`; fx avg `-0.0703` n `6`; index avg `0.0686` n `25`; metal avg `0.0925` n `20`; unknown avg `-0.0678` n `766`
- 24h: commodity avg `-0.2033` n `12`; crypto_alt avg `-0.7042` n `230`; crypto_major avg `-1.0004` n `8`; equity avg `-1.894` n `92`; fx avg `-0.0609` n `6`; index avg `-0.4112` n `25`; metal avg `-0.2568` n `20`; unknown avg `-0.0424` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
