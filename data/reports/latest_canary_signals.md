# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T10:52:32.650679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.1677` n `232`; crypto_major avg `0.2354` n `8`; equity avg `0.0643` n `133`; fx avg `-0.0175` n `6`; index avg `0.0117` n `26`; metal avg `0.0462` n `20`; unknown avg `0.4146` n `792`
- 1h: commodity avg `0.2162` n `12`; crypto_alt avg `-0.0251` n `232`; crypto_major avg `-0.0093` n `8`; equity avg `-0.1221` n `133`; fx avg `-0.0054` n `6`; index avg `-0.0329` n `26`; metal avg `-0.0324` n `20`; unknown avg `-0.2147` n `790`
- 4h: commodity avg `0.4841` n `12`; crypto_alt avg `0.0265` n `232`; crypto_major avg `-0.1839` n `8`; equity avg `-0.2082` n `133`; fx avg `-0.0598` n `6`; index avg `-0.0668` n `26`; metal avg `0.0055` n `20`; unknown avg `0.1068` n `790`
- 24h: commodity avg `0.5337` n `12`; crypto_alt avg `2.2788` n `232`; crypto_major avg `2.0541` n `8`; equity avg `1.628` n `133`; fx avg `-0.4043` n `6`; index avg `0.1499` n `26`; metal avg `0.8589` n `20`; unknown avg `-0.2157` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0413`, n `668`, weak_sample_signal
