# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T08:22:28.005175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.0355` n `239`; crypto_major avg `0.0323` n `8`; equity avg `0.0824` n `168`; fx avg `0.0147` n `6`; index avg `0.0077` n `27`; metal avg `0.0598` n `20`; unknown avg `2.5887` n `1257`
- 1h: commodity avg `-0.1783` n `13`; crypto_alt avg `-0.2357` n `239`; crypto_major avg `-0.6182` n `8`; equity avg `-0.0324` n `168`; fx avg `0.0129` n `6`; index avg `0.0117` n `27`; metal avg `0.0821` n `20`; unknown avg `185.2342` n `1241`
- 4h: commodity avg `-0.3076` n `13`; crypto_alt avg `-0.1233` n `239`; crypto_major avg `-0.8559` n `8`; equity avg `-1.3832` n `168`; fx avg `-0.048` n `6`; index avg `-0.1317` n `27`; metal avg `-0.2667` n `20`; unknown avg `208.6646` n `1207`
- 24h: commodity avg `0.039` n `13`; crypto_alt avg `-2.9948` n `239`; crypto_major avg `-3.6207` n `8`; equity avg `-5.885` n `167`; fx avg `0.0899` n `6`; index avg `-0.5625` n `27`; metal avg `-0.9963` n `20`; unknown avg `694.8128` n `1029`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
