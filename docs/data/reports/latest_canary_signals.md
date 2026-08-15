# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T04:21:56.532584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.0988` n `230`; crypto_major avg `0.0514` n `8`; equity avg `-0.0097` n `114`; fx avg `0.002` n `6`; index avg `0.0006` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0169` n `791`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `-0.0147` n `230`; crypto_major avg `-0.0737` n `8`; equity avg `0.0363` n `114`; fx avg `-0.0329` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0089` n `20`; unknown avg `-0.1496` n `791`
- 4h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.0577` n `230`; crypto_major avg `0.2783` n `8`; equity avg `0.1233` n `114`; fx avg `0.0571` n `6`; index avg `0.0079` n `25`; metal avg `-0.0348` n `20`; unknown avg `0.3769` n `791`
- 24h: commodity avg `0.175` n `12`; crypto_alt avg `0.4005` n `230`; crypto_major avg `-0.2863` n `8`; equity avg `-0.082` n `114`; fx avg `0.1563` n `6`; index avg `-0.0281` n `25`; metal avg `0.3755` n `20`; unknown avg `0.0058` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
