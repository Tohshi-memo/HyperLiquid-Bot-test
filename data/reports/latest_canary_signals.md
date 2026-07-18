# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T16:52:31.522990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.152` n `230`; crypto_major avg `0.1479` n `8`; equity avg `0.0265` n `96`; fx avg `-0.0111` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0711` n `770`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.1452` n `230`; crypto_major avg `0.209` n `8`; equity avg `-0.0257` n `96`; fx avg `-0.0481` n `6`; index avg `-0.019` n `25`; metal avg `-0.004` n `20`; unknown avg `0.0355` n `770`
- 4h: commodity avg `-0.0323` n `12`; crypto_alt avg `0.1221` n `230`; crypto_major avg `0.1709` n `8`; equity avg `-0.0779` n `96`; fx avg `-0.0551` n `6`; index avg `-0.015` n `25`; metal avg `-0.0544` n `20`; unknown avg `-0.0716` n `770`
- 24h: commodity avg `0.2994` n `12`; crypto_alt avg `-0.7806` n `230`; crypto_major avg `0.2022` n `8`; equity avg `-1.3116` n `96`; fx avg `-0.1294` n `6`; index avg `-0.1295` n `25`; metal avg `-0.034` n `20`; unknown avg `0.0015` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
