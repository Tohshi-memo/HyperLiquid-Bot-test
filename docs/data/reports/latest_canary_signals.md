# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T03:07:26.102877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1479` n `232`; crypto_major avg `0.012` n `8`; equity avg `0.0761` n `130`; fx avg `-0.0067` n `6`; index avg `0.0217` n `26`; metal avg `0.0069` n `20`; unknown avg `-0.0427` n `790`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `0.1182` n `232`; crypto_major avg `0.0829` n `8`; equity avg `-0.0961` n `130`; fx avg `-0.0066` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0442` n `20`; unknown avg `-0.2071` n `790`
- 4h: commodity avg `0.0269` n `12`; crypto_alt avg `0.5233` n `232`; crypto_major avg `-0.007` n `8`; equity avg `0.0051` n `130`; fx avg `0.0105` n `6`; index avg `0.0506` n `26`; metal avg `0.0069` n `20`; unknown avg `0.2579` n `790`
- 24h: commodity avg `0.4036` n `12`; crypto_alt avg `1.8866` n `231`; crypto_major avg `1.7756` n `8`; equity avg `1.2844` n `130`; fx avg `-0.0265` n `6`; index avg `0.1325` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.2389` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
