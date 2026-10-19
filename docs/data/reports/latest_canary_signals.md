# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T15:52:38.770316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0649` n `13`; crypto_alt avg `-0.1452` n `237`; crypto_major avg `-0.15` n `8`; equity avg `-0.0266` n `151`; fx avg `-0.0165` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0184` n `20`; unknown avg `-0.176` n `1196`
- 1h: commodity avg `0.108` n `13`; crypto_alt avg `-0.0506` n `237`; crypto_major avg `-0.2764` n `8`; equity avg `0.5326` n `151`; fx avg `-0.0039` n `6`; index avg `0.1313` n `26`; metal avg `0.0347` n `20`; unknown avg `2.2986` n `1193`
- 4h: commodity avg `-0.07` n `13`; crypto_alt avg `0.3384` n `237`; crypto_major avg `-0.3166` n `8`; equity avg `0.4341` n `151`; fx avg `0.0078` n `6`; index avg `0.1573` n `26`; metal avg `-0.157` n `20`; unknown avg `0.0872` n `1105`
- 24h: commodity avg `-0.2576` n `13`; crypto_alt avg `1.2699` n `237`; crypto_major avg `1.5214` n `8`; equity avg `3.7822` n `151`; fx avg `-0.034` n `6`; index avg `0.7217` n `26`; metal avg `0.1295` n `20`; unknown avg `5.3379` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2206`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
