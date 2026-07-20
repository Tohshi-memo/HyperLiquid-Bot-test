# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T23:43:16.689606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.0062` n `230`; crypto_major avg `0.0156` n `8`; equity avg `-0.008` n `98`; fx avg `0.0018` n `6`; index avg `0.0062` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.2499` n `770`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.1741` n `230`; crypto_major avg `0.2431` n `8`; equity avg `0.175` n `98`; fx avg `0.0096` n `6`; index avg `0.0746` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.3915` n `770`
- 4h: commodity avg `0.0064` n `12`; crypto_alt avg `0.2692` n `230`; crypto_major avg `0.3387` n `8`; equity avg `0.0247` n `98`; fx avg `-0.0229` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0348` n `20`; unknown avg `-0.3602` n `770`
- 24h: commodity avg `-0.333` n `12`; crypto_alt avg `1.5131` n `230`; crypto_major avg `1.0478` n `8`; equity avg `-0.2684` n `98`; fx avg `-0.1939` n `6`; index avg `-0.0032` n `25`; metal avg `0.2181` n `20`; unknown avg `-0.0811` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
