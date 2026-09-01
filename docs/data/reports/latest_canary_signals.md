# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T08:52:26.464098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.1198` n `232`; crypto_major avg `-0.1155` n `8`; equity avg `-0.0783` n `130`; fx avg `-0.0036` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0186` n `20`; unknown avg `-0.1169` n `792`
- 1h: commodity avg `0.0941` n `12`; crypto_alt avg `-1.0546` n `232`; crypto_major avg `-0.7827` n `8`; equity avg `-0.9489` n `130`; fx avg `-0.002` n `6`; index avg `-0.1975` n `26`; metal avg `-0.4726` n `20`; unknown avg `-0.3078` n `790`
- 4h: commodity avg `0.1313` n `12`; crypto_alt avg `-0.9578` n `232`; crypto_major avg `-1.0306` n `8`; equity avg `-1.0868` n `130`; fx avg `-0.0145` n `6`; index avg `-0.2025` n `26`; metal avg `-0.5223` n `20`; unknown avg `-0.1037` n `770`
- 24h: commodity avg `0.4577` n `12`; crypto_alt avg `0.2994` n `232`; crypto_major avg `-0.1274` n `8`; equity avg `-0.6279` n `130`; fx avg `0.0967` n `6`; index avg `-0.2511` n `26`; metal avg `-0.7078` n `20`; unknown avg `0.0997` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0402`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0369`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0331`, n `668`, weak_sample_signal
