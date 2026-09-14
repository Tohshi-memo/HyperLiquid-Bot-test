# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T05:07:28.402885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.0115` n `233`; crypto_major avg `-0.0561` n `8`; equity avg `-0.0021` n `136`; fx avg `0.0102` n `6`; index avg `-0.0016` n `27`; metal avg `0.0442` n `20`; unknown avg `1.334` n `892`
- 1h: commodity avg `-0.0757` n `12`; crypto_alt avg `0.0466` n `233`; crypto_major avg `0.0645` n `8`; equity avg `-0.0487` n `136`; fx avg `-0.0046` n `6`; index avg `-0.0246` n `27`; metal avg `0.0293` n `20`; unknown avg `1.1161` n `886`
- 4h: commodity avg `-0.176` n `12`; crypto_alt avg `1.3536` n `233`; crypto_major avg `1.4669` n `8`; equity avg `0.3291` n `136`; fx avg `-0.03` n `6`; index avg `0.027` n `27`; metal avg `0.063` n `20`; unknown avg `11.6923` n `880`
- 24h: commodity avg `0.5958` n `12`; crypto_alt avg `-0.5282` n `233`; crypto_major avg `0.0383` n `8`; equity avg `-1.386` n `136`; fx avg `0.0326` n `6`; index avg `-0.3254` n `26`; metal avg `-0.1289` n `20`; unknown avg `1.7159` n `676`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
