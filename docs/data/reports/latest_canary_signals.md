# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T00:07:19.743779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0824` n `12`; crypto_alt avg `0.1277` n `228`; crypto_major avg `-0.0796` n `8`; equity avg `-0.0355` n `67`; fx avg `-0.0328` n `6`; index avg `-0.0138` n `23`; metal avg `-0.049` n `18`; unknown avg `0.1426` n `396`
- 1h: commodity avg `0.1438` n `12`; crypto_alt avg `0.4486` n `228`; crypto_major avg `0.2772` n `8`; equity avg `0.1709` n `67`; fx avg `-0.0814` n `6`; index avg `-0.0037` n `23`; metal avg `0.0477` n `18`; unknown avg `0.3616` n `396`
- 4h: commodity avg `-0.5782` n `12`; crypto_alt avg `0.1184` n `228`; crypto_major avg `0.298` n `8`; equity avg `-0.0484` n `67`; fx avg `-0.041` n `6`; index avg `-0.0773` n `23`; metal avg `1.31` n `18`; unknown avg `0.0862` n `396`
- 24h: commodity avg `0.6365` n `12`; crypto_alt avg `-1.3324` n `228`; crypto_major avg `0.6906` n `8`; equity avg `0.3094` n `67`; fx avg `0.0209` n `6`; index avg `-0.2146` n `23`; metal avg `1.0033` n `18`; unknown avg `-0.0962` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
