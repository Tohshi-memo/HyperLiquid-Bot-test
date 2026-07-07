# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T06:37:25.611470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0322` n `12`; crypto_alt avg `0.2447` n `229`; crypto_major avg `0.3083` n `8`; equity avg `0.0959` n `91`; fx avg `0.0016` n `6`; index avg `-0.0039` n `25`; metal avg `0.0546` n `20`; unknown avg `0.0757` n `763`
- 1h: commodity avg `0.137` n `12`; crypto_alt avg `0.3274` n `229`; crypto_major avg `0.3297` n `8`; equity avg `0.286` n `91`; fx avg `0.0309` n `6`; index avg `0.0758` n `25`; metal avg `0.1221` n `20`; unknown avg `0.2146` n `745`
- 4h: commodity avg `0.0895` n `12`; crypto_alt avg `-0.1967` n `229`; crypto_major avg `-0.2614` n `8`; equity avg `-0.214` n `91`; fx avg `-0.0174` n `6`; index avg `-0.0552` n `25`; metal avg `-0.2912` n `20`; unknown avg `14.5668` n `745`
- 24h: commodity avg `0.2201` n `12`; crypto_alt avg `0.6636` n `229`; crypto_major avg `-0.1765` n `8`; equity avg `-1.3318` n `90`; fx avg `0.0069` n `6`; index avg `-0.3196` n `25`; metal avg `-0.3543` n `20`; unknown avg `-0.3509` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
