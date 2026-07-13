# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T12:22:25.663944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.1165` n `230`; crypto_major avg `-0.1083` n `8`; equity avg `0.0101` n `92`; fx avg `0.0213` n `6`; index avg `0.0003` n `25`; metal avg `0.0182` n `20`; unknown avg `0.0465` n `766`
- 1h: commodity avg `0.1219` n `12`; crypto_alt avg `-0.3183` n `230`; crypto_major avg `-0.313` n `8`; equity avg `-0.2077` n `92`; fx avg `0.0252` n `6`; index avg `-0.0489` n `25`; metal avg `0.0075` n `20`; unknown avg `0.0313` n `766`
- 4h: commodity avg `0.1906` n `12`; crypto_alt avg `-0.1052` n `230`; crypto_major avg `-0.3497` n `8`; equity avg `0.0202` n `92`; fx avg `-0.0359` n `6`; index avg `-0.042` n `25`; metal avg `-0.1309` n `20`; unknown avg `-0.0854` n `766`
- 24h: commodity avg `0.0301` n `12`; crypto_alt avg `-1.3871` n `230`; crypto_major avg `-1.6962` n `8`; equity avg `-2.1187` n `92`; fx avg `-0.0373` n `6`; index avg `-0.4654` n `25`; metal avg `-0.25` n `20`; unknown avg `-0.142` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
