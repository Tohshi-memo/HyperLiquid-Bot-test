# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T23:37:28.717400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `0.0384` n `233`; crypto_major avg `0.0118` n `8`; equity avg `-0.084` n `134`; fx avg `0.0101` n `6`; index avg `-0.0102` n `26`; metal avg `0.0215` n `20`; unknown avg `0.3265` n `797`
- 1h: commodity avg `0.0226` n `12`; crypto_alt avg `0.0674` n `233`; crypto_major avg `0.045` n `8`; equity avg `-0.0512` n `134`; fx avg `-0.0133` n `6`; index avg `0.0112` n `26`; metal avg `0.0208` n `20`; unknown avg `1.159` n `795`
- 4h: commodity avg `0.1722` n `12`; crypto_alt avg `-0.1954` n `233`; crypto_major avg `0.1248` n `8`; equity avg `-0.1611` n `134`; fx avg `-0.0316` n `6`; index avg `-0.0569` n `26`; metal avg `-0.0659` n `20`; unknown avg `0.4023` n `725`
- 24h: commodity avg `0.0674` n `12`; crypto_alt avg `-0.1463` n `232`; crypto_major avg `0.228` n `8`; equity avg `0.3763` n `134`; fx avg `-0.0993` n `6`; index avg `-0.1208` n `26`; metal avg `-0.3723` n `20`; unknown avg `6.3667` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
