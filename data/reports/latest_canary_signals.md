# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T13:22:31.068204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0691` n `13`; crypto_alt avg `0.3461` n `235`; crypto_major avg `0.3236` n `8`; equity avg `0.1222` n `150`; fx avg `-0.0175` n `6`; index avg `0.0215` n `26`; metal avg `-0.0282` n `20`; unknown avg `1.8428` n `1077`
- 1h: commodity avg `-0.1628` n `13`; crypto_alt avg `-0.0094` n `235`; crypto_major avg `0.1487` n `8`; equity avg `0.2177` n `150`; fx avg `-0.0206` n `6`; index avg `0.044` n `26`; metal avg `-0.0576` n `20`; unknown avg `0.5629` n `1075`
- 4h: commodity avg `0.0262` n `13`; crypto_alt avg `-0.6104` n `235`; crypto_major avg `-0.8662` n `8`; equity avg `-0.0701` n `150`; fx avg `-0.0107` n `6`; index avg `0.0362` n `26`; metal avg `-0.124` n `20`; unknown avg `2.0675` n `1069`
- 24h: commodity avg `0.6882` n `13`; crypto_alt avg `0.5638` n `235`; crypto_major avg `-1.6551` n `8`; equity avg `-0.9569` n `150`; fx avg `0.0406` n `6`; index avg `-0.109` n `26`; metal avg `0.0103` n `20`; unknown avg `416.7238` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
