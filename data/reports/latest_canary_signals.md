# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T03:52:19.080044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0582` n `12`; crypto_alt avg `-0.2757` n `228`; crypto_major avg `-0.1813` n `8`; equity avg `-0.0508` n `67`; fx avg `-0.0032` n `6`; index avg `0.0183` n `23`; metal avg `0.0231` n `18`; unknown avg `1.0066` n `418`
- 1h: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.1908` n `228`; crypto_major avg `-0.1397` n `8`; equity avg `-0.1223` n `67`; fx avg `0.0089` n `6`; index avg `-0.0849` n `23`; metal avg `-0.1635` n `18`; unknown avg `0.6509` n `418`
- 4h: commodity avg `-0.3291` n `12`; crypto_alt avg `-0.443` n `228`; crypto_major avg `0.0473` n `8`; equity avg `-0.0673` n `67`; fx avg `-0.0708` n `6`; index avg `-0.0141` n `23`; metal avg `-0.5613` n `18`; unknown avg `0.5781` n `418`
- 24h: commodity avg `-0.0785` n `12`; crypto_alt avg `-0.634` n `228`; crypto_major avg `-0.4062` n `8`; equity avg `0.6501` n `67`; fx avg `-0.0675` n `6`; index avg `0.9702` n `23`; metal avg `-0.3505` n `18`; unknown avg `1.4859` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
