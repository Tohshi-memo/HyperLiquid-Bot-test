# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T21:22:31.463765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `0.0454` n `230`; crypto_major avg `0.058` n `8`; equity avg `-0.0006` n `98`; fx avg `-0.0005` n `6`; index avg `0.0006` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.042` n `770`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.2371` n `230`; crypto_major avg `0.2678` n `8`; equity avg `0.1172` n `98`; fx avg `0.0029` n `6`; index avg `0.0104` n `25`; metal avg `0.0145` n `20`; unknown avg `-0.0659` n `770`
- 4h: commodity avg `0.1029` n `12`; crypto_alt avg `0.2638` n `230`; crypto_major avg `0.1961` n `8`; equity avg `-0.8129` n `98`; fx avg `-0.0063` n `6`; index avg `-0.1522` n `25`; metal avg `-0.081` n `20`; unknown avg `-0.1478` n `770`
- 24h: commodity avg `-0.4077` n `12`; crypto_alt avg `1.8873` n `230`; crypto_major avg `1.4586` n `8`; equity avg `-0.2484` n `98`; fx avg `-0.2131` n `6`; index avg `0.0053` n `25`; metal avg `0.1369` n `20`; unknown avg `0.3281` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
