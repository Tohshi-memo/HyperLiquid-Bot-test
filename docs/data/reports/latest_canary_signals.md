# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T03:22:15.555164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1026` n `12`; crypto_alt avg `-0.0283` n `228`; crypto_major avg `-0.0948` n `8`; equity avg `0.0908` n `67`; fx avg `0.0044` n `6`; index avg `-0.0085` n `23`; metal avg `0.1606` n `18`; unknown avg `-0.1156` n `397`
- 1h: commodity avg `-0.3558` n `12`; crypto_alt avg `-0.2388` n `228`; crypto_major avg `-0.3521` n `8`; equity avg `0.1528` n `67`; fx avg `-0.0215` n `6`; index avg `0.0567` n `23`; metal avg `-0.0342` n `18`; unknown avg `-0.1379` n `396`
- 4h: commodity avg `-0.2203` n `12`; crypto_alt avg `0.4005` n `228`; crypto_major avg `-0.3501` n `8`; equity avg `0.4071` n `67`; fx avg `-0.1794` n `6`; index avg `0.251` n `23`; metal avg `-0.3782` n `18`; unknown avg `0.0859` n `396`
- 24h: commodity avg `-0.0483` n `12`; crypto_alt avg `-1.1937` n `228`; crypto_major avg `-0.3548` n `8`; equity avg `0.3949` n `67`; fx avg `-0.0591` n `6`; index avg `-0.2077` n `23`; metal avg `0.4667` n `18`; unknown avg `-0.3628` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
