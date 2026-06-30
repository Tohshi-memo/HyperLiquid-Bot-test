# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T05:37:33.638805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.2143` n `228`; crypto_major avg `-0.1081` n `8`; equity avg `-0.2115` n `88`; fx avg `0.0126` n `6`; index avg `-0.0622` n `23`; metal avg `0.0051` n `20`; unknown avg `-0.1895` n `763`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.338` n `228`; crypto_major avg `-0.3448` n `8`; equity avg `-0.2188` n `88`; fx avg `0.0029` n `6`; index avg `-0.0729` n `23`; metal avg `-0.228` n `20`; unknown avg `-0.6093` n `763`
- 4h: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.2764` n `228`; crypto_major avg `-0.6098` n `8`; equity avg `0.5226` n `88`; fx avg `-0.05` n `6`; index avg `0.1434` n `23`; metal avg `0.0329` n `20`; unknown avg `9.5702` n `761`
- 24h: commodity avg `-0.1101` n `12`; crypto_alt avg `0.1562` n `228`; crypto_major avg `1.2545` n `8`; equity avg `2.2524` n `88`; fx avg `0.1068` n `6`; index avg `0.3117` n `23`; metal avg `-0.3406` n `20`; unknown avg `12.1478` n `726`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
