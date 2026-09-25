# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T09:37:27.683683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.2436` n `234`; crypto_major avg `0.3448` n `8`; equity avg `-0.006` n `141`; fx avg `0.011` n `6`; index avg `-0.0054` n `26`; metal avg `0.0023` n `20`; unknown avg `1.2248` n `946`
- 1h: commodity avg `-0.0675` n `12`; crypto_alt avg `0.3062` n `234`; crypto_major avg `0.5488` n `8`; equity avg `0.1483` n `141`; fx avg `-0.0308` n `6`; index avg `0.0252` n `26`; metal avg `0.0597` n `20`; unknown avg `1.572` n `944`
- 4h: commodity avg `-0.084` n `12`; crypto_alt avg `1.733` n `234`; crypto_major avg `1.2159` n `8`; equity avg `0.4975` n `141`; fx avg `-0.0304` n `6`; index avg `0.0848` n `26`; metal avg `0.1776` n `20`; unknown avg `0.6388` n `904`
- 24h: commodity avg `-0.0251` n `12`; crypto_alt avg `5.1224` n `234`; crypto_major avg `3.0275` n `8`; equity avg `2.2636` n `141`; fx avg `-0.2335` n `6`; index avg `0.3399` n `26`; metal avg `0.2153` n `20`; unknown avg `14.5868` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
