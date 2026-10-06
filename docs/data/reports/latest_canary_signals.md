# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T09:52:29.744658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0379` n `13`; crypto_alt avg `0.1855` n `235`; crypto_major avg `0.1341` n `8`; equity avg `-0.0184` n `150`; fx avg `0.0007` n `6`; index avg `-0.0056` n `26`; metal avg `-0.047` n `20`; unknown avg `-0.0237` n `1074`
- 1h: commodity avg `-0.157` n `13`; crypto_alt avg `0.0349` n `235`; crypto_major avg `-0.0576` n `8`; equity avg `0.072` n `149`; fx avg `0.012` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0145` n `20`; unknown avg `-0.1876` n `1072`
- 4h: commodity avg `-0.5442` n `13`; crypto_alt avg `0.3836` n `235`; crypto_major avg `0.2189` n `8`; equity avg `0.1826` n `149`; fx avg `0.0433` n `6`; index avg `0.0418` n `26`; metal avg `0.1231` n `20`; unknown avg `-0.1168` n `976`
- 24h: commodity avg `-0.7023` n `13`; crypto_alt avg `-0.7821` n `235`; crypto_major avg `-0.4363` n `8`; equity avg `0.5444` n `149`; fx avg `0.0439` n `6`; index avg `0.2193` n `26`; metal avg `-0.1293` n `20`; unknown avg `-0.1223` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
