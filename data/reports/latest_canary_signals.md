# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T23:37:24.458125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0204` n `229`; crypto_major avg `0.0656` n `8`; equity avg `-0.027` n `91`; fx avg `-0.0013` n `6`; index avg `0.0001` n `25`; metal avg `-0.009` n `20`; unknown avg `1.5329` n `763`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.1533` n `229`; crypto_major avg `-0.2446` n `8`; equity avg `-0.4621` n `91`; fx avg `-0.0115` n `6`; index avg `-0.0871` n `25`; metal avg `-0.0562` n `20`; unknown avg `1.589` n `763`
- 4h: commodity avg `0.0519` n `12`; crypto_alt avg `0.0626` n `229`; crypto_major avg `-0.0248` n `8`; equity avg `-0.4352` n `91`; fx avg `0.0169` n `6`; index avg `-0.0743` n `25`; metal avg `-0.0142` n `20`; unknown avg `1.1447` n `763`
- 24h: commodity avg `0.2559` n `12`; crypto_alt avg `0.4686` n `229`; crypto_major avg `-0.1642` n `8`; equity avg `-1.1665` n `90`; fx avg `0.1301` n `6`; index avg `-0.0481` n `25`; metal avg `-0.3952` n `20`; unknown avg `-0.3392` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
