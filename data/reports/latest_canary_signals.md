# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T17:22:29.307587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `-0.2171` n `230`; crypto_major avg `-0.3432` n `8`; equity avg `-0.1154` n `98`; fx avg `-0.0001` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0236` n `20`; unknown avg `0.1154` n `773`
- 1h: commodity avg `0.1568` n `12`; crypto_alt avg `0.1264` n `230`; crypto_major avg `0.1044` n `8`; equity avg `-0.1437` n `98`; fx avg `0.0084` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0751` n `20`; unknown avg `-0.1147` n `773`
- 4h: commodity avg `0.1675` n `12`; crypto_alt avg `0.4406` n `230`; crypto_major avg `0.605` n `8`; equity avg `1.1387` n `98`; fx avg `-0.026` n `6`; index avg `0.2373` n `25`; metal avg `0.0115` n `20`; unknown avg `9.6791` n `773`
- 24h: commodity avg `0.6097` n `12`; crypto_alt avg `0.0518` n `230`; crypto_major avg `-0.6631` n `8`; equity avg `-0.1913` n `98`; fx avg `-0.0262` n `6`; index avg `-0.0586` n `25`; metal avg `0.3496` n `20`; unknown avg `0.8772` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1066`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0935`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0883`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0822`, n `666`, weak_sample_signal
