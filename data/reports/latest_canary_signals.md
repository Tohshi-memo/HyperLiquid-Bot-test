# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T22:15:07.887019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0033` n `232`; crypto_major avg `-0.0125` n `8`; equity avg `0.0089` n `134`; fx avg `0.0029` n `6`; index avg `0.0089` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.347` n `794`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.271` n `232`; crypto_major avg `-0.0004` n `8`; equity avg `0.0335` n `134`; fx avg `0.0023` n `6`; index avg `0.0031` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.1815` n `792`
- 4h: commodity avg `0.0613` n `12`; crypto_alt avg `0.5288` n `232`; crypto_major avg `-0.4144` n `8`; equity avg `0.0217` n `134`; fx avg `-0.0164` n `6`; index avg `0.0166` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.6402` n `770`
- 24h: commodity avg `0.1499` n `12`; crypto_alt avg `3.5618` n `232`; crypto_major avg `2.6949` n `8`; equity avg `0.2806` n `134`; fx avg `-0.047` n `6`; index avg `0.0603` n `26`; metal avg `0.0605` n `20`; unknown avg `1281.059` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
