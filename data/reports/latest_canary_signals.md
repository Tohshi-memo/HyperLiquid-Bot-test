# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T09:37:29.312719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `0.1105` n `231`; crypto_major avg `0.1798` n `8`; equity avg `0.1198` n `122`; fx avg `-0.026` n `6`; index avg `0.0147` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.0429` n `793`
- 1h: commodity avg `0.0172` n `12`; crypto_alt avg `0.8555` n `231`; crypto_major avg `0.8158` n `8`; equity avg `0.2116` n `122`; fx avg `-0.061` n `6`; index avg `0.0247` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.6926` n `793`
- 4h: commodity avg `0.0981` n `12`; crypto_alt avg `0.1598` n `231`; crypto_major avg `0.1343` n `8`; equity avg `0.1233` n `122`; fx avg `0.0244` n `6`; index avg `0.0184` n `25`; metal avg `0.0214` n `20`; unknown avg `0.3794` n `777`
- 24h: commodity avg `-0.1792` n `12`; crypto_alt avg `2.3295` n `231`; crypto_major avg `0.8319` n `8`; equity avg `-1.1829` n `122`; fx avg `-0.1656` n `6`; index avg `-0.0989` n `25`; metal avg `0.1177` n `20`; unknown avg `5.477` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
