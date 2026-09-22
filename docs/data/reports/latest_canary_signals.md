# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T22:37:32.862092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.2658` n `234`; crypto_major avg `0.147` n `8`; equity avg `0.0341` n `140`; fx avg `0.0018` n `6`; index avg `0.0015` n `26`; metal avg `0.0105` n `20`; unknown avg `0.2301` n `945`
- 1h: commodity avg `-0.0263` n `12`; crypto_alt avg `0.302` n `234`; crypto_major avg `0.0465` n `8`; equity avg `0.1092` n `140`; fx avg `0.0166` n `6`; index avg `0.0165` n `26`; metal avg `0.0354` n `20`; unknown avg `-0.0691` n `942`
- 4h: commodity avg `-0.0142` n `12`; crypto_alt avg `1.0207` n `234`; crypto_major avg `0.187` n `8`; equity avg `0.2543` n `140`; fx avg `-0.0234` n `6`; index avg `0.0271` n `26`; metal avg `0.0867` n `20`; unknown avg `0.252` n `906`
- 24h: commodity avg `0.1692` n `12`; crypto_alt avg `2.6139` n `234`; crypto_major avg `-0.0137` n `8`; equity avg `0.8778` n `140`; fx avg `-0.2804` n `6`; index avg `0.1042` n `26`; metal avg `0.2613` n `20`; unknown avg `1.6601` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
