# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T22:52:26.965484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `-0.0191` n `229`; crypto_major avg `-0.0499` n `8`; equity avg `-0.2313` n `91`; fx avg `-0.0006` n `6`; index avg `-0.0738` n `25`; metal avg `-0.0276` n `20`; unknown avg `-0.0415` n `763`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `-0.3018` n `229`; crypto_major avg `-0.3949` n `8`; equity avg `-0.2171` n `91`; fx avg `-0.0079` n `6`; index avg `-0.0613` n `25`; metal avg `-0.0089` n `20`; unknown avg `-0.0246` n `763`
- 4h: commodity avg `0.042` n `12`; crypto_alt avg `0.2424` n `229`; crypto_major avg `0.2468` n `8`; equity avg `-0.0263` n `91`; fx avg `0.0223` n `6`; index avg `-0.0392` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.4611` n `763`
- 24h: commodity avg `0.217` n `12`; crypto_alt avg `0.6004` n `229`; crypto_major avg `0.0228` n `8`; equity avg `-0.9533` n `90`; fx avg `0.1391` n `6`; index avg `-0.0002` n `25`; metal avg `-0.3354` n `20`; unknown avg `-0.4504` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
