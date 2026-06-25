# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T00:37:25.838908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0293` n `12`; crypto_alt avg `-0.2631` n `228`; crypto_major avg `-0.091` n `8`; equity avg `-0.2334` n `86`; fx avg `0.0047` n `6`; index avg `0.0065` n `23`; metal avg `-0.1365` n `20`; unknown avg `-0.3115` n `764`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `-0.2673` n `228`; crypto_major avg `-0.1455` n `8`; equity avg `-0.5159` n `86`; fx avg `0.0648` n `6`; index avg `-0.1072` n `23`; metal avg `-0.2193` n `20`; unknown avg `-0.3258` n `764`
- 4h: commodity avg `0.1136` n `12`; crypto_alt avg `0.3913` n `228`; crypto_major avg `0.5548` n `8`; equity avg `0.3656` n `86`; fx avg `0.0479` n `6`; index avg `0.0771` n `23`; metal avg `-0.1177` n `20`; unknown avg `-1.1349` n `748`
- 24h: commodity avg `-0.3912` n `12`; crypto_alt avg `-2.6625` n `228`; crypto_major avg `-2.1921` n `8`; equity avg `3.9825` n `86`; fx avg `0.0723` n `6`; index avg `0.3578` n `23`; metal avg `-1.6559` n `20`; unknown avg `-1.5449` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
