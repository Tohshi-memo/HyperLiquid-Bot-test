# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T01:37:20.755742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2167` n `12`; crypto_alt avg `-0.0785` n `228`; crypto_major avg `-0.0434` n `8`; equity avg `0.0322` n `67`; fx avg `-0.0053` n `6`; index avg `0.0271` n `23`; metal avg `-0.0685` n `18`; unknown avg `0.8407` n `418`
- 1h: commodity avg `-0.321` n `12`; crypto_alt avg `-0.288` n `228`; crypto_major avg `-0.0707` n `8`; equity avg `0.1493` n `67`; fx avg `-0.0132` n `6`; index avg `0.038` n `23`; metal avg `-0.2248` n `18`; unknown avg `-0.1882` n `418`
- 4h: commodity avg `-0.5623` n `12`; crypto_alt avg `-0.0943` n `228`; crypto_major avg `0.2113` n `8`; equity avg `0.2529` n `67`; fx avg `-0.0016` n `6`; index avg `0.1902` n `23`; metal avg `0.1242` n `18`; unknown avg `0.5573` n `418`
- 24h: commodity avg `-0.1877` n `12`; crypto_alt avg `0.1891` n `228`; crypto_major avg `-0.1254` n `8`; equity avg `1.1786` n `67`; fx avg `-0.0309` n `6`; index avg `1.133` n `23`; metal avg `0.193` n `18`; unknown avg `0.6588` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
