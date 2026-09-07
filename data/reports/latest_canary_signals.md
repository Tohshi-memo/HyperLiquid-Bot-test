# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T08:07:27.777889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0659` n `12`; crypto_alt avg `0.1805` n `232`; crypto_major avg `0.0851` n `8`; equity avg `0.0466` n `134`; fx avg `-0.0392` n `6`; index avg `0.0014` n `26`; metal avg `0.0565` n `20`; unknown avg `0.0225` n `794`
- 1h: commodity avg `-0.1192` n `12`; crypto_alt avg `-0.4916` n `232`; crypto_major avg `-0.3972` n `8`; equity avg `-0.0951` n `134`; fx avg `-0.0316` n `6`; index avg `-0.0104` n `26`; metal avg `0.108` n `20`; unknown avg `0.0358` n `794`
- 4h: commodity avg `-0.1398` n `12`; crypto_alt avg `-0.1361` n `232`; crypto_major avg `-0.1423` n `8`; equity avg `-0.0082` n `134`; fx avg `-0.0675` n `6`; index avg `0.0633` n `26`; metal avg `0.1396` n `20`; unknown avg `0.3255` n `758`
- 24h: commodity avg `-0.0941` n `12`; crypto_alt avg `-0.0972` n `232`; crypto_major avg `-0.7518` n `8`; equity avg `0.4026` n `134`; fx avg `-0.0667` n `6`; index avg `0.0636` n `26`; metal avg `-0.0339` n `20`; unknown avg `382.8059` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
