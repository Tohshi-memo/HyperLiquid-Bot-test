# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T16:52:31.822775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `0.0051` n `237`; crypto_major avg `-0.0168` n `8`; equity avg `-0.2114` n `151`; fx avg `-0.0042` n `6`; index avg `-0.0317` n `26`; metal avg `-0.0317` n `20`; unknown avg `0.1005` n `1196`
- 1h: commodity avg `0.1357` n `13`; crypto_alt avg `0.2874` n `237`; crypto_major avg `0.0446` n `8`; equity avg `-0.8029` n `151`; fx avg `-0.0007` n `6`; index avg `-0.1429` n `26`; metal avg `-0.0468` n `20`; unknown avg `0.1451` n `1188`
- 4h: commodity avg `0.1025` n `13`; crypto_alt avg `0.0574` n `237`; crypto_major avg `-0.6205` n `8`; equity avg `-0.5605` n `151`; fx avg `-0.0014` n `6`; index avg `-0.0111` n `26`; metal avg `-0.1069` n `20`; unknown avg `0.3639` n `1121`
- 24h: commodity avg `-0.1362` n `13`; crypto_alt avg `1.6948` n `237`; crypto_major avg `1.7044` n `8`; equity avg `2.9164` n `151`; fx avg `-0.0312` n `6`; index avg `0.5546` n `26`; metal avg `0.0829` n `20`; unknown avg `3.3035` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2024`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
