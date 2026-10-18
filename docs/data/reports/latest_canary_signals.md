# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T19:07:47.736850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `13`; crypto_alt avg `-0.0655` n `237`; crypto_major avg `0.0256` n `8`; equity avg `-0.0131` n `151`; fx avg `0.0035` n `6`; index avg `0.008` n `26`; metal avg `0.0044` n `20`; unknown avg `2.5991` n `1184`
- 1h: commodity avg `0.0053` n `13`; crypto_alt avg `-0.0986` n `237`; crypto_major avg `0.0156` n `8`; equity avg `0.0079` n `151`; fx avg `0.005` n `6`; index avg `-0.0069` n `26`; metal avg `0.0064` n `20`; unknown avg `2.2753` n `1174`
- 4h: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.7643` n `237`; crypto_major avg `-0.2213` n `8`; equity avg `-0.2356` n `151`; fx avg `0.0132` n `6`; index avg `-0.0431` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.5071` n `1143`
- 24h: commodity avg `-0.0234` n `13`; crypto_alt avg `-3.6244` n `236`; crypto_major avg `-1.2715` n `8`; equity avg `-1.1028` n `151`; fx avg `0.0089` n `6`; index avg `-0.153` n `26`; metal avg `-0.0335` n `20`; unknown avg `0.7998` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2106`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1406`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1338`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
