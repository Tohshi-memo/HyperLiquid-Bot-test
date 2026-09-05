# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T23:37:25.642787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `12`; crypto_alt avg `0.0033` n `232`; crypto_major avg `0.0051` n `8`; equity avg `0.0017` n `134`; fx avg `-0.0074` n `6`; index avg `0.0001` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0297` n `794`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `-0.1465` n `232`; crypto_major avg `-0.2152` n `8`; equity avg `0.0178` n `134`; fx avg `-0.0066` n `6`; index avg `-0.0151` n `26`; metal avg `-0.006` n `20`; unknown avg `0.2744` n `792`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `0.3427` n `232`; crypto_major avg `-0.426` n `8`; equity avg `0.0847` n `134`; fx avg `-0.0145` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.2531` n `770`
- 24h: commodity avg `0.135` n `12`; crypto_alt avg `2.8682` n `232`; crypto_major avg `2.0684` n `8`; equity avg `0.2763` n `134`; fx avg `-0.0741` n `6`; index avg `0.0772` n `26`; metal avg `0.0628` n `20`; unknown avg `1281.047` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
