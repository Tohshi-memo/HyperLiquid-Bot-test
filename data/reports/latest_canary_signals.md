# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T08:07:31.155670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `13`; crypto_alt avg `-0.0984` n `239`; crypto_major avg `-0.0151` n `8`; equity avg `0.0628` n `162`; fx avg `-0.0156` n `6`; index avg `0.0051` n `27`; metal avg `-0.0927` n `20`; unknown avg `0.1339` n `1238`
- 1h: commodity avg `0.098` n `13`; crypto_alt avg `-0.0414` n `239`; crypto_major avg `-0.0796` n `8`; equity avg `0.0564` n `162`; fx avg `-0.0166` n `6`; index avg `0.0002` n `27`; metal avg `-0.1219` n `20`; unknown avg `0.448` n `1222`
- 4h: commodity avg `0.1746` n `13`; crypto_alt avg `-0.19` n `239`; crypto_major avg `-0.2675` n `8`; equity avg `-0.4445` n `162`; fx avg `-0.031` n `6`; index avg `0.0005` n `27`; metal avg `-0.0755` n `20`; unknown avg `-0.0241` n `1172`
- 24h: commodity avg `-1.049` n `13`; crypto_alt avg `0.9357` n `239`; crypto_major avg `1.1828` n `8`; equity avg `-2.5611` n `162`; fx avg `-0.0417` n `6`; index avg `-0.2756` n `27`; metal avg `-0.1202` n `20`; unknown avg `39.0799` n `1115`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
