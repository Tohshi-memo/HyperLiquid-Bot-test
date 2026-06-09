# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T23:22:26.647425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0378` n `12`; crypto_alt avg `0.1695` n `228`; crypto_major avg `0.0797` n `8`; equity avg `-0.099` n `74`; fx avg `-0.006` n `6`; index avg `-0.0727` n `23`; metal avg `-0.246` n `18`; unknown avg `0.032` n `547`
- 1h: commodity avg `0.1176` n `12`; crypto_alt avg `-0.2013` n `228`; crypto_major avg `-0.3017` n `8`; equity avg `-0.2728` n `74`; fx avg `-0.002` n `6`; index avg `-0.0961` n `23`; metal avg `-0.4168` n `18`; unknown avg `-0.1669` n `547`
- 4h: commodity avg `0.3675` n `12`; crypto_alt avg `-0.1808` n `228`; crypto_major avg `-0.4872` n `8`; equity avg `-0.1275` n `74`; fx avg `-0.0344` n `6`; index avg `0.4987` n `23`; metal avg `-0.3839` n `18`; unknown avg `-0.0616` n `547`
- 24h: commodity avg `-0.5996` n `12`; crypto_alt avg `-1.4047` n `228`; crypto_major avg `-3.0453` n `8`; equity avg `-2.3293` n `74`; fx avg `0.0764` n `6`; index avg `-0.9705` n `23`; metal avg `-1.8873` n `18`; unknown avg `-0.2082` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0395`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0371`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0369`, n `668`, weak_sample_signal
