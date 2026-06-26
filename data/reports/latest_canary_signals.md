# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T05:07:30.006453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.0625` n `228`; crypto_major avg `0.0006` n `8`; equity avg `0.1459` n `86`; fx avg `0.0072` n `6`; index avg `0.0534` n `23`; metal avg `0.0056` n `20`; unknown avg `-0.2685` n `765`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.397` n `228`; crypto_major avg `-0.3625` n `8`; equity avg `-0.2127` n `86`; fx avg `-0.008` n `6`; index avg `-0.0462` n `23`; metal avg `-0.0004` n `20`; unknown avg `1.503` n `765`
- 4h: commodity avg `-0.1921` n `12`; crypto_alt avg `-0.4685` n `228`; crypto_major avg `-0.0867` n `8`; equity avg `-1.3281` n `86`; fx avg `-0.0268` n `6`; index avg `-0.3322` n `23`; metal avg `-0.3468` n `20`; unknown avg `-0.0117` n `749`
- 24h: commodity avg `0.2773` n `12`; crypto_alt avg `-2.8536` n `228`; crypto_major avg `-2.8422` n `8`; equity avg `-4.3069` n `86`; fx avg `0.0355` n `6`; index avg `-0.6963` n `23`; metal avg `-0.1487` n `20`; unknown avg `0.6338` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
