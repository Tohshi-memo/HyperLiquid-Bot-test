# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T22:22:38.893420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `0.0102` n `233`; crypto_major avg `0.0703` n `8`; equity avg `-0.0272` n `134`; fx avg `-0.0034` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0169` n `20`; unknown avg `0.2483` n `773`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `0.0509` n `233`; crypto_major avg `0.1649` n `8`; equity avg `-0.0434` n `134`; fx avg `-0.0176` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0542` n `20`; unknown avg `-0.225` n `747`
- 4h: commodity avg `0.1882` n `12`; crypto_alt avg `-0.8324` n `233`; crypto_major avg `-0.511` n `8`; equity avg `-0.6264` n `134`; fx avg `-0.0674` n `6`; index avg `-0.1319` n `26`; metal avg `-0.2767` n `20`; unknown avg `0.2182` n `725`
- 24h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.211` n `232`; crypto_major avg `0.2127` n `8`; equity avg `0.3473` n `134`; fx avg `-0.1278` n `6`; index avg `-0.1643` n `26`; metal avg `-0.3542` n `20`; unknown avg `0.4995` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
