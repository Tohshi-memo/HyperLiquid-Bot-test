# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T09:22:28.115190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `-0.1213` n `235`; crypto_major avg `-0.0885` n `8`; equity avg `-0.0666` n `150`; fx avg `0.0083` n `6`; index avg `-0.0143` n `26`; metal avg `-0.0565` n `20`; unknown avg `-0.0322` n `1077`
- 1h: commodity avg `0.0143` n `13`; crypto_alt avg `0.0795` n `235`; crypto_major avg `0.0024` n `8`; equity avg `-0.0995` n `150`; fx avg `0.0253` n `6`; index avg `-0.0286` n `26`; metal avg `-0.0497` n `20`; unknown avg `-0.0792` n `1075`
- 4h: commodity avg `0.4496` n `13`; crypto_alt avg `0.0315` n `235`; crypto_major avg `-0.1975` n `8`; equity avg `-0.874` n `150`; fx avg `0.0351` n `6`; index avg `-0.1887` n `26`; metal avg `-0.1855` n `20`; unknown avg `0.2732` n `1031`
- 24h: commodity avg `0.7974` n `13`; crypto_alt avg `-0.1003` n `235`; crypto_major avg `-1.8304` n `8`; equity avg `-1.4364` n `150`; fx avg `0.0061` n `6`; index avg `-0.2857` n `26`; metal avg `-0.0806` n `20`; unknown avg `416.6519` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
