# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T23:22:29.164394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.0256` n `232`; crypto_major avg `-0.0376` n `8`; equity avg `0.0085` n `134`; fx avg `-0.0003` n `6`; index avg `-0.0054` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.0258` n `794`
- 1h: commodity avg `-0.0347` n `12`; crypto_alt avg `-0.1885` n `232`; crypto_major avg `-0.3078` n `8`; equity avg `0.0358` n `134`; fx avg `-0.0017` n `6`; index avg `-0.0172` n `26`; metal avg `0.0002` n `20`; unknown avg `10.3598` n `792`
- 4h: commodity avg `-0.0234` n `12`; crypto_alt avg `0.1857` n `232`; crypto_major avg `-0.5438` n `8`; equity avg `0.0825` n `134`; fx avg `-0.0157` n `6`; index avg `0.0014` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.4731` n `770`
- 24h: commodity avg `0.1212` n `12`; crypto_alt avg `3.0696` n `232`; crypto_major avg `2.1287` n `8`; equity avg `0.2791` n `134`; fx avg `-0.0561` n `6`; index avg `0.0691` n `26`; metal avg `0.0584` n `20`; unknown avg `1281.1676` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
