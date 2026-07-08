# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T16:22:26.471065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0798` n `12`; crypto_alt avg `0.1023` n `229`; crypto_major avg `0.1146` n `8`; equity avg `0.3794` n `91`; fx avg `0.0024` n `6`; index avg `0.1372` n `25`; metal avg `0.0235` n `20`; unknown avg `0.0899` n `764`
- 1h: commodity avg `-0.0743` n `12`; crypto_alt avg `0.3376` n `229`; crypto_major avg `0.5025` n `8`; equity avg `0.5691` n `91`; fx avg `0.0099` n `6`; index avg `0.1948` n `25`; metal avg `0.0813` n `20`; unknown avg `0.1762` n `764`
- 4h: commodity avg `0.2381` n `12`; crypto_alt avg `-0.3411` n `229`; crypto_major avg `-0.6365` n `8`; equity avg `0.8215` n `91`; fx avg `0.0618` n `6`; index avg `0.2137` n `25`; metal avg `-0.3309` n `20`; unknown avg `-0.254` n `763`
- 24h: commodity avg `1.0535` n `12`; crypto_alt avg `-3.832` n `229`; crypto_major avg `-4.08` n `8`; equity avg `-0.5916` n `91`; fx avg `0.0154` n `6`; index avg `-0.2412` n `25`; metal avg `-1.5402` n `20`; unknown avg `-0.6349` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
