# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T02:52:25.176978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `0.0203` n `229`; crypto_major avg `0.0432` n `8`; equity avg `0.096` n `88`; fx avg `-0.0152` n `6`; index avg `0.0149` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.3167` n `761`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `-0.3202` n `229`; crypto_major avg `-0.4945` n `8`; equity avg `0.1352` n `88`; fx avg `-0.0011` n `6`; index avg `0.0499` n `25`; metal avg `0.1194` n `20`; unknown avg `0.3089` n `761`
- 4h: commodity avg `0.126` n `12`; crypto_alt avg `0.6459` n `229`; crypto_major avg `0.4766` n `8`; equity avg `0.9959` n `88`; fx avg `0.0518` n `6`; index avg `0.2225` n `25`; metal avg `0.702` n `20`; unknown avg `0.5481` n `761`
- 24h: commodity avg `0.3275` n `12`; crypto_alt avg `2.0212` n `228`; crypto_major avg `2.8769` n `8`; equity avg `-1.3286` n `88`; fx avg `-0.0863` n `6`; index avg `-0.2617` n `25`; metal avg `1.2982` n `20`; unknown avg `6.0884` n `735`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
