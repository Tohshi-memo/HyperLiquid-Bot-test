# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T03:37:24.187072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.0379` n `230`; crypto_major avg `0.0737` n `8`; equity avg `0.0912` n `93`; fx avg `0.0182` n `6`; index avg `0.015` n `25`; metal avg `0.0377` n `20`; unknown avg `0.0204` n `767`
- 1h: commodity avg `-0.0176` n `12`; crypto_alt avg `0.173` n `230`; crypto_major avg `0.543` n `8`; equity avg `0.3221` n `93`; fx avg `0.026` n `6`; index avg `0.0328` n `25`; metal avg `-0.0272` n `20`; unknown avg `0.0524` n `767`
- 4h: commodity avg `0.1025` n `12`; crypto_alt avg `-0.0395` n `230`; crypto_major avg `-0.0052` n `8`; equity avg `1.0758` n `93`; fx avg `0.0965` n `6`; index avg `0.1374` n `25`; metal avg `-0.0529` n `20`; unknown avg `-0.5289` n `767`
- 24h: commodity avg `0.0992` n `12`; crypto_alt avg `2.1081` n `230`; crypto_major avg `3.4347` n `8`; equity avg `3.1395` n `92`; fx avg `0.1519` n `6`; index avg `0.8291` n `25`; metal avg `0.4566` n `20`; unknown avg `0.264` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
