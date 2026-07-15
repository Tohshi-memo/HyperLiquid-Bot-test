# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T03:22:31.565761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `0.1403` n `230`; crypto_major avg `0.0719` n `8`; equity avg `0.0545` n `93`; fx avg `-0.0132` n `6`; index avg `0.0121` n `25`; metal avg `-0.0645` n `20`; unknown avg `-0.0495` n `767`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.0731` n `230`; crypto_major avg `0.4546` n `8`; equity avg `0.3` n `93`; fx avg `0.0038` n `6`; index avg `0.026` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.1322` n `767`
- 4h: commodity avg `0.1104` n `12`; crypto_alt avg `-0.0692` n `230`; crypto_major avg `-0.0366` n `8`; equity avg `1.0737` n `93`; fx avg `0.0582` n `6`; index avg `0.1234` n `25`; metal avg `-0.0747` n `20`; unknown avg `-0.5637` n `767`
- 24h: commodity avg `0.0917` n `12`; crypto_alt avg `2.3809` n `230`; crypto_major avg `3.7771` n `8`; equity avg `3.4352` n `92`; fx avg `0.1099` n `6`; index avg `0.9497` n `25`; metal avg `0.4996` n `20`; unknown avg `0.2949` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
