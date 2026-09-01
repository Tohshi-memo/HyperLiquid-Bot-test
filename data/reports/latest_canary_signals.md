# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T00:37:24.390477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0833` n `232`; crypto_major avg `-0.0487` n `8`; equity avg `0.0228` n `129`; fx avg `0.0529` n `6`; index avg `0.0148` n `26`; metal avg `-0.013` n `20`; unknown avg `3.3413` n `793`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `0.6151` n `232`; crypto_major avg `0.2725` n `8`; equity avg `0.0438` n `129`; fx avg `0.0288` n `6`; index avg `0.0237` n `26`; metal avg `0.1115` n `20`; unknown avg `2.3163` n `791`
- 4h: commodity avg `0.0736` n `12`; crypto_alt avg `0.7287` n `232`; crypto_major avg `0.069` n `8`; equity avg `0.065` n `129`; fx avg `0.0305` n `6`; index avg `0.0316` n `26`; metal avg `0.0947` n `20`; unknown avg `0.0589` n `785`
- 24h: commodity avg `0.6907` n `12`; crypto_alt avg `1.8411` n `231`; crypto_major avg `1.3683` n `8`; equity avg `0.9513` n `129`; fx avg `-0.0986` n `6`; index avg `0.1004` n `26`; metal avg `-0.2699` n `20`; unknown avg `0.1947` n `740`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
