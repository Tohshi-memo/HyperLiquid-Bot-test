# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T09:07:29.587351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.0273` n `235`; crypto_major avg `-0.0222` n `8`; equity avg `-0.0057` n `143`; fx avg `0.0006` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.2952` n `1077`
- 1h: commodity avg `0.0231` n `13`; crypto_alt avg `-0.1464` n `235`; crypto_major avg `-0.0396` n `8`; equity avg `0.0114` n `143`; fx avg `-0.0005` n `6`; index avg `0.0028` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.4154` n `1077`
- 4h: commodity avg `0.0002` n `13`; crypto_alt avg `0.125` n `235`; crypto_major avg `0.2935` n `8`; equity avg `-0.0334` n `143`; fx avg `-0.0175` n `6`; index avg `-0.0061` n `26`; metal avg `0.0055` n `20`; unknown avg `0.3679` n `1033`
- 24h: commodity avg `0.1466` n `13`; crypto_alt avg `2.5141` n `235`; crypto_major avg `1.2593` n `8`; equity avg `0.235` n `143`; fx avg `-0.043` n `6`; index avg `0.0168` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.1705` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
