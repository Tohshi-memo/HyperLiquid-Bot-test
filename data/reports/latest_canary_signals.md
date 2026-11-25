# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T22:07:37.592653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.205` n `239`; crypto_major avg `-0.2006` n `8`; equity avg `0.0378` n `168`; fx avg `-0.0013` n `6`; index avg `0.003` n `27`; metal avg `0.0806` n `20`; unknown avg `1.4414` n `1251`
- 1h: commodity avg `-0.011` n `13`; crypto_alt avg `-0.1282` n `239`; crypto_major avg `-0.2793` n `8`; equity avg `-0.1998` n `168`; fx avg `-0.0085` n `6`; index avg `-0.018` n `27`; metal avg `0.095` n `20`; unknown avg `15.6534` n `1251`
- 4h: commodity avg `-0.0224` n `13`; crypto_alt avg `1.104` n `239`; crypto_major avg `1.0461` n `8`; equity avg `1.9062` n `168`; fx avg `-0.0035` n `6`; index avg `0.1699` n `27`; metal avg `0.5569` n `20`; unknown avg `3.5493` n `1201`
- 24h: commodity avg `0.4129` n `13`; crypto_alt avg `2.3324` n `239`; crypto_major avg `1.005` n `8`; equity avg `-0.7523` n `168`; fx avg `0.048` n `6`; index avg `-0.0858` n `27`; metal avg `0.2465` n `20`; unknown avg `1.5414` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
