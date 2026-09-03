# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T11:52:35.202058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0476` n `12`; crypto_alt avg `0.0044` n `232`; crypto_major avg `-0.0144` n `8`; equity avg `-0.1068` n `133`; fx avg `-0.0052` n `6`; index avg `-0.0345` n `26`; metal avg `0.005` n `20`; unknown avg `-0.0607` n `792`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `0.3881` n `232`; crypto_major avg `0.5694` n `8`; equity avg `0.0388` n `133`; fx avg `-0.0169` n `6`; index avg `0.0077` n `26`; metal avg `0.0602` n `20`; unknown avg `1.5632` n `790`
- 4h: commodity avg `0.451` n `12`; crypto_alt avg `0.4587` n `232`; crypto_major avg `0.5694` n `8`; equity avg `-0.2842` n `133`; fx avg `-0.1178` n `6`; index avg `-0.0533` n `26`; metal avg `0.0131` n `20`; unknown avg `-0.1123` n `790`
- 24h: commodity avg `0.8141` n `12`; crypto_alt avg `2.3335` n `232`; crypto_major avg `2.2463` n `8`; equity avg `1.3983` n `133`; fx avg `-0.3884` n `6`; index avg `0.0646` n `26`; metal avg `0.6311` n `20`; unknown avg `-0.1615` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0419`, n `668`, weak_sample_signal
