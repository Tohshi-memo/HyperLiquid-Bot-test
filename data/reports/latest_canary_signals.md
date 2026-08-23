# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T19:07:31.221658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.0435` n `231`; crypto_major avg `-0.0387` n `8`; equity avg `0.0158` n `122`; fx avg `-0.0123` n `6`; index avg `0.0017` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.0616` n `793`
- 1h: commodity avg `-0.036` n `12`; crypto_alt avg `0.2773` n `231`; crypto_major avg `0.2544` n `8`; equity avg `0.109` n `122`; fx avg `-0.0071` n `6`; index avg `0.0289` n `25`; metal avg `0.0197` n `20`; unknown avg `0.3828` n `793`
- 4h: commodity avg `-0.0675` n `12`; crypto_alt avg `0.6173` n `231`; crypto_major avg `0.058` n `8`; equity avg `0.2778` n `122`; fx avg `-0.0067` n `6`; index avg `0.0642` n `25`; metal avg `0.0479` n `20`; unknown avg `0.5835` n `793`
- 24h: commodity avg `-0.0337` n `12`; crypto_alt avg `2.2221` n `231`; crypto_major avg `0.5432` n `8`; equity avg `0.7944` n `122`; fx avg `0.0117` n `6`; index avg `0.123` n `25`; metal avg `0.0975` n `20`; unknown avg `5.3391` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
