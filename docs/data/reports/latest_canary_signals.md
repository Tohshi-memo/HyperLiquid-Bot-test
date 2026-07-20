# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T07:52:32.308877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.102` n `12`; crypto_alt avg `0.1903` n `230`; crypto_major avg `0.1432` n `8`; equity avg `-0.0073` n `98`; fx avg `-0.0037` n `6`; index avg `-0.0013` n `25`; metal avg `0.0303` n `20`; unknown avg `0.023` n `763`
- 1h: commodity avg `-0.2841` n `12`; crypto_alt avg `0.5751` n `230`; crypto_major avg `0.533` n `8`; equity avg `0.281` n `98`; fx avg `0.0279` n `6`; index avg `0.0695` n `25`; metal avg `0.2239` n `20`; unknown avg `0.0766` n `763`
- 4h: commodity avg `-0.2919` n `12`; crypto_alt avg `-0.2278` n `230`; crypto_major avg `-0.6539` n `8`; equity avg `-0.1885` n `98`; fx avg `0.0065` n `6`; index avg `-0.0378` n `25`; metal avg `0.0305` n `20`; unknown avg `-0.0977` n `747`
- 24h: commodity avg `-0.3778` n `12`; crypto_alt avg `0.0084` n `230`; crypto_major avg `-0.4077` n `8`; equity avg `0.09` n `97`; fx avg `-0.0284` n `6`; index avg `0.0349` n `25`; metal avg `0.1972` n `20`; unknown avg `-0.0232` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.088`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
