# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T03:07:23.863494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `-0.0614` n `230`; crypto_major avg `-0.1129` n `8`; equity avg `-0.2316` n `92`; fx avg `-0.0306` n `6`; index avg `-0.0927` n `25`; metal avg `0.0378` n `20`; unknown avg `-0.111` n `766`
- 1h: commodity avg `0.1065` n `12`; crypto_alt avg `-0.2993` n `230`; crypto_major avg `-0.2295` n `8`; equity avg `-0.5907` n `92`; fx avg `-0.0409` n `6`; index avg `-0.169` n `25`; metal avg `0.0638` n `20`; unknown avg `-0.1872` n `766`
- 4h: commodity avg `0.0929` n `12`; crypto_alt avg `0.5813` n `230`; crypto_major avg `0.6431` n `8`; equity avg `-0.2932` n `92`; fx avg `-0.0466` n `6`; index avg `-0.1544` n `25`; metal avg `0.0911` n `20`; unknown avg `0.1354` n `766`
- 24h: commodity avg `1.0092` n `12`; crypto_alt avg `-0.6681` n `230`; crypto_major avg `-1.2629` n `8`; equity avg `-1.9525` n `92`; fx avg `-0.2061` n `6`; index avg `-0.4345` n `25`; metal avg `-0.0281` n `20`; unknown avg `-0.2914` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
