# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T20:16:07.635663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.0632` n `230`; crypto_major avg `0.1058` n `8`; equity avg `-0.1427` n `98`; fx avg `-0.0026` n `6`; index avg `-0.0104` n `25`; metal avg `0.0016` n `20`; unknown avg `-0.0563` n `770`
- 1h: commodity avg `-0.1124` n `12`; crypto_alt avg `0.142` n `230`; crypto_major avg `0.1131` n `8`; equity avg `-0.1539` n `98`; fx avg `-0.0075` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0264` n `20`; unknown avg `-0.1991` n `770`
- 4h: commodity avg `0.1945` n `12`; crypto_alt avg `0.0673` n `230`; crypto_major avg `-0.2162` n `8`; equity avg `-1.1902` n `98`; fx avg `-0.0162` n `6`; index avg `-0.2576` n `25`; metal avg `-0.1584` n `20`; unknown avg `-0.2299` n `770`
- 24h: commodity avg `-0.4034` n `12`; crypto_alt avg `1.5742` n `230`; crypto_major avg `1.1879` n `8`; equity avg `-0.3601` n `98`; fx avg `-0.2088` n `6`; index avg `0.018` n `25`; metal avg `0.0834` n `20`; unknown avg `0.1441` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0933`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.085`, n `666`, weak_sample_signal
