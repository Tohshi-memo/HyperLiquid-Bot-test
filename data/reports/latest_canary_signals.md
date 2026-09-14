# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T05:37:29.435463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6171` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0467` n `12`; crypto_alt avg `0.1158` n `233`; crypto_major avg `0.0494` n `8`; equity avg `0.0128` n `136`; fx avg `0.0123` n `6`; index avg `0.0161` n `27`; metal avg `0.0273` n `20`; unknown avg `2.4968` n `894`
- 1h: commodity avg `-0.0672` n `12`; crypto_alt avg `-0.0416` n `233`; crypto_major avg `-0.0086` n `8`; equity avg `-0.0864` n `136`; fx avg `0.0065` n `6`; index avg `-0.0001` n `27`; metal avg `0.0336` n `20`; unknown avg `1.5593` n `892`
- 4h: commodity avg `-0.105` n `12`; crypto_alt avg `1.3859` n `233`; crypto_major avg `1.6025` n `8`; equity avg `0.2352` n `136`; fx avg `-0.0128` n `6`; index avg `0.0274` n `27`; metal avg `-0.0146` n `20`; unknown avg `11.1953` n `880`
- 24h: commodity avg `0.5661` n `12`; crypto_alt avg `-0.6087` n `233`; crypto_major avg `-0.0441` n `8`; equity avg `-1.4345` n `136`; fx avg `0.0423` n `6`; index avg `-0.3129` n `26`; metal avg `-0.1272` n `20`; unknown avg `2.2512` n `676`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
