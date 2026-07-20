# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T18:52:41.453451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0367` n `12`; crypto_alt avg `-0.1481` n `230`; crypto_major avg `-0.2601` n `8`; equity avg `-0.2498` n `98`; fx avg `-0.0101` n `6`; index avg `-0.044` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.2509` n `770`
- 1h: commodity avg `0.189` n `12`; crypto_alt avg `0.0161` n `230`; crypto_major avg `-0.2111` n `8`; equity avg `-0.4368` n `98`; fx avg `-0.0009` n `6`; index avg `-0.0815` n `25`; metal avg `-0.0138` n `20`; unknown avg `0.2229` n `770`
- 4h: commodity avg `0.2451` n `12`; crypto_alt avg `1.2044` n `230`; crypto_major avg `1.3451` n `8`; equity avg `0.2729` n `98`; fx avg `-0.0527` n `6`; index avg `-0.0408` n `25`; metal avg `-0.0719` n `20`; unknown avg `0.3664` n `770`
- 24h: commodity avg `-0.2465` n `12`; crypto_alt avg `2.0028` n `230`; crypto_major avg `1.5731` n `8`; equity avg `0.2515` n `98`; fx avg `-0.1502` n `6`; index avg `0.1147` n `25`; metal avg `0.1407` n `20`; unknown avg `0.5291` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0861`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0834`, n `666`, weak_sample_signal
