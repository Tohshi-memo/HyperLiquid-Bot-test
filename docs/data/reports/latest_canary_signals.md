# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T21:37:26.895566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.0144` n `235`; crypto_major avg `-0.012` n `8`; equity avg `0.0086` n `143`; fx avg `0.0066` n `6`; index avg `0.0041` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.0103` n `1079`
- 1h: commodity avg `0.1006` n `13`; crypto_alt avg `-0.2313` n `235`; crypto_major avg `-0.1538` n `8`; equity avg `-0.0087` n `143`; fx avg `0.0102` n `6`; index avg `0.0032` n `26`; metal avg `0.0006` n `20`; unknown avg `-0.2145` n `1077`
- 4h: commodity avg `0.2198` n `13`; crypto_alt avg `0.0722` n `235`; crypto_major avg `-0.1187` n `8`; equity avg `0.0593` n `143`; fx avg `0.0096` n `6`; index avg `0.0125` n `26`; metal avg `0.0102` n `20`; unknown avg `-0.0638` n `1062`
- 24h: commodity avg `0.0091` n `13`; crypto_alt avg `2.861` n `235`; crypto_major avg `1.3706` n `8`; equity avg `0.2042` n `143`; fx avg `-0.0184` n `6`; index avg `0.0435` n `26`; metal avg `-0.0117` n `20`; unknown avg `-0.5183` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
