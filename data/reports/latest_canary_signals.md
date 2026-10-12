# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T20:52:29.357641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `0.0937` n `235`; crypto_major avg `0.0702` n `8`; equity avg `0.024` n `151`; fx avg `0.0013` n `6`; index avg `0.017` n `26`; metal avg `0.0117` n `20`; unknown avg `0.3821` n `1134`
- 1h: commodity avg `-0.1297` n `13`; crypto_alt avg `0.1223` n `235`; crypto_major avg `0.1886` n `8`; equity avg `0.029` n `151`; fx avg `-0.006` n `6`; index avg `-0.0021` n `26`; metal avg `0.0263` n `20`; unknown avg `5.81` n `1106`
- 4h: commodity avg `-0.2222` n `13`; crypto_alt avg `0.3565` n `235`; crypto_major avg `0.2465` n `8`; equity avg `0.0959` n `151`; fx avg `-0.0052` n `6`; index avg `-0.01` n `26`; metal avg `0.0635` n `20`; unknown avg `1.2316` n `1106`
- 24h: commodity avg `0.169` n `13`; crypto_alt avg `-2.7393` n `235`; crypto_major avg `-1.5167` n `8`; equity avg `-3.3704` n `151`; fx avg `-0.1786` n `6`; index avg `-0.3396` n `26`; metal avg `-0.1556` n `20`; unknown avg `0.3257` n `869`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2079`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1732`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1203`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.096`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0887`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `666`, weak_sample_signal
