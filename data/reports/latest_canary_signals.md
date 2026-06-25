# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T19:52:29.900779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0596` n `12`; crypto_alt avg `-0.0688` n `228`; crypto_major avg `-0.0426` n `8`; equity avg `0.1058` n `86`; fx avg `-0.0137` n `6`; index avg `0.0094` n `23`; metal avg `-0.084` n `20`; unknown avg `0.0809` n `765`
- 1h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.4489` n `228`; crypto_major avg `-0.5227` n `8`; equity avg `-0.2334` n `86`; fx avg `-0.0057` n `6`; index avg `-0.0578` n `23`; metal avg `-0.1454` n `20`; unknown avg `-0.2023` n `765`
- 4h: commodity avg `0.026` n `12`; crypto_alt avg `-0.6006` n `228`; crypto_major avg `-0.0654` n `8`; equity avg `-0.1111` n `86`; fx avg `0.0166` n `6`; index avg `-0.0257` n `23`; metal avg `-0.2996` n `20`; unknown avg `0.3176` n `765`
- 24h: commodity avg `0.4268` n `12`; crypto_alt avg `-0.4822` n `228`; crypto_major avg `-0.2921` n `8`; equity avg `0.0309` n `86`; fx avg `0.0835` n `6`; index avg `0.3575` n `23`; metal avg `0.5918` n `20`; unknown avg `0.493` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
