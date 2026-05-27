# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T13:07:22.031581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1578` n `12`; crypto_alt avg `-0.3402` n `228`; crypto_major avg `-0.2367` n `8`; equity avg `-0.0371` n `67`; fx avg `-0.0199` n `6`; index avg `-0.0676` n `23`; metal avg `-0.302` n `18`; unknown avg `-0.2474` n `418`
- 1h: commodity avg `-0.5619` n `12`; crypto_alt avg `0.3946` n `228`; crypto_major avg `-0.0193` n `8`; equity avg `-0.2241` n `67`; fx avg `0.0047` n `6`; index avg `-0.064` n `23`; metal avg `0.0386` n `18`; unknown avg `0.008` n `418`
- 4h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.1542` n `228`; crypto_major avg `-0.1735` n `8`; equity avg `0.0601` n `67`; fx avg `-0.02` n `6`; index avg `0.0473` n `23`; metal avg `-0.8073` n `18`; unknown avg `-0.4004` n `418`
- 24h: commodity avg `-1.6741` n `12`; crypto_alt avg `-2.2118` n `228`; crypto_major avg `-1.3547` n `8`; equity avg `0.547` n `67`; fx avg `-0.0493` n `6`; index avg `0.6476` n `23`; metal avg `-1.4055` n `18`; unknown avg `0.6659` n `398`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
