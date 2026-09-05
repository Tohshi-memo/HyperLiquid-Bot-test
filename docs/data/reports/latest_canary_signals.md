# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T19:37:26.411846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `-0.1567` n `232`; crypto_major avg `-0.1129` n `8`; equity avg `-0.0004` n `134`; fx avg `-0.0086` n `6`; index avg `0.0122` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.2019` n `794`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0589` n `232`; crypto_major avg `-0.367` n `8`; equity avg `-0.0308` n `134`; fx avg `-0.0073` n `6`; index avg `0.0395` n `26`; metal avg `-0.004` n `20`; unknown avg `19.7583` n `792`
- 4h: commodity avg `0.0261` n `12`; crypto_alt avg `0.6102` n `232`; crypto_major avg `0.8269` n `8`; equity avg `0.0542` n `134`; fx avg `-0.0361` n `6`; index avg `0.0579` n `26`; metal avg `0.0228` n `20`; unknown avg `1.1753` n `786`
- 24h: commodity avg `0.0518` n `12`; crypto_alt avg `2.5544` n `232`; crypto_major avg `2.5219` n `8`; equity avg `0.3588` n `134`; fx avg `-0.0522` n `6`; index avg `0.0671` n `26`; metal avg `0.0635` n `20`; unknown avg `0.1505` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
