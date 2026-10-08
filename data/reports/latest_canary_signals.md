# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T13:52:26.993114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5672` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0362` n `13`; crypto_alt avg `0.0871` n `235`; crypto_major avg `0.0055` n `8`; equity avg `-0.1168` n `150`; fx avg `0.008` n `6`; index avg `0.0146` n `26`; metal avg `0.0354` n `20`; unknown avg `0.0604` n `1077`
- 1h: commodity avg `-0.0841` n `13`; crypto_alt avg `0.2687` n `235`; crypto_major avg `-0.0288` n `8`; equity avg `-0.1596` n `150`; fx avg `0.008` n `6`; index avg `0.0472` n `26`; metal avg `0.0719` n `20`; unknown avg `20.0837` n `1073`
- 4h: commodity avg `0.0171` n `13`; crypto_alt avg `-1.4239` n `235`; crypto_major avg `-1.5514` n `8`; equity avg `-0.5754` n `150`; fx avg `0.0225` n `6`; index avg `0.0158` n `26`; metal avg `-0.0537` n `20`; unknown avg `2.5376` n `1067`
- 24h: commodity avg `0.6354` n `13`; crypto_alt avg `0.1641` n `235`; crypto_major avg `-2.2747` n `8`; equity avg `-1.2614` n `150`; fx avg `0.0585` n `6`; index avg `-0.0446` n `26`; metal avg `0.1377` n `20`; unknown avg `0.2217` n `970`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
