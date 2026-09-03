# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T23:37:27.078913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.2548` n `232`; crypto_major avg `0.1533` n `8`; equity avg `0.0347` n `133`; fx avg `-0.0119` n `6`; index avg `0.0034` n `26`; metal avg `0.0245` n `20`; unknown avg `-0.2213` n `792`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `0.3426` n `232`; crypto_major avg `0.4399` n `8`; equity avg `0.0581` n `133`; fx avg `-0.007` n `6`; index avg `0.0107` n `26`; metal avg `0.0094` n `20`; unknown avg `2.3311` n `790`
- 4h: commodity avg `0.1086` n `12`; crypto_alt avg `-0.3489` n `232`; crypto_major avg `-0.2935` n `8`; equity avg `-0.0745` n `133`; fx avg `0.0063` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0094` n `20`; unknown avg `4.5624` n `766`
- 24h: commodity avg `-0.0756` n `12`; crypto_alt avg `4.2836` n `232`; crypto_major avg `5.3633` n `8`; equity avg `1.238` n `133`; fx avg `-0.2278` n `6`; index avg `0.1658` n `26`; metal avg `0.8274` n `20`; unknown avg `1.2994` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
