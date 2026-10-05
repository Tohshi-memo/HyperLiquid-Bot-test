# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T10:22:28.646347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0378` n `13`; crypto_alt avg `-0.0016` n `235`; crypto_major avg `-0.0319` n `8`; equity avg `-0.013` n `144`; fx avg `0.0034` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0203` n `20`; unknown avg `0.0196` n `1079`
- 1h: commodity avg `-0.0044` n `13`; crypto_alt avg `0.0345` n `235`; crypto_major avg `0.0025` n `8`; equity avg `-0.1054` n `144`; fx avg `-0.0034` n `6`; index avg `-0.0312` n `26`; metal avg `-0.1283` n `20`; unknown avg `38.3092` n `1077`
- 4h: commodity avg `0.2473` n `13`; crypto_alt avg `0.363` n `235`; crypto_major avg `0.2575` n `8`; equity avg `-0.1985` n `144`; fx avg `0.055` n `6`; index avg `-0.0465` n `26`; metal avg `0.0366` n `20`; unknown avg `5.724` n `997`
- 24h: commodity avg `-0.0609` n `13`; crypto_alt avg `0.9307` n `235`; crypto_major avg `0.8296` n `8`; equity avg `0.1044` n `144`; fx avg `-0.0371` n `6`; index avg `-0.0902` n `26`; metal avg `0.2263` n `20`; unknown avg `0.8013` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
