# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T04:37:32.742033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `-0.0009` n `235`; crypto_major avg `0.0184` n `8`; equity avg `0.0065` n `143`; fx avg `0.0` n `6`; index avg `-0.0024` n `26`; metal avg `0.0036` n `20`; unknown avg `3.0036` n `1079`
- 1h: commodity avg `-0.0187` n `13`; crypto_alt avg `0.2476` n `235`; crypto_major avg `-0.0151` n `8`; equity avg `0.0056` n `143`; fx avg `0.0002` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0021` n `20`; unknown avg `1.593` n `1071`
- 4h: commodity avg `-0.0762` n `13`; crypto_alt avg `0.2593` n `235`; crypto_major avg `0.0514` n `8`; equity avg `0.0211` n `143`; fx avg `-0.0021` n `6`; index avg `-0.0104` n `26`; metal avg `0.0121` n `20`; unknown avg `-0.2332` n `1071`
- 24h: commodity avg `0.0996` n `13`; crypto_alt avg `1.9752` n `235`; crypto_major avg `0.9555` n `8`; equity avg `0.2606` n `143`; fx avg `-0.0283` n `6`; index avg `0.016` n `26`; metal avg `0.0125` n `20`; unknown avg `0.1331` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1988`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
