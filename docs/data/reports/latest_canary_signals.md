# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T13:52:27.063690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.3408` n `230`; crypto_major avg `0.4655` n `8`; equity avg `0.0234` n `121`; fx avg `0.0028` n `6`; index avg `0.0012` n `25`; metal avg `-0.0087` n `20`; unknown avg `0.1013` n `794`
- 1h: commodity avg `-0.0461` n `12`; crypto_alt avg `0.0184` n `230`; crypto_major avg `0.0239` n `8`; equity avg `0.0001` n `121`; fx avg `-0.0034` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.0429` n `794`
- 4h: commodity avg `-0.0422` n `12`; crypto_alt avg `0.1407` n `230`; crypto_major avg `0.4705` n `8`; equity avg `-0.0125` n `121`; fx avg `0.0128` n `6`; index avg `-0.0001` n `25`; metal avg `0.0232` n `20`; unknown avg `0.2459` n `794`
- 24h: commodity avg `0.0092` n `12`; crypto_alt avg `1.1649` n `230`; crypto_major avg `3.0687` n `8`; equity avg `-0.7636` n `121`; fx avg `0.062` n `6`; index avg `-0.0362` n `25`; metal avg `-0.0955` n `20`; unknown avg `0.8049` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
