# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T22:07:29.804582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0628` n `12`; crypto_alt avg `-0.0308` n `232`; crypto_major avg `-0.0071` n `8`; equity avg `-0.0365` n `131`; fx avg `0.0158` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0623` n `20`; unknown avg `0.0246` n `791`
- 1h: commodity avg `0.0452` n `12`; crypto_alt avg `-0.0116` n `232`; crypto_major avg `0.0538` n `8`; equity avg `-0.1958` n `131`; fx avg `0.018` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0173` n `20`; unknown avg `-0.0799` n `785`
- 4h: commodity avg `0.2331` n `12`; crypto_alt avg `-0.0216` n `232`; crypto_major avg `-0.1946` n `8`; equity avg `-0.2137` n `131`; fx avg `0.0079` n `6`; index avg `-0.0096` n `26`; metal avg `-0.1127` n `20`; unknown avg `2.128` n `773`
- 24h: commodity avg `0.9147` n `12`; crypto_alt avg `-0.6521` n `232`; crypto_major avg `-2.2153` n `8`; equity avg `-2.1256` n `130`; fx avg `0.0461` n `6`; index avg `-0.3423` n `26`; metal avg `-0.906` n `20`; unknown avg `-0.3982` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0445`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0313`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0307`, n `668`, weak_sample_signal
