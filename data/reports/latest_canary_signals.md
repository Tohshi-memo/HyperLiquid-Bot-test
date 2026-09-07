# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T00:06:01.002180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.1028` n `232`; crypto_major avg `0.0385` n `8`; equity avg `0.1383` n `134`; fx avg `-0.0188` n `6`; index avg `0.0022` n `26`; metal avg `0.0026` n `20`; unknown avg `142.588` n `792`
- 1h: commodity avg `0.0168` n `12`; crypto_alt avg `0.452` n `232`; crypto_major avg `0.2663` n `8`; equity avg `0.1274` n `134`; fx avg `0.0018` n `6`; index avg `0.0079` n `26`; metal avg `-0.0273` n `20`; unknown avg `143.2927` n `788`
- 4h: commodity avg `-0.0223` n `12`; crypto_alt avg `1.0492` n `232`; crypto_major avg `0.8872` n `8`; equity avg `0.0545` n `134`; fx avg `0.0307` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0697` n `20`; unknown avg `144.794` n `777`
- 24h: commodity avg `0.0272` n `12`; crypto_alt avg `1.7874` n `232`; crypto_major avg `1.1059` n `8`; equity avg `0.329` n `134`; fx avg `0.0379` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0889` n `20`; unknown avg `152.0813` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
