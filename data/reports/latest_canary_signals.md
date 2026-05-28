# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T17:52:22.161537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `12`; crypto_alt avg `0.1716` n `228`; crypto_major avg `0.0123` n `8`; equity avg `0.2469` n `69`; fx avg `0.0026` n `6`; index avg `0.0094` n `23`; metal avg `0.1019` n `18`; unknown avg `-0.0556` n `417`
- 1h: commodity avg `0.2716` n `12`; crypto_alt avg `0.5296` n `228`; crypto_major avg `0.3093` n `8`; equity avg `0.3512` n `69`; fx avg `-0.0052` n `6`; index avg `-0.0389` n `23`; metal avg `0.0142` n `18`; unknown avg `0.1004` n `417`
- 4h: commodity avg `-0.0774` n `12`; crypto_alt avg `1.5768` n `228`; crypto_major avg `1.7516` n `8`; equity avg `2.161` n `69`; fx avg `-0.024` n `6`; index avg `1.3292` n `23`; metal avg `1.8499` n `18`; unknown avg `0.3092` n `417`
- 24h: commodity avg `0.5797` n `12`; crypto_alt avg `-3.2992` n `228`; crypto_major avg `-0.978` n `8`; equity avg `1.6893` n `68`; fx avg `-0.0191` n `6`; index avg `1.0892` n `23`; metal avg `0.7896` n `18`; unknown avg `-0.6175` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
