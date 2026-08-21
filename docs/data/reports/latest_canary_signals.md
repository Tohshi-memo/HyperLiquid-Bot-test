# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T05:52:31.106031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.0746` n `230`; crypto_major avg `0.1762` n `8`; equity avg `-0.1399` n `121`; fx avg `0.0142` n `6`; index avg `-0.0292` n `25`; metal avg `0.0416` n `20`; unknown avg `-0.0618` n `793`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `0.3203` n `230`; crypto_major avg `0.3601` n `8`; equity avg `-0.0205` n `121`; fx avg `0.0187` n `6`; index avg `-0.0242` n `25`; metal avg `0.0233` n `20`; unknown avg `0.0883` n `793`
- 4h: commodity avg `-0.078` n `12`; crypto_alt avg `0.8981` n `230`; crypto_major avg `-0.0258` n `8`; equity avg `0.0428` n `121`; fx avg `0.0232` n `6`; index avg `0.0263` n `25`; metal avg `0.1525` n `20`; unknown avg `-0.1182` n `793`
- 24h: commodity avg `0.2688` n `12`; crypto_alt avg `6.3518` n `230`; crypto_major avg `7.3825` n `8`; equity avg `-0.4262` n `121`; fx avg `-0.0319` n `6`; index avg `-0.0763` n `25`; metal avg `0.6777` n `20`; unknown avg `2.7031` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
