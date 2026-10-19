# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T10:22:29.303407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `13`; crypto_alt avg `-0.2993` n `237`; crypto_major avg `-0.3378` n `8`; equity avg `-0.0965` n `151`; fx avg `0.0019` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0237` n `20`; unknown avg `1.1509` n `1195`
- 1h: commodity avg `0.1577` n `13`; crypto_alt avg `-0.4571` n `237`; crypto_major avg `-0.4665` n `8`; equity avg `0.0491` n `151`; fx avg `0.0061` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.8166` n `1193`
- 4h: commodity avg `0.3967` n `13`; crypto_alt avg `-0.3381` n `237`; crypto_major avg `-0.3138` n `8`; equity avg `-0.3192` n `151`; fx avg `-0.0084` n `6`; index avg `-0.07` n `26`; metal avg `-0.0825` n `20`; unknown avg `0.9817` n `1146`
- 24h: commodity avg `-0.1622` n `13`; crypto_alt avg `-0.1377` n `237`; crypto_major avg `0.4097` n `8`; equity avg `2.4112` n `151`; fx avg `-0.043` n `6`; index avg `0.4287` n `26`; metal avg `0.2107` n `20`; unknown avg `1.7837` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1981`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1313`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0621`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
