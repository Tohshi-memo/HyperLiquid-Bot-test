# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T02:52:28.879334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0605` n `13`; crypto_alt avg `-0.091` n `239`; crypto_major avg `-0.022` n `8`; equity avg `-0.2606` n `168`; fx avg `-0.0006` n `6`; index avg `-0.0353` n `27`; metal avg `-0.1012` n `20`; unknown avg `1.6629` n `1267`
- 1h: commodity avg `-0.0247` n `13`; crypto_alt avg `0.1485` n `239`; crypto_major avg `0.1475` n `8`; equity avg `0.1878` n `168`; fx avg `-0.0103` n `6`; index avg `0.0022` n `27`; metal avg `0.4036` n `20`; unknown avg `20.5442` n `1263`
- 4h: commodity avg `-0.0173` n `13`; crypto_alt avg `1.2936` n `239`; crypto_major avg `0.9164` n `8`; equity avg `1.0405` n `168`; fx avg `-0.0493` n `6`; index avg `0.1019` n `27`; metal avg `0.2327` n `20`; unknown avg `0.0339` n `1201`
- 24h: commodity avg `0.5594` n `13`; crypto_alt avg `4.1929` n `239`; crypto_major avg `3.1526` n `8`; equity avg `2.4686` n `168`; fx avg `-0.0129` n `6`; index avg `0.2115` n `27`; metal avg `0.601` n `20`; unknown avg `770.6277` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1966`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
