# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T21:07:34.991114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `0.1571` n `230`; crypto_major avg `0.1319` n `8`; equity avg `0.0798` n `98`; fx avg `0.0082` n `6`; index avg `-0.0006` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.1` n `770`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `0.2898` n `230`; crypto_major avg `0.327` n `8`; equity avg `-0.0237` n `98`; fx avg `-0.0028` n `6`; index avg `-0.009` n `25`; metal avg `0.021` n `20`; unknown avg `-0.042` n `770`
- 4h: commodity avg `0.0876` n `12`; crypto_alt avg `0.1404` n `230`; crypto_major avg `-0.0599` n `8`; equity avg `-0.6689` n `98`; fx avg `-0.0037` n `6`; index avg `-0.1392` n `25`; metal avg `-0.08` n `20`; unknown avg `-0.2265` n `770`
- 24h: commodity avg `-0.4102` n `12`; crypto_alt avg `1.7438` n `230`; crypto_major avg `1.3007` n `8`; equity avg `-0.2528` n `98`; fx avg `-0.2212` n `6`; index avg `0.0107` n `25`; metal avg `0.1314` n `20`; unknown avg `0.2938` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1081`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0946`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
