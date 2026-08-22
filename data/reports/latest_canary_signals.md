# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T12:52:27.200328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.037` n `230`; crypto_major avg `0.0364` n `8`; equity avg `0.0117` n `121`; fx avg `0.0013` n `6`; index avg `-0.0058` n `25`; metal avg `0.0063` n `20`; unknown avg `0.015` n `794`
- 1h: commodity avg `0.0168` n `12`; crypto_alt avg `0.3738` n `230`; crypto_major avg `0.7366` n `8`; equity avg `0.0366` n `121`; fx avg `-0.0073` n `6`; index avg `0.0051` n `25`; metal avg `0.0098` n `20`; unknown avg `0.1126` n `794`
- 4h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.2874` n `230`; crypto_major avg `0.0536` n `8`; equity avg `-0.0399` n `121`; fx avg `0.0191` n `6`; index avg `0.0024` n `25`; metal avg `0.0288` n `20`; unknown avg `0.2382` n `794`
- 24h: commodity avg `-0.0346` n `12`; crypto_alt avg `1.3047` n `230`; crypto_major avg `3.8445` n `8`; equity avg `-1.0156` n `121`; fx avg `0.0625` n `6`; index avg `-0.1365` n `25`; metal avg `-0.1095` n `20`; unknown avg `1.4452` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
