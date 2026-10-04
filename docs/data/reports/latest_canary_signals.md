# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T10:22:34.115804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `13`; crypto_alt avg `-0.0595` n `235`; crypto_major avg `0.041` n `8`; equity avg `0.0082` n `143`; fx avg `0.002` n `6`; index avg `0.0004` n `26`; metal avg `-0.0019` n `20`; unknown avg `-0.0239` n `1079`
- 1h: commodity avg `-0.0447` n `13`; crypto_alt avg `-0.2207` n `235`; crypto_major avg `0.147` n `8`; equity avg `0.0159` n `143`; fx avg `0.004` n `6`; index avg `0.0062` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.1045` n `1077`
- 4h: commodity avg `-0.0483` n `13`; crypto_alt avg `-0.0338` n `235`; crypto_major avg `0.5277` n `8`; equity avg `0.0074` n `143`; fx avg `0.0097` n `6`; index avg `0.0068` n `26`; metal avg `-0.0073` n `20`; unknown avg `0.1813` n `1061`
- 24h: commodity avg `0.0893` n `13`; crypto_alt avg `1.7732` n `235`; crypto_major avg `1.5075` n `8`; equity avg `0.249` n `143`; fx avg `-0.0258` n `6`; index avg `0.0333` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0343` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
