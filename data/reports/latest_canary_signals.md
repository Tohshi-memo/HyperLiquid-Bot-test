# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T17:07:31.116398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.025` n `12`; crypto_alt avg `0.2109` n `228`; crypto_major avg `0.1223` n `8`; equity avg `0.0093` n `74`; fx avg `-0.0011` n `6`; index avg `0.0036` n `23`; metal avg `0.0102` n `18`; unknown avg `0.0543` n `645`
- 1h: commodity avg `-0.0978` n `12`; crypto_alt avg `0.1566` n `228`; crypto_major avg `-0.0371` n `8`; equity avg `-0.0689` n `74`; fx avg `0.0014` n `6`; index avg `-0.0493` n `23`; metal avg `0.0534` n `18`; unknown avg `0.1269` n `645`
- 4h: commodity avg `0.0032` n `12`; crypto_alt avg `-0.2195` n `228`; crypto_major avg `-0.358` n `8`; equity avg `-0.1468` n `74`; fx avg `-0.0231` n `6`; index avg `0.0111` n `23`; metal avg `-0.0374` n `18`; unknown avg `0.1361` n `645`
- 24h: commodity avg `-0.1554` n `12`; crypto_alt avg `-0.9793` n `228`; crypto_major avg `-0.3144` n `8`; equity avg `0.4955` n `74`; fx avg `-0.0022` n `6`; index avg `0.1377` n `23`; metal avg `0.0934` n `18`; unknown avg `1.7552` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
