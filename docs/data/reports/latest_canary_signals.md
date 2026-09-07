# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T05:22:25.162360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.1181` n `232`; crypto_major avg `0.2358` n `8`; equity avg `-0.0212` n `134`; fx avg `0.0025` n `6`; index avg `-0.001` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.1785` n `794`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `0.3057` n `232`; crypto_major avg `0.2999` n `8`; equity avg `-0.0165` n `134`; fx avg `-0.0225` n `6`; index avg `-0.0009` n `26`; metal avg `0.0069` n `20`; unknown avg `0.3785` n `786`
- 4h: commodity avg `0.1059` n `12`; crypto_alt avg `0.2656` n `232`; crypto_major avg `0.0278` n `8`; equity avg `0.2567` n `134`; fx avg `0.1056` n `6`; index avg `0.0003` n `26`; metal avg `0.0358` n `20`; unknown avg `133.8335` n `758`
- 24h: commodity avg `0.0738` n `12`; crypto_alt avg `0.2556` n `232`; crypto_major avg `-0.4302` n `8`; equity avg `0.4517` n `134`; fx avg `0.0119` n `6`; index avg `0.003` n `26`; metal avg `-0.1805` n `20`; unknown avg `80.4243` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
