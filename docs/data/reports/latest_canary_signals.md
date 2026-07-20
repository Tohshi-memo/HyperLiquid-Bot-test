# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T22:07:34.444548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `12`; crypto_alt avg `-0.1215` n `230`; crypto_major avg `-0.125` n `8`; equity avg `-0.0916` n `98`; fx avg `-0.0125` n `6`; index avg `-0.0517` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.0022` n `770`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `-0.3016` n `230`; crypto_major avg `-0.2501` n `8`; equity avg `0.0191` n `98`; fx avg `-0.0216` n `6`; index avg `-0.0338` n `25`; metal avg `-0.0259` n `20`; unknown avg `-0.0017` n `770`
- 4h: commodity avg `0.1214` n `12`; crypto_alt avg `-0.2495` n `230`; crypto_major avg `-0.3721` n `8`; equity avg `-0.8706` n `98`; fx avg `-0.0323` n `6`; index avg `-0.19` n `25`; metal avg `-0.0935` n `20`; unknown avg `-0.0421` n `770`
- 24h: commodity avg `-0.4042` n `12`; crypto_alt avg `1.7219` n `230`; crypto_major avg `1.3991` n `8`; equity avg `-0.1314` n `98`; fx avg `-0.1912` n `6`; index avg `0.0064` n `25`; metal avg `0.2227` n `20`; unknown avg `0.3632` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1078`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0945`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
