# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T23:22:27.096127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.2657` n `229`; crypto_major avg `-0.1977` n `8`; equity avg `0.1218` n `91`; fx avg `-0.0079` n `6`; index avg `0.0017` n `25`; metal avg `0.0001` n `20`; unknown avg `0.049` n `765`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `-0.2468` n `229`; crypto_major avg `-0.298` n `8`; equity avg `0.1324` n `91`; fx avg `-0.0033` n `6`; index avg `0.005` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.1129` n `765`
- 4h: commodity avg `0.0509` n `12`; crypto_alt avg `-0.2767` n `229`; crypto_major avg `-0.0736` n `8`; equity avg `-0.032` n `91`; fx avg `0.0022` n `6`; index avg `0.0096` n `25`; metal avg `0.0278` n `20`; unknown avg `-0.484` n `765`
- 24h: commodity avg `-1.1229` n `12`; crypto_alt avg `0.8404` n `229`; crypto_major avg `0.4289` n `8`; equity avg `1.8281` n `91`; fx avg `0.0455` n `6`; index avg `0.3749` n `25`; metal avg `0.6613` n `20`; unknown avg `-0.2379` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
