# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T11:22:29.177546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0463` n `13`; crypto_alt avg `0.1215` n `239`; crypto_major avg `0.1585` n `8`; equity avg `-0.0377` n `164`; fx avg `-0.0194` n `6`; index avg `-0.0201` n `27`; metal avg `-0.0252` n `20`; unknown avg `0.4218` n `1264`
- 1h: commodity avg `-0.0692` n `13`; crypto_alt avg `-0.003` n `239`; crypto_major avg `0.0034` n `8`; equity avg `0.0719` n `164`; fx avg `0.0201` n `6`; index avg `-0.0356` n `27`; metal avg `-0.0684` n `20`; unknown avg `0.1654` n `1264`
- 4h: commodity avg `-0.0456` n `13`; crypto_alt avg `0.1604` n `239`; crypto_major avg `0.0899` n `8`; equity avg `0.3908` n `164`; fx avg `0.076` n `6`; index avg `0.1047` n `27`; metal avg `-0.1162` n `20`; unknown avg `306.3725` n `1222`
- 24h: commodity avg `0.0552` n `13`; crypto_alt avg `0.2777` n `239`; crypto_major avg `-0.0101` n `8`; equity avg `0.7369` n `164`; fx avg `0.048` n `6`; index avg `0.2548` n `27`; metal avg `-0.1703` n `20`; unknown avg `1.7343` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
