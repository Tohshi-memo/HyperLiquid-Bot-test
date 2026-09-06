# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T18:22:59.297925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.0179` n `232`; crypto_major avg `0.0399` n `8`; equity avg `0.0181` n `134`; fx avg `0.007` n `6`; index avg `0.0055` n `26`; metal avg `-0.0018` n `20`; unknown avg `-0.0046` n `787`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `0.1693` n `232`; crypto_major avg `0.1406` n `8`; equity avg `0.0966` n `134`; fx avg `0.0134` n `6`; index avg `0.0134` n `26`; metal avg `0.018` n `20`; unknown avg `-0.1456` n `783`
- 4h: commodity avg `-0.0025` n `12`; crypto_alt avg `0.4705` n `232`; crypto_major avg `0.2204` n `8`; equity avg `0.143` n `134`; fx avg `-0.0058` n `6`; index avg `0.0242` n `26`; metal avg `0.0115` n `20`; unknown avg `-0.1793` n `770`
- 24h: commodity avg `0.0742` n `12`; crypto_alt avg `1.1382` n `232`; crypto_major avg `-0.3308` n `8`; equity avg `0.2693` n `134`; fx avg `-0.0186` n `6`; index avg `0.0255` n `26`; metal avg `-0.039` n `20`; unknown avg `71.285` n `670`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
