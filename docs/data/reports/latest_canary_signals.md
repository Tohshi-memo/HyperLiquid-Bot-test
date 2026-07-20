# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T02:22:26.000906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.2646` n `230`; crypto_major avg `-0.3018` n `8`; equity avg `-0.3902` n `98`; fx avg `-0.0021` n `6`; index avg `-0.1043` n `25`; metal avg `-0.0228` n `20`; unknown avg `0.3622` n `769`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `-0.0335` n `230`; crypto_major avg `-0.0237` n `8`; equity avg `-0.5735` n `98`; fx avg `-0.0225` n `6`; index avg `-0.1123` n `25`; metal avg `-0.0325` n `20`; unknown avg `0.0079` n `769`
- 4h: commodity avg `-0.1022` n `12`; crypto_alt avg `-0.0703` n `230`; crypto_major avg `-0.2113` n `8`; equity avg `-0.4563` n `98`; fx avg `-0.0406` n `6`; index avg `-0.0637` n `25`; metal avg `0.1486` n `20`; unknown avg `1.3476` n `767`
- 24h: commodity avg `-0.0508` n `12`; crypto_alt avg `-0.0748` n `230`; crypto_major avg `-0.0614` n `8`; equity avg `-0.0645` n `97`; fx avg `-0.0208` n `6`; index avg `-0.0168` n `25`; metal avg `-0.0077` n `20`; unknown avg `0.0418` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1475`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1208`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `667`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1081`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1058`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `667`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0908`, n `667`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0829`, n `667`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0792`, n `667`, weak_sample_signal
