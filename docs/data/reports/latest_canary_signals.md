# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T09:07:28.617005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `0.0184` n `228`; crypto_major avg `-0.1145` n `8`; equity avg `-0.0346` n `86`; fx avg `0.011` n `6`; index avg `-0.0161` n `23`; metal avg `-0.0481` n `20`; unknown avg `0.0119` n `764`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `0.1841` n `228`; crypto_major avg `0.1724` n `8`; equity avg `-0.0934` n `86`; fx avg `0.021` n `6`; index avg `-0.0083` n `23`; metal avg `-0.1217` n `20`; unknown avg `-0.0181` n `764`
- 4h: commodity avg `-0.1051` n `12`; crypto_alt avg `0.2771` n `228`; crypto_major avg `0.1343` n `8`; equity avg `0.3102` n `86`; fx avg `0.0309` n `6`; index avg `0.0862` n `23`; metal avg `0.0494` n `20`; unknown avg `0.0485` n `740`
- 24h: commodity avg `-0.49` n `12`; crypto_alt avg `0.4828` n `228`; crypto_major avg `0.2685` n `8`; equity avg `4.9013` n `86`; fx avg `-0.0101` n `6`; index avg `0.1148` n `23`; metal avg `-0.3846` n `20`; unknown avg `0.0867` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
