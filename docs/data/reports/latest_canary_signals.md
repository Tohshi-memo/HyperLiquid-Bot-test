# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T10:22:30.063460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0673` n `13`; crypto_alt avg `-0.083` n `235`; crypto_major avg `-0.0955` n `8`; equity avg `-0.0987` n `150`; fx avg `-0.0024` n `6`; index avg `-0.0305` n `26`; metal avg `-0.0362` n `20`; unknown avg `0.1034` n `1077`
- 1h: commodity avg `0.1068` n `13`; crypto_alt avg `0.3985` n `235`; crypto_major avg `0.1007` n `8`; equity avg `-0.0779` n `150`; fx avg `-0.0081` n `6`; index avg `-0.0223` n `26`; metal avg `-0.0347` n `20`; unknown avg `1.3722` n `1075`
- 4h: commodity avg `0.5343` n `13`; crypto_alt avg `1.0381` n `235`; crypto_major avg `0.3174` n `8`; equity avg `-0.4064` n `150`; fx avg `0.0575` n `6`; index avg `-0.0977` n `26`; metal avg `-0.0664` n `20`; unknown avg `1.3734` n `1059`
- 24h: commodity avg `0.8414` n `13`; crypto_alt avg `0.4501` n `235`; crypto_major avg `-1.5492` n `8`; equity avg `-1.4967` n `150`; fx avg `0.0202` n `6`; index avg `-0.2802` n `26`; metal avg `-0.0763` n `20`; unknown avg `416.4797` n `974`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
