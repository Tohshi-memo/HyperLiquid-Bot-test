# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T23:29:34.256372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0341` n `12`; crypto_alt avg `0.0352` n `230`; crypto_major avg `0.0128` n `8`; equity avg `0.1362` n `92`; fx avg `0.0034` n `6`; index avg `0.0386` n `25`; metal avg `0.0424` n `20`; unknown avg `-0.0047` n `766`
- 1h: commodity avg `-0.0483` n `12`; crypto_alt avg `0.079` n `230`; crypto_major avg `-0.0016` n `8`; equity avg `0.2599` n `92`; fx avg `-0.0202` n `6`; index avg `0.0707` n `25`; metal avg `0.029` n `20`; unknown avg `0.1099` n `766`
- 4h: commodity avg `0.0101` n `12`; crypto_alt avg `0.1606` n `230`; crypto_major avg `0.0238` n `8`; equity avg `0.2832` n `92`; fx avg `-0.0121` n `6`; index avg `0.0725` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.2031` n `766`
- 24h: commodity avg `0.079` n `12`; crypto_alt avg `2.3788` n `230`; crypto_major avg `3.6592` n `8`; equity avg `2.0054` n `92`; fx avg `-0.0058` n `6`; index avg `0.5404` n `25`; metal avg `0.6114` n `20`; unknown avg `0.2131` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
