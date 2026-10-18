# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T02:22:24.326251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `13`; crypto_alt avg `0.0236` n `237`; crypto_major avg `0.0569` n `8`; equity avg `0.0777` n `151`; fx avg `-0.0013` n `6`; index avg `0.0103` n `26`; metal avg `-0.0041` n `20`; unknown avg `1.1446` n `1193`
- 1h: commodity avg `0.0498` n `13`; crypto_alt avg `-0.2508` n `237`; crypto_major avg `0.0479` n `8`; equity avg `-0.0374` n `151`; fx avg `-0.0016` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0083` n `20`; unknown avg `2.2585` n `1191`
- 4h: commodity avg `0.0089` n `13`; crypto_alt avg `0.1959` n `236`; crypto_major avg `0.5618` n `8`; equity avg `0.2655` n `151`; fx avg `0.0084` n `6`; index avg `0.0392` n `26`; metal avg `0.0409` n `20`; unknown avg `0.2079` n `1185`
- 24h: commodity avg `-0.1125` n `13`; crypto_alt avg `-2.3242` n `236`; crypto_major avg `-0.5368` n `8`; equity avg `-0.8971` n `151`; fx avg `-0.029` n `6`; index avg `-0.1004` n `26`; metal avg `-0.0506` n `20`; unknown avg `3.6882` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1621`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1336`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1027`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0751`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
