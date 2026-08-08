# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T09:07:28.172380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0226` n `230`; crypto_major avg `0.0405` n `8`; equity avg `0.0032` n `112`; fx avg `0.0049` n `6`; index avg `0.0084` n `25`; metal avg `0.0081` n `20`; unknown avg `0.0075` n `784`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0699` n `230`; crypto_major avg `0.1398` n `8`; equity avg `0.0526` n `112`; fx avg `0.0009` n `6`; index avg `0.003` n `25`; metal avg `0.0114` n `20`; unknown avg `0.1333` n `784`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `0.1935` n `230`; crypto_major avg `0.2101` n `8`; equity avg `0.0461` n `112`; fx avg `0.002` n `6`; index avg `0.0027` n `25`; metal avg `0.0149` n `20`; unknown avg `0.1411` n `751`
- 24h: commodity avg `-0.1034` n `12`; crypto_alt avg `0.0101` n `230`; crypto_major avg `0.3247` n `8`; equity avg `0.7302` n `112`; fx avg `-0.0296` n `6`; index avg `0.0349` n `25`; metal avg `-0.1016` n `20`; unknown avg `0.126` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
