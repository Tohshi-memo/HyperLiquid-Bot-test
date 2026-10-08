# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T22:22:32.393862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `13`; crypto_alt avg `0.0526` n `235`; crypto_major avg `0.0394` n `8`; equity avg `0.0929` n `150`; fx avg `0.0075` n `6`; index avg `0.0258` n `26`; metal avg `0.0329` n `20`; unknown avg `-0.1248` n `1077`
- 1h: commodity avg `-0.0356` n `13`; crypto_alt avg `0.0777` n `235`; crypto_major avg `0.0533` n `8`; equity avg `0.1612` n `150`; fx avg `0.0052` n `6`; index avg `0.027` n `26`; metal avg `0.0306` n `20`; unknown avg `-0.0133` n `1075`
- 4h: commodity avg `-0.278` n `13`; crypto_alt avg `1.6494` n `235`; crypto_major avg `1.2872` n `8`; equity avg `0.3512` n `150`; fx avg `0.0224` n `6`; index avg `0.0735` n `26`; metal avg `0.0807` n `20`; unknown avg `0.1024` n `1007`
- 24h: commodity avg `0.5261` n `13`; crypto_alt avg `-2.6172` n `235`; crypto_major avg `-3.1579` n `8`; equity avg `-2.6178` n `150`; fx avg `0.0604` n `6`; index avg `-0.347` n `26`; metal avg `0.0373` n `20`; unknown avg `6.1976` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
