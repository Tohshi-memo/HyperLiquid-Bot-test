# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T07:37:29.341793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.5658` n `232`; crypto_major avg `-0.5011` n `8`; equity avg `-0.0862` n `134`; fx avg `0.0007` n `6`; index avg `0.0089` n `26`; metal avg `0.0077` n `20`; unknown avg `0.6858` n `796`
- 1h: commodity avg `-0.0776` n `12`; crypto_alt avg `-0.6813` n `232`; crypto_major avg `-0.5631` n `8`; equity avg `-0.0873` n `134`; fx avg `0.0134` n `6`; index avg `0.0022` n `26`; metal avg `0.0135` n `20`; unknown avg `0.6545` n `794`
- 4h: commodity avg `0.0334` n `12`; crypto_alt avg `-0.3186` n `232`; crypto_major avg `-0.4158` n `8`; equity avg `0.0613` n `134`; fx avg `-0.0393` n `6`; index avg `0.0633` n `26`; metal avg `0.0041` n `20`; unknown avg `0.7839` n `758`
- 24h: commodity avg `0.0414` n `12`; crypto_alt avg `0.0486` n `232`; crypto_major avg `-0.7621` n `8`; equity avg `0.4052` n `134`; fx avg `-0.0509` n `6`; index avg `0.045` n `26`; metal avg `-0.1391` n `20`; unknown avg `382.7781` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
