# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T03:22:25.777905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `-0.0865` n `230`; crypto_major avg `-0.0689` n `8`; equity avg `0.0365` n `98`; fx avg `-0.008` n `6`; index avg `0.0217` n `25`; metal avg `0.0735` n `20`; unknown avg `-0.038` n `769`
- 1h: commodity avg `-0.0389` n `12`; crypto_alt avg `0.0943` n `230`; crypto_major avg `0.1445` n `8`; equity avg `0.2834` n `98`; fx avg `0.0004` n `6`; index avg `0.0557` n `25`; metal avg `0.1865` n `20`; unknown avg `-0.0246` n `769`
- 4h: commodity avg `-0.0765` n `12`; crypto_alt avg `0.2223` n `230`; crypto_major avg `0.1244` n `8`; equity avg `-0.0677` n `98`; fx avg `-0.0453` n `6`; index avg `0.0131` n `25`; metal avg `0.3562` n `20`; unknown avg `2.2417` n `767`
- 24h: commodity avg `-0.0856` n `12`; crypto_alt avg `0.2206` n `230`; crypto_major avg `0.3041` n `8`; equity avg `0.2823` n `97`; fx avg `-0.0091` n `6`; index avg `0.0014` n `25`; metal avg `0.1729` n `20`; unknown avg `0.0058` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1007`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0746`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
