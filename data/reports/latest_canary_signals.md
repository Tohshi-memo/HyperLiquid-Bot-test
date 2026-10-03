# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T14:37:28.475583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `13`; crypto_alt avg `0.2397` n `235`; crypto_major avg `0.0338` n `8`; equity avg `-0.002` n `143`; fx avg `0.0009` n `6`; index avg `0.0002` n `26`; metal avg `-0.0082` n `20`; unknown avg `-0.026` n `982`
- 1h: commodity avg `0.0844` n `13`; crypto_alt avg `0.3986` n `235`; crypto_major avg `0.0508` n `8`; equity avg `-0.0007` n `143`; fx avg `-0.0075` n `6`; index avg `0.0042` n `26`; metal avg `-0.0115` n `20`; unknown avg `-0.0094` n `964`
- 4h: commodity avg `0.2329` n `13`; crypto_alt avg `0.4556` n `235`; crypto_major avg `0.207` n `8`; equity avg `-0.004` n `143`; fx avg `-0.0183` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0161` n `20`; unknown avg `0.1141` n `954`
- 24h: commodity avg `0.9036` n `13`; crypto_alt avg `-1.5294` n `235`; crypto_major avg `-1.429` n `8`; equity avg `-0.7232` n `143`; fx avg `-0.0413` n `6`; index avg `-0.108` n `26`; metal avg `-0.2481` n `20`; unknown avg `0.6613` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
