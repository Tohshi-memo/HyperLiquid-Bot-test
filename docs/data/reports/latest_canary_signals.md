# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T09:52:26.925639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.0812` n `232`; crypto_major avg `-0.0792` n `8`; equity avg `-0.007` n `134`; fx avg `0.0034` n `6`; index avg `0.0001` n `26`; metal avg `-0.003` n `20`; unknown avg `0.0453` n `796`
- 1h: commodity avg `0.0255` n `12`; crypto_alt avg `0.1287` n `232`; crypto_major avg `0.0195` n `8`; equity avg `-0.0171` n `134`; fx avg `0.0043` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0115` n `20`; unknown avg `-0.0734` n `790`
- 4h: commodity avg `-0.212` n `12`; crypto_alt avg `-0.074` n `232`; crypto_major avg `-0.4448` n `8`; equity avg `-0.0013` n `134`; fx avg `-0.123` n `6`; index avg `0.0223` n `26`; metal avg `0.1012` n `20`; unknown avg `1.1568` n `758`
- 24h: commodity avg `-0.0777` n `12`; crypto_alt avg `0.1496` n `232`; crypto_major avg `-0.8783` n `8`; equity avg `0.3697` n `134`; fx avg `-0.1253` n `6`; index avg `0.0366` n `26`; metal avg `-0.0752` n `20`; unknown avg `75.4425` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
