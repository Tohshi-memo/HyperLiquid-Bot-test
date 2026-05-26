# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T01:52:17.068731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `12`; crypto_alt avg `0.2088` n `228`; crypto_major avg `0.0712` n `8`; equity avg `0.0856` n `67`; fx avg `0.015` n `6`; index avg `0.0299` n `23`; metal avg `-0.1931` n `18`; unknown avg `-0.0519` n `407`
- 1h: commodity avg `0.1972` n `12`; crypto_alt avg `-0.0865` n `228`; crypto_major avg `0.0586` n `8`; equity avg `-0.3022` n `67`; fx avg `-0.076` n `6`; index avg `-0.0476` n `23`; metal avg `-0.5874` n `18`; unknown avg `0.7335` n `407`
- 4h: commodity avg `0.2378` n `12`; crypto_alt avg `-1.834` n `228`; crypto_major avg `-1.1623` n `8`; equity avg `-1.0995` n `67`; fx avg `-0.0862` n `6`; index avg `-0.5432` n `23`; metal avg `-1.135` n `18`; unknown avg `2.7407` n `405`
- 24h: commodity avg `0.108` n `12`; crypto_alt avg `-0.1042` n `228`; crypto_major avg `-0.9484` n `8`; equity avg `-0.4294` n `67`; fx avg `-0.0266` n `6`; index avg `0.0241` n `23`; metal avg `-0.6191` n `18`; unknown avg `1.131` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
