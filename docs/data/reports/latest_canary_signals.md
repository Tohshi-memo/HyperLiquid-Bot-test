# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T13:07:26.370332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `0.2109` n `237`; crypto_major avg `0.0012` n `8`; equity avg `-0.0911` n `151`; fx avg `-0.0005` n `6`; index avg `-0.004` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.2168` n `1191`
- 1h: commodity avg `-0.0302` n `13`; crypto_alt avg `0.152` n `237`; crypto_major avg `-0.2998` n `8`; equity avg `-0.0787` n `151`; fx avg `-0.0016` n `6`; index avg `-0.019` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.2781` n `1191`
- 4h: commodity avg `0.0125` n `13`; crypto_alt avg `0.2916` n `237`; crypto_major avg `-0.0674` n `8`; equity avg `-0.0959` n `151`; fx avg `0.0125` n `6`; index avg `-0.0084` n `26`; metal avg `0.0156` n `20`; unknown avg `3.8717` n `1153`
- 24h: commodity avg `0.0597` n `13`; crypto_alt avg `-1.6936` n `236`; crypto_major avg `0.0111` n `8`; equity avg `-0.5466` n `151`; fx avg `-0.0478` n `6`; index avg `-0.0596` n `26`; metal avg `-0.0238` n `20`; unknown avg `1.6244` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.208`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1321`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
