# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T00:22:14.797071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.4103` n `228`; crypto_major avg `-0.3886` n `8`; equity avg `-0.3639` n `66`; fx avg `-0.0031` n `6`; index avg `-0.2239` n `23`; metal avg `-0.0997` n `18`; unknown avg `-0.1256` n `383`
- 1h: commodity avg `-0.2511` n `12`; crypto_alt avg `-0.3714` n `228`; crypto_major avg `-0.6622` n `8`; equity avg `-0.6765` n `66`; fx avg `0.0324` n `6`; index avg `-0.3619` n `23`; metal avg `-0.244` n `18`; unknown avg `-0.2911` n `383`
- 4h: commodity avg `-0.2458` n `12`; crypto_alt avg `-0.5944` n `228`; crypto_major avg `-0.6786` n `8`; equity avg `-0.6074` n `66`; fx avg `-0.0104` n `6`; index avg `-0.3435` n `23`; metal avg `-0.0131` n `18`; unknown avg `-0.5042` n `383`
- 24h: commodity avg `0.8377` n `12`; crypto_alt avg `-1.9937` n `228`; crypto_major avg `-1.8057` n `8`; equity avg `-1.0599` n `66`; fx avg `0.0095` n `6`; index avg `-1.0829` n `23`; metal avg `-3.24` n `18`; unknown avg `0.3825` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
