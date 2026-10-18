# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T18:37:28.382916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.0532` n `237`; crypto_major avg `-0.0537` n `8`; equity avg `-0.0177` n `151`; fx avg `0.0029` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0008` n `20`; unknown avg `1.4702` n `1186`
- 1h: commodity avg `-0.016` n `13`; crypto_alt avg `-0.3067` n `237`; crypto_major avg `-0.2067` n `8`; equity avg `-0.0084` n `151`; fx avg `0.0114` n `6`; index avg `-0.0096` n `26`; metal avg `0.0037` n `20`; unknown avg `0.8848` n `1180`
- 4h: commodity avg `-0.0063` n `13`; crypto_alt avg `-0.4517` n `237`; crypto_major avg `-0.2727` n `8`; equity avg `-0.197` n `151`; fx avg `0.0214` n `6`; index avg `-0.0546` n `26`; metal avg `0.0063` n `20`; unknown avg `-0.7464` n `1151`
- 24h: commodity avg `-0.0343` n `13`; crypto_alt avg `-3.5808` n `236`; crypto_major avg `-1.5244` n `8`; equity avg `-1.0631` n `151`; fx avg `0.0085` n `6`; index avg `-0.15` n `26`; metal avg `-0.047` n `20`; unknown avg `0.4415` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1321`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
