# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T03:37:30.079997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.0781` n `229`; crypto_major avg `0.1234` n `8`; equity avg `0.3136` n `88`; fx avg `-0.0077` n `6`; index avg `0.0561` n `25`; metal avg `0.0418` n `20`; unknown avg `-0.1509` n `765`
- 1h: commodity avg `-0.0863` n `12`; crypto_alt avg `-0.197` n `229`; crypto_major avg `-0.3465` n `8`; equity avg `0.3377` n `88`; fx avg `-0.013` n `6`; index avg `0.0536` n `25`; metal avg `-0.0292` n `20`; unknown avg `0.0074` n `763`
- 4h: commodity avg `-0.0503` n `12`; crypto_alt avg `-0.4752` n `229`; crypto_major avg `-0.5487` n `8`; equity avg `-1.0296` n `88`; fx avg `0.0497` n `6`; index avg `-0.1621` n `25`; metal avg `-0.3801` n `20`; unknown avg `-0.3049` n `763`
- 24h: commodity avg `-0.2621` n `12`; crypto_alt avg `0.6967` n `229`; crypto_major avg `1.5245` n `8`; equity avg `-0.6822` n `88`; fx avg `0.0711` n `6`; index avg `-0.0613` n `25`; metal avg `-0.1545` n `20`; unknown avg `1.0491` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
