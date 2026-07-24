# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T19:37:33.858295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1012` n `12`; crypto_alt avg `0.0096` n `230`; crypto_major avg `0.0655` n `8`; equity avg `0.1511` n `100`; fx avg `-0.0038` n `6`; index avg `0.0341` n `25`; metal avg `0.0276` n `20`; unknown avg `0.11` n `773`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `0.1083` n `230`; crypto_major avg `0.2888` n `8`; equity avg `-0.1025` n `100`; fx avg `0.0033` n `6`; index avg `-0.0077` n `25`; metal avg `-0.0265` n `20`; unknown avg `-0.0575` n `773`
- 4h: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.1193` n `230`; crypto_major avg `-0.0831` n `8`; equity avg `-1.1146` n `100`; fx avg `-0.0444` n `6`; index avg `-0.2117` n `25`; metal avg `-0.1796` n `20`; unknown avg `-0.0992` n `773`
- 24h: commodity avg `-0.5257` n `12`; crypto_alt avg `-0.9523` n `230`; crypto_major avg `-0.7387` n `8`; equity avg `-3.1074` n `100`; fx avg `-0.1668` n `6`; index avg `-0.3926` n `25`; metal avg `0.0231` n `20`; unknown avg `14.0584` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1298`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1247`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1124`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
