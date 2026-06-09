# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T23:03:53.272831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1147` n `12`; crypto_alt avg `-0.0608` n `228`; crypto_major avg `-0.0363` n `8`; equity avg `0.2341` n `74`; fx avg `0.0081` n `6`; index avg `0.1212` n `23`; metal avg `0.2281` n `18`; unknown avg `-0.0464` n `547`
- 1h: commodity avg `-0.1375` n `12`; crypto_alt avg `-0.0559` n `228`; crypto_major avg `-0.0839` n `8`; equity avg `-0.2424` n `74`; fx avg `0.0181` n `6`; index avg `-0.0606` n `23`; metal avg `-0.1433` n `18`; unknown avg `-0.0788` n `547`
- 4h: commodity avg `0.3232` n `12`; crypto_alt avg `-0.4374` n `228`; crypto_major avg `-0.6017` n `8`; equity avg `-0.3941` n `74`; fx avg `-0.0263` n `6`; index avg `0.3104` n `23`; metal avg `-0.428` n `18`; unknown avg `-0.1048` n `547`
- 24h: commodity avg `-0.6538` n `12`; crypto_alt avg `-1.9748` n `228`; crypto_major avg `-3.4853` n `8`; equity avg `-2.2155` n `74`; fx avg `0.0748` n `6`; index avg `-0.8535` n `23`; metal avg `-1.6569` n `18`; unknown avg `-0.1154` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0376`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0362`, n `668`, weak_sample_signal
