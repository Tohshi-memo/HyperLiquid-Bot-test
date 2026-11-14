# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T13:52:26.036662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `0.009` n `239`; crypto_major avg `0.0851` n `8`; equity avg `0.0557` n `162`; fx avg `0.0045` n `6`; index avg `0.0029` n `27`; metal avg `0.0173` n `20`; unknown avg `158.5465` n `1262`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `-0.3038` n `239`; crypto_major avg `-0.3352` n `8`; equity avg `-0.1063` n `162`; fx avg `0.0031` n `6`; index avg `-0.0064` n `27`; metal avg `0.0057` n `20`; unknown avg `0.376` n `1260`
- 4h: commodity avg `-0.024` n `13`; crypto_alt avg `-1.0804` n `239`; crypto_major avg `-0.8962` n `8`; equity avg `-0.2123` n `162`; fx avg `0.019` n `6`; index avg `-0.0199` n `27`; metal avg `-0.0001` n `20`; unknown avg `80.5984` n `1238`
- 24h: commodity avg `-0.3161` n `13`; crypto_alt avg `-4.8929` n `239`; crypto_major avg `-4.9007` n `8`; equity avg `-3.1506` n `162`; fx avg `-0.1332` n `6`; index avg `-0.2615` n `27`; metal avg `-0.3051` n `20`; unknown avg `0.4848` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
