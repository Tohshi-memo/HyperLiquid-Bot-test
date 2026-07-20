# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T03:07:27.470595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.104` n `230`; crypto_major avg `-0.1231` n `8`; equity avg `-0.1763` n `98`; fx avg `0.0068` n `6`; index avg `-0.08` n `25`; metal avg `-0.02` n `20`; unknown avg `0.138` n `769`
- 1h: commodity avg `-0.0821` n `12`; crypto_alt avg `-0.0845` n `230`; crypto_major avg `-0.0889` n `8`; equity avg `-0.1455` n `98`; fx avg `0.0063` n `6`; index avg `-0.0704` n `25`; metal avg `0.0897` n `20`; unknown avg `0.2197` n `769`
- 4h: commodity avg `-0.119` n `12`; crypto_alt avg `0.2105` n `230`; crypto_major avg `0.2016` n `8`; equity avg `-0.1087` n `98`; fx avg `-0.0391` n `6`; index avg `-0.0208` n `25`; metal avg `0.257` n `20`; unknown avg `3.5691` n `767`
- 24h: commodity avg `-0.0854` n `12`; crypto_alt avg `0.1247` n `230`; crypto_major avg `0.22` n `8`; equity avg `0.1906` n `97`; fx avg `-0.0032` n `6`; index avg `-0.0191` n `25`; metal avg `0.1144` n `20`; unknown avg `0.0202` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0874`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0834`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
