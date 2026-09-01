# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T09:37:28.218231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.0027` n `232`; crypto_major avg `-0.0357` n `8`; equity avg `-0.0113` n `130`; fx avg `0.0097` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0579` n `20`; unknown avg `-0.156` n `792`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `-0.1934` n `232`; crypto_major avg `-0.0271` n `8`; equity avg `-0.3646` n `130`; fx avg `0.0207` n `6`; index avg `-0.0812` n `26`; metal avg `-0.0783` n `20`; unknown avg `-0.352` n `790`
- 4h: commodity avg `0.1871` n `12`; crypto_alt avg `-1.3818` n `232`; crypto_major avg `-1.2623` n `8`; equity avg `-1.4156` n `130`; fx avg `0.0551` n `6`; index avg `-0.3103` n `26`; metal avg `-0.6541` n `20`; unknown avg `-0.2858` n `770`
- 24h: commodity avg `0.4014` n `12`; crypto_alt avg `0.2492` n `232`; crypto_major avg `-0.0843` n `8`; equity avg `-0.8501` n `130`; fx avg `0.1012` n `6`; index avg `-0.315` n `26`; metal avg `-0.7833` n `20`; unknown avg `0.084` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0455`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0358`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.03`, n `668`, weak_sample_signal
