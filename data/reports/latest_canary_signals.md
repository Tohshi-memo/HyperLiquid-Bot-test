# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T11:07:35.288536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.0227` n `232`; crypto_major avg `-0.0136` n `8`; equity avg `0.0` n `134`; fx avg `-0.0011` n `6`; index avg `0.0074` n `26`; metal avg `-0.0011` n `20`; unknown avg `161.2692` n `792`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.3366` n `232`; crypto_major avg `0.0045` n `8`; equity avg `0.0642` n `134`; fx avg `0.0087` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0111` n `20`; unknown avg `161.9505` n `792`
- 4h: commodity avg `-0.0007` n `12`; crypto_alt avg `0.4914` n `232`; crypto_major avg `0.0927` n `8`; equity avg `0.1362` n `134`; fx avg `0.0199` n `6`; index avg `0.0122` n `26`; metal avg `-0.0156` n `20`; unknown avg `325.9761` n `784`
- 24h: commodity avg `0.1563` n `12`; crypto_alt avg `2.1386` n `232`; crypto_major avg `2.0585` n `8`; equity avg `0.5499` n `134`; fx avg `-0.0178` n `6`; index avg `0.0815` n `26`; metal avg `0.0039` n `20`; unknown avg `492.4954` n `677`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
