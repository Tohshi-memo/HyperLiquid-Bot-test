# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T13:22:29.243339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.069` n `239`; crypto_major avg `0.0243` n `8`; equity avg `0.0195` n `166`; fx avg `0.0008` n `6`; index avg `-0.0082` n `27`; metal avg `0.0022` n `20`; unknown avg `-0.199` n `1261`
- 1h: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.0464` n `239`; crypto_major avg `-0.2701` n `8`; equity avg `-0.0861` n `166`; fx avg `0.0064` n `6`; index avg `0.013` n `27`; metal avg `-0.0406` n `20`; unknown avg `324.5275` n `1259`
- 4h: commodity avg `0.0027` n `13`; crypto_alt avg `0.5769` n `239`; crypto_major avg `0.5926` n `8`; equity avg `0.3245` n `166`; fx avg `-0.0126` n `6`; index avg `0.0313` n `27`; metal avg `0.0493` n `20`; unknown avg `155.4405` n `1151`
- 24h: commodity avg `-0.0074` n `13`; crypto_alt avg `1.7889` n `239`; crypto_major avg `1.8968` n `8`; equity avg `1.4287` n `166`; fx avg `-0.0029` n `6`; index avg `0.1683` n `27`; metal avg `0.0714` n `20`; unknown avg `0.5798` n `1086`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
