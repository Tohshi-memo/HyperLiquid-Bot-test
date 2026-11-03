# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T17:47:26.009505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0483` n `13`; crypto_alt avg `0.0185` n `239`; crypto_major avg `0.1123` n `8`; equity avg `-0.0266` n `158`; fx avg `0.0` n `6`; index avg `0.0115` n `27`; metal avg `0.0281` n `20`; unknown avg `0.1417` n `1261`
- 1h: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.1157` n `239`; crypto_major avg `-0.0008` n `8`; equity avg `0.1404` n `158`; fx avg `0.0068` n `6`; index avg `0.0102` n `27`; metal avg `0.007` n `20`; unknown avg `0.0129` n `1257`
- 4h: commodity avg `0.3412` n `13`; crypto_alt avg `-0.113` n `239`; crypto_major avg `0.2654` n `8`; equity avg `0.2464` n `158`; fx avg `0.0856` n `6`; index avg `-0.0394` n `27`; metal avg `-0.3501` n `20`; unknown avg `447.8161` n `1251`
- 24h: commodity avg `0.1396` n `13`; crypto_alt avg `0.9949` n `239`; crypto_major avg `1.6465` n `8`; equity avg `0.2102` n `158`; fx avg `0.0578` n `6`; index avg `-0.0026` n `27`; metal avg `-0.5378` n `20`; unknown avg `0.3655` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
