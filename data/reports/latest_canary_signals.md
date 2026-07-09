# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T11:52:30.541092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.0945` n `229`; crypto_major avg `0.0991` n `8`; equity avg `0.1947` n `91`; fx avg `-0.0075` n `6`; index avg `0.0582` n `25`; metal avg `0.0722` n `20`; unknown avg `0.078` n `764`
- 1h: commodity avg `-0.1204` n `12`; crypto_alt avg `0.1581` n `229`; crypto_major avg `-0.0014` n `8`; equity avg `0.4721` n `91`; fx avg `-0.0074` n `6`; index avg `0.1635` n `25`; metal avg `0.1766` n `20`; unknown avg `0.0318` n `764`
- 4h: commodity avg `0.2068` n `12`; crypto_alt avg `-0.0565` n `229`; crypto_major avg `-0.4105` n `8`; equity avg `0.2532` n `91`; fx avg `-0.0047` n `6`; index avg `0.0772` n `25`; metal avg `0.0307` n `20`; unknown avg `0.0655` n `764`
- 24h: commodity avg `-0.2345` n `12`; crypto_alt avg `1.099` n `229`; crypto_major avg `0.0519` n `8`; equity avg `3.294` n `91`; fx avg `0.1373` n `6`; index avg `0.5138` n `25`; metal avg `0.6334` n `20`; unknown avg `0.7251` n `741`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
