# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T21:52:27.346166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `0.1125` n `232`; crypto_major avg `-0.0426` n `8`; equity avg `0.0141` n `134`; fx avg `0.002` n `6`; index avg `0.0119` n `26`; metal avg `0.0088` n `20`; unknown avg `0.7352` n `794`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `0.4775` n `232`; crypto_major avg `0.1697` n `8`; equity avg `0.0432` n `134`; fx avg `0.0056` n `6`; index avg `-0.0` n `26`; metal avg `0.0013` n `20`; unknown avg `33.2045` n `788`
- 4h: commodity avg `0.0878` n `12`; crypto_alt avg `0.6471` n `232`; crypto_major avg `0.0224` n `8`; equity avg `0.0078` n `134`; fx avg `-0.0167` n `6`; index avg `0.0212` n `26`; metal avg `-0.0063` n `20`; unknown avg `20.9435` n `770`
- 24h: commodity avg `0.145` n `12`; crypto_alt avg `3.4462` n `232`; crypto_major avg `2.7586` n `8`; equity avg `0.24` n `134`; fx avg `-0.0264` n `6`; index avg `0.0585` n `26`; metal avg `0.0708` n `20`; unknown avg `1281.0607` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
