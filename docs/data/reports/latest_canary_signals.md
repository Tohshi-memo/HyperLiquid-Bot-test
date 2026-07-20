# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T12:07:33.941238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2822` n `12`; crypto_alt avg `-0.0152` n `230`; crypto_major avg `-0.1909` n `8`; equity avg `-0.1766` n `98`; fx avg `0.0007` n `6`; index avg `-0.0565` n `25`; metal avg `-0.1271` n `20`; unknown avg `-0.0379` n `770`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `0.3972` n `230`; crypto_major avg `0.5125` n `8`; equity avg `0.1708` n `98`; fx avg `-0.0131` n `6`; index avg `0.014` n `25`; metal avg `-0.057` n `20`; unknown avg `0.1101` n `770`
- 4h: commodity avg `-0.024` n `12`; crypto_alt avg `0.736` n `230`; crypto_major avg `0.909` n `8`; equity avg `0.7192` n `98`; fx avg `-0.0333` n `6`; index avg `0.1482` n `25`; metal avg `-0.0492` n `20`; unknown avg `0.0231` n `769`
- 24h: commodity avg `-0.4932` n `12`; crypto_alt avg `1.036` n `230`; crypto_major avg `0.607` n `8`; equity avg `0.9848` n `97`; fx avg `-0.044` n `6`; index avg `0.1805` n `25`; metal avg `0.196` n `20`; unknown avg `0.0051` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0737`, n `666`, weak_sample_signal
