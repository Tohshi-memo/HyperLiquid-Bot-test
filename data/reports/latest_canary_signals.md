# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T17:37:32.887153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0826` n `12`; crypto_alt avg `-0.1067` n `230`; crypto_major avg `-0.061` n `8`; equity avg `-0.0918` n `98`; fx avg `-0.0025` n `6`; index avg `-0.0155` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0047` n `770`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `-0.185` n `8`; equity avg `-0.3403` n `98`; fx avg `-0.0084` n `6`; index avg `-0.0746` n `25`; metal avg `-0.0219` n `20`; unknown avg `0.1079` n `770`
- 4h: commodity avg `0.1644` n `12`; crypto_alt avg `0.5743` n `230`; crypto_major avg `0.767` n `8`; equity avg `-0.5583` n `98`; fx avg `-0.0795` n `6`; index avg `-0.1677` n `25`; metal avg `0.0503` n `20`; unknown avg `0.0514` n `770`
- 24h: commodity avg `-0.4134` n `12`; crypto_alt avg `1.5956` n `230`; crypto_major avg `1.1489` n `8`; equity avg `0.5119` n `98`; fx avg `-0.157` n `6`; index avg `0.1756` n `25`; metal avg `0.2016` n `20`; unknown avg `0.2921` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0878`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0846`, n `666`, weak_sample_signal
