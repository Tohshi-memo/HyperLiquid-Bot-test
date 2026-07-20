# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T13:22:24.641133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.022` n `230`; crypto_major avg `-0.0679` n `8`; equity avg `-0.0406` n `98`; fx avg `-0.0019` n `6`; index avg `0.0045` n `25`; metal avg `0.0382` n `20`; unknown avg `-0.0091` n `770`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `-0.1363` n `230`; crypto_major avg `-0.1022` n `8`; equity avg `0.1394` n `98`; fx avg `0.0014` n `6`; index avg `0.0191` n `25`; metal avg `0.0413` n `20`; unknown avg `-0.0184` n `770`
- 4h: commodity avg `0.1414` n `12`; crypto_alt avg `0.5418` n `230`; crypto_major avg `0.5994` n `8`; equity avg `0.621` n `98`; fx avg `-0.0172` n `6`; index avg `0.1231` n `25`; metal avg `-0.0367` n `20`; unknown avg `0.1282` n `770`
- 24h: commodity avg `-0.482` n `12`; crypto_alt avg `0.7842` n `230`; crypto_major avg `0.4581` n `8`; equity avg `0.879` n `97`; fx avg `-0.0583` n `6`; index avg `0.1915` n `25`; metal avg `0.1659` n `20`; unknown avg `0.0597` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.089`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0772`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
