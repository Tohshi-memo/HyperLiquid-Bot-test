# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T13:22:27.996956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.3442` n `232`; crypto_major avg `0.1638` n `8`; equity avg `0.2468` n `131`; fx avg `-0.005` n `6`; index avg `0.0166` n `26`; metal avg `-0.0967` n `20`; unknown avg `0.4245` n `792`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `-0.323` n `232`; crypto_major avg `-0.3868` n `8`; equity avg `-0.1323` n `130`; fx avg `-0.0153` n `6`; index avg `-0.0126` n `26`; metal avg `-0.196` n `20`; unknown avg `0.2802` n `790`
- 4h: commodity avg `-0.1003` n `12`; crypto_alt avg `0.2894` n `232`; crypto_major avg `-0.0878` n `8`; equity avg `-0.4083` n `130`; fx avg `-0.0042` n `6`; index avg `-0.0453` n `26`; metal avg `-0.1867` n `20`; unknown avg `-0.4561` n `790`
- 24h: commodity avg `0.3012` n `12`; crypto_alt avg `0.9934` n `232`; crypto_major avg `0.1073` n `8`; equity avg `-0.8466` n `130`; fx avg `0.0605` n `6`; index avg `-0.2817` n `26`; metal avg `-0.835` n `20`; unknown avg `-0.0106` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0311`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0303`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0298`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0291`, n `668`, weak_sample_signal
