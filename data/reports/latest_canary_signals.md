# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T22:37:36.490471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.0903` n `229`; crypto_major avg `0.0348` n `8`; equity avg `0.0446` n `91`; fx avg `-0.0019` n `6`; index avg `0.0343` n `25`; metal avg `0.0157` n `20`; unknown avg `0.0356` n `764`
- 1h: commodity avg `-0.1172` n `12`; crypto_alt avg `0.3531` n `229`; crypto_major avg `0.2233` n `8`; equity avg `0.1469` n `91`; fx avg `0.0171` n `6`; index avg `0.047` n `25`; metal avg `0.0679` n `20`; unknown avg `0.0534` n `764`
- 4h: commodity avg `0.1673` n `12`; crypto_alt avg `0.311` n `229`; crypto_major avg `0.3623` n `8`; equity avg `0.6478` n `91`; fx avg `0.0277` n `6`; index avg `0.0803` n `25`; metal avg `-0.0015` n `20`; unknown avg `1.1438` n `764`
- 24h: commodity avg `0.3558` n `12`; crypto_alt avg `-1.6085` n `229`; crypto_major avg `-2.4364` n `8`; equity avg `1.4553` n `91`; fx avg `0.0599` n `6`; index avg `0.0307` n `25`; metal avg `-0.682` n `20`; unknown avg `0.0044` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
