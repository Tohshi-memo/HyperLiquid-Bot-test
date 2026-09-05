# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T23:07:28.046564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.0596` n `232`; crypto_major avg `-0.1412` n `8`; equity avg `0.0003` n `134`; fx avg `-0.0006` n `6`; index avg `0.0076` n `26`; metal avg `-0.0022` n `20`; unknown avg `1.6301` n `792`
- 1h: commodity avg `-0.0169` n `12`; crypto_alt avg `-0.2076` n `232`; crypto_major avg `-0.418` n `8`; equity avg `0.0255` n `134`; fx avg `-0.0015` n `6`; index avg `0.0161` n `26`; metal avg `-0.0006` n `20`; unknown avg `2.3171` n `792`
- 4h: commodity avg `0.0324` n `12`; crypto_alt avg `0.3415` n `232`; crypto_major avg `-0.6239` n `8`; equity avg `0.0637` n `134`; fx avg `-0.0154` n `6`; index avg `-0.0047` n `26`; metal avg `0.0003` n `20`; unknown avg `2.3363` n `770`
- 24h: commodity avg `0.1302` n `12`; crypto_alt avg `3.2266` n `232`; crypto_major avg `2.2571` n `8`; equity avg `0.2721` n `134`; fx avg `-0.0535` n `6`; index avg `0.067` n `26`; metal avg `0.0606` n `20`; unknown avg `1281.4845` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
