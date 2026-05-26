# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T01:48:12.816997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0321` n `12`; crypto_alt avg `0.0851` n `228`; crypto_major avg `0.0433` n `8`; equity avg `0.0234` n `67`; fx avg `0.0173` n `6`; index avg `0.0218` n `23`; metal avg `-0.2635` n `18`; unknown avg `-0.0204` n `407`
- 1h: commodity avg `0.2123` n `12`; crypto_alt avg `-0.2094` n `228`; crypto_major avg `0.0306` n `8`; equity avg `-0.3637` n `67`; fx avg `-0.0738` n `6`; index avg `-0.0556` n `23`; metal avg `-0.6572` n `18`; unknown avg `0.6756` n `407`
- 4h: commodity avg `0.2529` n `12`; crypto_alt avg `-1.9539` n `228`; crypto_major avg `-1.1904` n `8`; equity avg `-1.1608` n `67`; fx avg `-0.084` n `6`; index avg `-0.5513` n `23`; metal avg `-1.2042` n `18`; unknown avg `2.5072` n `405`
- 24h: commodity avg `0.1229` n `12`; crypto_alt avg `-0.2285` n `228`; crypto_major avg `-0.9767` n `8`; equity avg `-0.4912` n `67`; fx avg `-0.0244` n `6`; index avg `0.0158` n `23`; metal avg `-0.6884` n `18`; unknown avg `1.1116` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
