# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T01:37:26.493721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.1252` n `228`; crypto_major avg `0.144` n `8`; equity avg `0.0494` n `88`; fx avg `0.0081` n `6`; index avg `0.0316` n `23`; metal avg `0.1003` n `20`; unknown avg `0.0243` n `765`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.0845` n `228`; crypto_major avg `0.1789` n `8`; equity avg `0.2027` n `88`; fx avg `0.0065` n `6`; index avg `0.0766` n `23`; metal avg `-0.1892` n `20`; unknown avg `1.4325` n `765`
- 4h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.9778` n `228`; crypto_major avg `-1.0932` n `8`; equity avg `-0.285` n `88`; fx avg `0.0623` n `6`; index avg `-0.0978` n `23`; metal avg `-0.3837` n `20`; unknown avg `0.1734` n `763`
- 24h: commodity avg `-0.2907` n `12`; crypto_alt avg `0.7245` n `228`; crypto_major avg `2.0412` n `8`; equity avg `1.8565` n `88`; fx avg `0.2149` n `6`; index avg `0.2165` n `23`; metal avg `-0.603` n `20`; unknown avg `2.275` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
