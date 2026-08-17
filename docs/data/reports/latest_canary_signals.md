# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T14:39:54.308089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.0292` n `230`; crypto_major avg `0.0539` n `8`; equity avg `0.0941` n `114`; fx avg `-0.0112` n `6`; index avg `0.0308` n `25`; metal avg `0.0638` n `20`; unknown avg `0.0041` n `792`
- 1h: commodity avg `-0.0118` n `12`; crypto_alt avg `-0.1614` n `230`; crypto_major avg `-0.1398` n `8`; equity avg `0.2785` n `114`; fx avg `-0.0206` n `6`; index avg `0.0572` n `25`; metal avg `0.2355` n `20`; unknown avg `0.0259` n `792`
- 4h: commodity avg `0.0474` n `12`; crypto_alt avg `-0.0388` n `230`; crypto_major avg `-0.1383` n `8`; equity avg `-0.094` n `114`; fx avg `-0.0001` n `6`; index avg `0.0253` n `25`; metal avg `0.1125` n `20`; unknown avg `1.1805` n `792`
- 24h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1552` n `230`; crypto_major avg `0.6555` n `8`; equity avg `1.2385` n `114`; fx avg `0.0029` n `6`; index avg `0.175` n `25`; metal avg `0.3041` n `20`; unknown avg `0.1196` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
