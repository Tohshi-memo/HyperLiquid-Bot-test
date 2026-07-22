# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T16:37:28.619972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0665` n `12`; crypto_alt avg `0.276` n `230`; crypto_major avg `0.4429` n `8`; equity avg `-0.0317` n `98`; fx avg `-0.0009` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0331` n `20`; unknown avg `-0.0921` n `773`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `0.1314` n `230`; crypto_major avg `0.2215` n `8`; equity avg `-0.0637` n `98`; fx avg `-0.0059` n `6`; index avg `0.031` n `25`; metal avg `-0.0789` n `20`; unknown avg `-0.0902` n `773`
- 4h: commodity avg `0.004` n `12`; crypto_alt avg `0.7208` n `230`; crypto_major avg `0.8874` n `8`; equity avg `1.3618` n `98`; fx avg `-0.03` n `6`; index avg `0.2628` n `25`; metal avg `0.0192` n `20`; unknown avg `9.591` n `773`
- 24h: commodity avg `0.5143` n `12`; crypto_alt avg `0.0655` n `230`; crypto_major avg `-0.5137` n `8`; equity avg `0.0373` n `98`; fx avg `-0.0216` n `6`; index avg `-0.0531` n `25`; metal avg `0.3368` n `20`; unknown avg `0.9386` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1073`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0958`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0783`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
