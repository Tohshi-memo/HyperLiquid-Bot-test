# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T00:37:38.692459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `13`; crypto_alt avg `0.0913` n `235`; crypto_major avg `0.1384` n `8`; equity avg `-0.0056` n `143`; fx avg `0.0029` n `6`; index avg `-0.0011` n `26`; metal avg `0.0001` n `20`; unknown avg `0.4645` n `984`
- 1h: commodity avg `0.0217` n `13`; crypto_alt avg `0.4558` n `235`; crypto_major avg `0.2816` n `8`; equity avg `0.0066` n `143`; fx avg `0.0036` n `6`; index avg `0.0126` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.4383` n `976`
- 4h: commodity avg `0.1122` n `13`; crypto_alt avg `1.5067` n `235`; crypto_major avg `1.0415` n `8`; equity avg `0.0634` n `143`; fx avg `-0.0011` n `6`; index avg `-0.004` n `26`; metal avg `0.001` n `20`; unknown avg `1.7271` n `958`
- 24h: commodity avg `0.1367` n `13`; crypto_alt avg `-0.1797` n `235`; crypto_major avg `0.0443` n `8`; equity avg `0.6182` n `142`; fx avg `-0.196` n `6`; index avg `0.2677` n `26`; metal avg `-0.1496` n `20`; unknown avg `-0.5779` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
