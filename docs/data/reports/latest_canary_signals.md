# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T20:22:26.963762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `0.2635` n `232`; crypto_major avg `0.1805` n `8`; equity avg `0.0013` n `134`; fx avg `-0.0015` n `6`; index avg `0.0063` n `26`; metal avg `0.0118` n `20`; unknown avg `0.4401` n `793`
- 1h: commodity avg `-0.0299` n `12`; crypto_alt avg `0.3319` n `232`; crypto_major avg `0.168` n `8`; equity avg `0.0228` n `134`; fx avg `-0.0024` n `6`; index avg `0.0053` n `26`; metal avg `0.0045` n `20`; unknown avg `0.5031` n `781`
- 4h: commodity avg `-0.0474` n `12`; crypto_alt avg `0.1997` n `232`; crypto_major avg `0.1508` n `8`; equity avg `0.2033` n `134`; fx avg `-0.0087` n `6`; index avg `0.0223` n `26`; metal avg `0.0291` n `20`; unknown avg `0.5161` n `755`
- 24h: commodity avg `-0.0086` n `12`; crypto_alt avg `1.3232` n `232`; crypto_major avg `0.2572` n `8`; equity avg `0.3879` n `134`; fx avg `-0.0051` n `6`; index avg `0.0301` n `26`; metal avg `-0.0124` n `20`; unknown avg `120.1908` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
