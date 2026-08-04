# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T21:37:39.575002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `0.0007` n `230`; crypto_major avg `-0.0136` n `8`; equity avg `0.0355` n `108`; fx avg `0.0058` n `6`; index avg `0.0148` n `25`; metal avg `0.0065` n `20`; unknown avg `0.0737` n `781`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.0081` n `230`; crypto_major avg `-0.1242` n `8`; equity avg `0.3371` n `108`; fx avg `0.0105` n `6`; index avg `0.0308` n `25`; metal avg `0.0174` n `20`; unknown avg `0.0995` n `781`
- 4h: commodity avg `-0.0733` n `12`; crypto_alt avg `0.2253` n `230`; crypto_major avg `-0.0987` n `8`; equity avg `-0.594` n `108`; fx avg `0.0575` n `6`; index avg `-0.0075` n `25`; metal avg `-0.1603` n `20`; unknown avg `0.0249` n `781`
- 24h: commodity avg `-1.2401` n `12`; crypto_alt avg `-0.1369` n `230`; crypto_major avg `0.4303` n `8`; equity avg `3.0651` n `107`; fx avg `0.1278` n `6`; index avg `0.7292` n `25`; metal avg `0.8573` n `20`; unknown avg `0.4254` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
