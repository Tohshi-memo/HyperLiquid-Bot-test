# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T09:37:25.397871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0587` n `230`; crypto_major avg `-0.1364` n `8`; equity avg `-0.0801` n `93`; fx avg `-0.0027` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0434` n `20`; unknown avg `-0.0547` n `767`
- 1h: commodity avg `0.0577` n `12`; crypto_alt avg `0.2465` n `230`; crypto_major avg `0.3705` n `8`; equity avg `0.1539` n `93`; fx avg `-0.0211` n `6`; index avg `0.0182` n `25`; metal avg `-0.0378` n `20`; unknown avg `-0.0239` n `767`
- 4h: commodity avg `0.0834` n `12`; crypto_alt avg `0.1637` n `230`; crypto_major avg `0.284` n `8`; equity avg `-0.0087` n `93`; fx avg `-0.0021` n `6`; index avg `-0.0486` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.0873` n `747`
- 24h: commodity avg `-0.0714` n `12`; crypto_alt avg `1.8709` n `230`; crypto_major avg `3.5501` n `8`; equity avg `1.2319` n `92`; fx avg `0.0253` n `6`; index avg `0.4303` n `25`; metal avg `0.2816` n `20`; unknown avg `0.3506` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
