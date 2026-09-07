# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T21:07:27.861263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.0069` n `232`; crypto_major avg `-0.1394` n `8`; equity avg `0.0131` n `134`; fx avg `-0.0065` n `6`; index avg `0.0033` n `26`; metal avg `-0.0038` n `20`; unknown avg `28.4022` n `786`
- 1h: commodity avg `-0.0226` n `12`; crypto_alt avg `0.3306` n `232`; crypto_major avg `0.0247` n `8`; equity avg `0.0138` n `134`; fx avg `-0.0007` n `6`; index avg `0.0029` n `26`; metal avg `0.011` n `20`; unknown avg `5.1052` n `764`
- 4h: commodity avg `0.0134` n `12`; crypto_alt avg `0.2876` n `232`; crypto_major avg `0.0123` n `8`; equity avg `0.1289` n `134`; fx avg `-0.0125` n `6`; index avg `0.0191` n `26`; metal avg `0.0102` n `20`; unknown avg `-0.2803` n `734`
- 24h: commodity avg `0.1615` n `12`; crypto_alt avg `0.295` n `232`; crypto_major avg `-1.195` n `8`; equity avg `0.46` n `134`; fx avg `-0.1511` n `6`; index avg `0.0835` n `26`; metal avg `0.0154` n `20`; unknown avg `7800.9769` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
