# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T05:07:25.531438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `0.1371` n `230`; crypto_major avg `0.2145` n `8`; equity avg `0.2227` n `92`; fx avg `0.0048` n `6`; index avg `0.0768` n `25`; metal avg `0.0408` n `20`; unknown avg `0.0299` n `766`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.2388` n `230`; crypto_major avg `0.2875` n `8`; equity avg `0.6267` n `92`; fx avg `0.0058` n `6`; index avg `0.1804` n `25`; metal avg `0.0905` n `20`; unknown avg `-0.069` n `766`
- 4h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.0227` n `230`; crypto_major avg `0.24` n `8`; equity avg `-0.2601` n `92`; fx avg `-0.0387` n `6`; index avg `-0.0148` n `25`; metal avg `0.3201` n `20`; unknown avg `-0.5553` n `766`
- 24h: commodity avg `0.9678` n `12`; crypto_alt avg `-0.3845` n `230`; crypto_major avg `-0.4869` n `8`; equity avg `-0.7946` n `92`; fx avg `-0.1971` n `6`; index avg `-0.0707` n `25`; metal avg `0.0551` n `20`; unknown avg `-0.2821` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
