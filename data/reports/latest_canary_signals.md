# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T03:52:19.265052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `-0.0389` n `228`; crypto_major avg `0.0027` n `8`; equity avg `-0.0179` n `67`; fx avg `-0.0098` n `6`; index avg `-0.0145` n `23`; metal avg `-0.0497` n `18`; unknown avg `0.0731` n `407`
- 1h: commodity avg `0.0144` n `12`; crypto_alt avg `-0.1282` n `228`; crypto_major avg `0.0682` n `8`; equity avg `0.0748` n `67`; fx avg `-0.0124` n `6`; index avg `0.0046` n `23`; metal avg `0.2001` n `18`; unknown avg `-0.5329` n `407`
- 4h: commodity avg `0.3007` n `12`; crypto_alt avg `-1.4589` n `228`; crypto_major avg `-1.0511` n `8`; equity avg `-0.6489` n `67`; fx avg `-0.1013` n `6`; index avg `-0.1832` n `23`; metal avg `-0.4883` n `18`; unknown avg `0.4342` n `405`
- 24h: commodity avg `0.4969` n `12`; crypto_alt avg `-0.2488` n `228`; crypto_major avg `-0.798` n `8`; equity avg `-0.3983` n `67`; fx avg `-0.0151` n `6`; index avg `0.0654` n `23`; metal avg `-0.0338` n `18`; unknown avg `0.2885` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
