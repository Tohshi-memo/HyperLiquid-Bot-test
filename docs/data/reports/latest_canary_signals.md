# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T12:37:15.193901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1679` n `12`; crypto_alt avg `0.1595` n `228`; crypto_major avg `0.1198` n `8`; equity avg `0.0118` n `67`; fx avg `-0.008` n `6`; index avg `0.0174` n `23`; metal avg `0.1701` n `18`; unknown avg `0.0307` n `405`
- 1h: commodity avg `0.2739` n `12`; crypto_alt avg `-0.1543` n `228`; crypto_major avg `0.0481` n `8`; equity avg `-0.031` n `67`; fx avg `-0.0169` n `6`; index avg `0.0257` n `23`; metal avg `-0.2049` n `18`; unknown avg `-0.1279` n `397`
- 4h: commodity avg `-0.0424` n `12`; crypto_alt avg `0.2426` n `228`; crypto_major avg `0.0906` n `8`; equity avg `0.2575` n `67`; fx avg `0.0179` n `6`; index avg `0.1315` n `23`; metal avg `0.106` n `18`; unknown avg `-0.2175` n `397`
- 24h: commodity avg `0.0718` n `12`; crypto_alt avg `0.9642` n `228`; crypto_major avg `0.1913` n `8`; equity avg `0.4944` n `67`; fx avg `0.0297` n `6`; index avg `0.0881` n `23`; metal avg `0.6283` n `18`; unknown avg `0.518` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
