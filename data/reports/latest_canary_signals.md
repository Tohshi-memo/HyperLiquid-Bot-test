# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T22:07:24.477701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.0134` n `232`; crypto_major avg `0.0038` n `8`; equity avg `0.0086` n `134`; fx avg `-0.0018` n `6`; index avg `-0.011` n `26`; metal avg `0.0004` n `20`; unknown avg `0.0897` n `792`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `0.5513` n `232`; crypto_major avg `0.2157` n `8`; equity avg `0.0339` n `134`; fx avg `0.0013` n `6`; index avg `0.0001` n `26`; metal avg `0.0029` n `20`; unknown avg `0.0363` n `792`
- 4h: commodity avg `0.058` n `12`; crypto_alt avg `0.6555` n `232`; crypto_major avg `-0.4557` n `8`; equity avg `0.0226` n `134`; fx avg `-0.0151` n `6`; index avg `0.0085` n `26`; metal avg `-0.0027` n `20`; unknown avg `1.9696` n `770`
- 24h: commodity avg `0.1625` n `12`; crypto_alt avg `3.5971` n `232`; crypto_major avg `2.7576` n `8`; equity avg `0.2521` n `134`; fx avg `-0.0507` n `6`; index avg `0.0556` n `26`; metal avg `0.0568` n `20`; unknown avg `1281.1093` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
