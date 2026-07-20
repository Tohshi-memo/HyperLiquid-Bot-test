# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T08:22:32.440747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0893` n `12`; crypto_alt avg `0.0038` n `230`; crypto_major avg `0.0453` n `8`; equity avg `0.0907` n `98`; fx avg `-0.0036` n `6`; index avg `0.0129` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.0344` n `769`
- 1h: commodity avg `-0.4307` n `12`; crypto_alt avg `0.3656` n `230`; crypto_major avg `0.2898` n `8`; equity avg `0.3982` n `98`; fx avg `-0.003` n `6`; index avg `0.0702` n `25`; metal avg `0.2442` n `20`; unknown avg `0.0935` n `763`
- 4h: commodity avg `-0.4974` n `12`; crypto_alt avg `0.2785` n `230`; crypto_major avg `-0.1706` n `8`; equity avg `0.1775` n `98`; fx avg `0.0106` n `6`; index avg `0.071` n `25`; metal avg `0.1391` n `20`; unknown avg `-0.057` n `747`
- 24h: commodity avg `-0.5641` n `12`; crypto_alt avg `0.0446` n `230`; crypto_major avg `-0.4091` n `8`; equity avg `0.1661` n `97`; fx avg `-0.0318` n `6`; index avg `0.0447` n `25`; metal avg `0.2305` n `20`; unknown avg `-0.0203` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0861`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
