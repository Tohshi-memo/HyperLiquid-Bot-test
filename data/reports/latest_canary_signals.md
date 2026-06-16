# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T12:52:42.757517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.138` n `12`; crypto_alt avg `-0.4352` n `228`; crypto_major avg `-0.2881` n `8`; equity avg `-0.1561` n `77`; fx avg `-0.0084` n `6`; index avg `-0.0059` n `23`; metal avg `0.0995` n `18`; unknown avg `0.3035` n `687`
- 1h: commodity avg `-0.3782` n `12`; crypto_alt avg `0.1819` n `228`; crypto_major avg `0.4684` n `8`; equity avg `-0.4486` n `77`; fx avg `-0.023` n `6`; index avg `-0.1466` n `23`; metal avg `0.2604` n `18`; unknown avg `0.4639` n `687`
- 4h: commodity avg `-0.232` n `12`; crypto_alt avg `-0.2711` n `228`; crypto_major avg `0.1601` n `8`; equity avg `-0.5777` n `77`; fx avg `-0.0035` n `6`; index avg `-0.0895` n `23`; metal avg `0.3953` n `18`; unknown avg `0.717` n `687`
- 24h: commodity avg `-0.3514` n `12`; crypto_alt avg `-0.2216` n `228`; crypto_major avg `1.6809` n `8`; equity avg `1.2712` n `76`; fx avg `-0.0862` n `6`; index avg `0.3641` n `23`; metal avg `0.1494` n `18`; unknown avg `0.8881` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
