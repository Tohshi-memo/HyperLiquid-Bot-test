# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T04:52:26.053479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.052` n `12`; crypto_alt avg `-0.1137` n `232`; crypto_major avg `-0.0745` n `8`; equity avg `-0.0463` n `130`; fx avg `0.0085` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0221` n `20`; unknown avg `-0.116` n `792`
- 1h: commodity avg `0.0729` n `12`; crypto_alt avg `-0.0327` n `232`; crypto_major avg `-0.1176` n `8`; equity avg `0.0614` n `130`; fx avg `0.0093` n `6`; index avg `0.0028` n `26`; metal avg `-0.1144` n `20`; unknown avg `0.2615` n `790`
- 4h: commodity avg `0.0598` n `12`; crypto_alt avg `0.1304` n `232`; crypto_major avg `-0.0292` n `8`; equity avg `0.1486` n `130`; fx avg `0.0252` n `6`; index avg `0.0237` n `26`; metal avg `-0.1853` n `20`; unknown avg `0.1604` n `790`
- 24h: commodity avg `0.4581` n `12`; crypto_alt avg `2.1821` n `232`; crypto_major avg `2.0807` n `8`; equity avg `1.2532` n `130`; fx avg `0.0139` n `6`; index avg `0.0819` n `26`; metal avg `-0.0732` n `20`; unknown avg `0.4489` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
