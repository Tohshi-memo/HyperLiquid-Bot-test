# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T17:07:32.548083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0807` n `12`; crypto_alt avg `0.0382` n `230`; crypto_major avg `0.047` n `8`; equity avg `0.1271` n `98`; fx avg `0.0117` n `6`; index avg `0.0282` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0441` n `773`
- 1h: commodity avg `0.1417` n `12`; crypto_alt avg `0.2342` n `230`; crypto_major avg `0.2645` n `8`; equity avg `-0.1314` n `98`; fx avg `0.0045` n `6`; index avg `0.0038` n `25`; metal avg `-0.1208` n `20`; unknown avg `-0.1145` n `773`
- 4h: commodity avg `-0.0102` n `12`; crypto_alt avg `0.794` n `230`; crypto_major avg `0.9549` n `8`; equity avg `1.4294` n `98`; fx avg `-0.0211` n `6`; index avg `0.2922` n `25`; metal avg `0.089` n `20`; unknown avg `9.84` n `773`
- 24h: commodity avg `0.5571` n `12`; crypto_alt avg `0.1386` n `230`; crypto_major avg `-0.4651` n `8`; equity avg `-0.2269` n `98`; fx avg `-0.0238` n `6`; index avg `-0.0735` n `25`; metal avg `0.3679` n `20`; unknown avg `0.883` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1075`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1005`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0902`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.083`, n `666`, weak_sample_signal
