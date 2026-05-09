# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T17:22:16.886664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.043` n `228`; crypto_major avg `-0.0574` n `8`; equity avg `0.0126` n `65`; fx avg `0.0` n `5`; index avg `0.0071` n `23`; metal avg `0.0031` n `18`; unknown avg `0.1292` n `376`
- 1h: commodity avg `0.0293` n `12`; crypto_alt avg `0.253` n `228`; crypto_major avg `-0.0073` n `8`; equity avg `0.0535` n `65`; fx avg `0.0` n `5`; index avg `0.0022` n `23`; metal avg `0.0128` n `18`; unknown avg `0.3056` n `376`
- 4h: commodity avg `0.3442` n `12`; crypto_alt avg `0.2639` n `228`; crypto_major avg `0.0149` n `8`; equity avg `0.0958` n `65`; fx avg `-0.0197` n `5`; index avg `0.0506` n `23`; metal avg `-0.0297` n `18`; unknown avg `0.0505` n `376`
- 24h: commodity avg `-0.0617` n `12`; crypto_alt avg `1.26` n `228`; crypto_major avg `1.2245` n `8`; equity avg `1.6995` n `65`; fx avg `0.0048` n `5`; index avg `0.4389` n `23`; metal avg `-0.0577` n `18`; unknown avg `0.5811` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
