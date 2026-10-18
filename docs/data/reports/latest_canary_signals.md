# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T13:52:33.556872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.0057` n `237`; crypto_major avg `0.1805` n `8`; equity avg `-0.0032` n `151`; fx avg `-0.01` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.021` n `1193`
- 1h: commodity avg `0.0245` n `13`; crypto_alt avg `-0.6014` n `237`; crypto_major avg `-0.7081` n `8`; equity avg `-0.3596` n `151`; fx avg `-0.0029` n `6`; index avg `-0.0506` n `26`; metal avg `-0.0239` n `20`; unknown avg `-0.4643` n `1189`
- 4h: commodity avg `-0.0442` n `13`; crypto_alt avg `-0.8672` n `237`; crypto_major avg `-1.0091` n `8`; equity avg `-0.3942` n `151`; fx avg `-0.0028` n `6`; index avg `-0.0795` n `26`; metal avg `-0.0247` n `20`; unknown avg `3.6332` n `1183`
- 24h: commodity avg `0.0572` n `13`; crypto_alt avg `-2.4936` n `236`; crypto_major avg `-0.7542` n `8`; equity avg `-0.8368` n `151`; fx avg `-0.0443` n `6`; index avg `-0.111` n `26`; metal avg `-0.0585` n `20`; unknown avg `1.3186` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2075`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0814`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
