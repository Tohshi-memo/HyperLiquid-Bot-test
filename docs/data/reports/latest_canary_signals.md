# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T19:52:28.372627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.0315` n `230`; crypto_major avg `-0.0786` n `8`; equity avg `0.1085` n `98`; fx avg `0.0015` n `6`; index avg `0.0166` n `25`; metal avg `0.0156` n `20`; unknown avg `-0.0119` n `771`
- 1h: commodity avg `0.0419` n `12`; crypto_alt avg `-0.0003` n `230`; crypto_major avg `0.0489` n `8`; equity avg `0.3004` n `98`; fx avg `0.0105` n `6`; index avg `0.0126` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0914` n `771`
- 4h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.1018` n `230`; crypto_major avg `-0.4635` n `8`; equity avg `0.3436` n `98`; fx avg `0.0378` n `6`; index avg `0.0634` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.076` n `771`
- 24h: commodity avg `0.4593` n `12`; crypto_alt avg `0.9203` n `230`; crypto_major avg `0.8149` n `8`; equity avg `3.7898` n `98`; fx avg `0.0489` n `6`; index avg `0.6076` n `25`; metal avg `0.7631` n `20`; unknown avg `0.3905` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0511`, n `666`, weak_sample_signal
