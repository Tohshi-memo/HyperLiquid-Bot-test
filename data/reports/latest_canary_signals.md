# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T00:52:26.742635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0799` n `13`; crypto_alt avg `0.0591` n `235`; crypto_major avg `-0.0086` n `8`; equity avg `-0.0153` n `143`; fx avg `-0.0014` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.4724` n `984`
- 1h: commodity avg `-0.0357` n `13`; crypto_alt avg `0.3534` n `235`; crypto_major avg `0.252` n `8`; equity avg `-0.012` n `143`; fx avg `0.0053` n `6`; index avg `0.0098` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.321` n `976`
- 4h: commodity avg `0.0461` n `13`; crypto_alt avg `1.7898` n `235`; crypto_major avg `1.1179` n `8`; equity avg `0.0881` n `143`; fx avg `0.0041` n `6`; index avg `0.0092` n `26`; metal avg `0.0393` n `20`; unknown avg `1.3768` n `958`
- 24h: commodity avg `0.1131` n `13`; crypto_alt avg `-0.1369` n `235`; crypto_major avg `-0.1548` n `8`; equity avg `0.6128` n `142`; fx avg `-0.1861` n `6`; index avg `0.2624` n `26`; metal avg `-0.1406` n `20`; unknown avg `-0.5767` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
