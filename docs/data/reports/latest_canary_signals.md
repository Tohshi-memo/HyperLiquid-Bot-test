# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T12:37:30.405060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `-0.2372` n `230`; crypto_major avg `-0.3493` n `8`; equity avg `-0.2227` n `92`; fx avg `-0.0067` n `6`; index avg `-0.0263` n `25`; metal avg `-0.0311` n `20`; unknown avg `-0.0032` n `766`
- 1h: commodity avg `0.1461` n `12`; crypto_alt avg `-0.462` n `230`; crypto_major avg `-0.5759` n `8`; equity avg `-0.5068` n `92`; fx avg `0.0272` n `6`; index avg `-0.0734` n `25`; metal avg `-0.1121` n `20`; unknown avg `0.114` n `766`
- 4h: commodity avg `0.1917` n `12`; crypto_alt avg `-0.2814` n `230`; crypto_major avg `-0.7048` n `8`; equity avg `-0.1736` n `92`; fx avg `-0.0382` n `6`; index avg `-0.0778` n `25`; metal avg `-0.1246` n `20`; unknown avg `-0.1411` n `766`
- 24h: commodity avg `0.1003` n `12`; crypto_alt avg `-1.5662` n `230`; crypto_major avg `-2.0175` n `8`; equity avg `-2.3376` n `92`; fx avg `-0.0396` n `6`; index avg `-0.4875` n `25`; metal avg `-0.2804` n `20`; unknown avg `-0.1635` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
