# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T01:52:18.124191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.1011` n `228`; crypto_major avg `-0.1924` n `8`; equity avg `0.114` n `67`; fx avg `0.0223` n `6`; index avg `0.0015` n `23`; metal avg `-0.0751` n `18`; unknown avg `0.1533` n `396`
- 1h: commodity avg `0.2336` n `12`; crypto_alt avg `-0.0515` n `228`; crypto_major avg `-0.2553` n `8`; equity avg `0.0781` n `67`; fx avg `-0.0066` n `6`; index avg `0.0512` n `23`; metal avg `-0.1609` n `18`; unknown avg `-0.0443` n `396`
- 4h: commodity avg `-0.7479` n `12`; crypto_alt avg `1.4411` n `228`; crypto_major avg `0.8289` n `8`; equity avg `0.3315` n `67`; fx avg `-0.1114` n `6`; index avg `0.1831` n `23`; metal avg `1.5216` n `18`; unknown avg `1.0025` n `396`
- 24h: commodity avg `0.454` n `12`; crypto_alt avg `-1.5269` n `228`; crypto_major avg `-0.2019` n `8`; equity avg `0.2457` n `67`; fx avg `-0.0303` n `6`; index avg `-0.1403` n `23`; metal avg `0.6586` n `18`; unknown avg `-0.3865` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
