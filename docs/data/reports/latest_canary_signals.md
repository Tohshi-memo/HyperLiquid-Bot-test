# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T01:22:27.333368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `13`; crypto_alt avg `-0.1611` n `237`; crypto_major avg `-0.0994` n `8`; equity avg `-0.0867` n `151`; fx avg `-0.0011` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.1241` n `1193`
- 1h: commodity avg `0.0067` n `13`; crypto_alt avg `0.0633` n `236`; crypto_major avg `0.2387` n `8`; equity avg `0.1209` n `151`; fx avg `0.0013` n `6`; index avg `0.0218` n `26`; metal avg `0.0164` n `20`; unknown avg `0.2025` n `1191`
- 4h: commodity avg `-0.0457` n `13`; crypto_alt avg `-0.5559` n `236`; crypto_major avg `-0.2446` n `8`; equity avg `-0.4198` n `151`; fx avg `0.0071` n `6`; index avg `-0.0615` n `26`; metal avg `-0.0254` n `20`; unknown avg `0.0634` n `1185`
- 24h: commodity avg `-0.1646` n `13`; crypto_alt avg `-1.9857` n `236`; crypto_major avg `-0.5357` n `8`; equity avg `-0.8581` n `151`; fx avg `-0.0249` n `6`; index avg `-0.0911` n `26`; metal avg `-0.0493` n `20`; unknown avg `3.7625` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1628`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
