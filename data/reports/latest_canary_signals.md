# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T19:22:25.599390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0387` n `12`; crypto_alt avg `0.1318` n `232`; crypto_major avg `-0.1182` n `8`; equity avg `-0.0102` n `134`; fx avg `0.0` n `6`; index avg `-0.0115` n `26`; metal avg `0.0005` n `20`; unknown avg `1.4568` n `794`
- 1h: commodity avg `0.0546` n `12`; crypto_alt avg `0.1101` n `232`; crypto_major avg `-0.3127` n `8`; equity avg `-0.0354` n `134`; fx avg `-0.0053` n `6`; index avg `0.0169` n `26`; metal avg `-0.0058` n `20`; unknown avg `1.3797` n `792`
- 4h: commodity avg `0.068` n `12`; crypto_alt avg `0.7182` n `232`; crypto_major avg `0.9896` n `8`; equity avg `0.0638` n `134`; fx avg `-0.0265` n `6`; index avg `0.0356` n `26`; metal avg `0.0305` n `20`; unknown avg `1.1352` n `786`
- 24h: commodity avg `0.0813` n `12`; crypto_alt avg `2.7613` n `232`; crypto_major avg `2.4831` n `8`; equity avg `0.4186` n `134`; fx avg `-0.0417` n `6`; index avg `0.0692` n `26`; metal avg `0.109` n `20`; unknown avg `0.1623` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
