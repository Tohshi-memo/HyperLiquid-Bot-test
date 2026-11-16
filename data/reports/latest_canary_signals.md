# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T20:52:26.482177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `13`; crypto_alt avg `0.2644` n `239`; crypto_major avg `0.3213` n `8`; equity avg `0.3642` n `162`; fx avg `-0.0017` n `6`; index avg `0.0279` n `27`; metal avg `0.008` n `20`; unknown avg `-0.168` n `1266`
- 1h: commodity avg `-0.0001` n `13`; crypto_alt avg `0.1346` n `239`; crypto_major avg `0.2258` n `8`; equity avg `-0.2719` n `162`; fx avg `-0.0141` n `6`; index avg `-0.0398` n `27`; metal avg `-0.0798` n `20`; unknown avg `168.8641` n `1256`
- 4h: commodity avg `-0.2397` n `13`; crypto_alt avg `0.4345` n `239`; crypto_major avg `0.5984` n `8`; equity avg `-0.7695` n `162`; fx avg `-0.031` n `6`; index avg `-0.1442` n `27`; metal avg `-0.0769` n `20`; unknown avg `7.4506` n `1253`
- 24h: commodity avg `-1.1273` n `13`; crypto_alt avg `-0.1429` n `239`; crypto_major avg `0.0082` n `8`; equity avg `-3.1405` n `162`; fx avg `-0.1218` n `6`; index avg `-0.3254` n `27`; metal avg `-0.3865` n `20`; unknown avg `251.7894` n `1039`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
