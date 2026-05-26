# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T10:16:18.411733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0542` n `12`; crypto_alt avg `0.3591` n `228`; crypto_major avg `0.2768` n `8`; equity avg `0.0841` n `67`; fx avg `0.0027` n `6`; index avg `0.0523` n `23`; metal avg `0.2197` n `18`; unknown avg `1.0085` n `417`
- 1h: commodity avg `-0.253` n `12`; crypto_alt avg `0.2132` n `228`; crypto_major avg `0.2316` n `8`; equity avg `0.1654` n `67`; fx avg `0.0026` n `6`; index avg `0.1252` n `23`; metal avg `0.0245` n `18`; unknown avg `1.0788` n `417`
- 4h: commodity avg `0.4252` n `12`; crypto_alt avg `0.3464` n `228`; crypto_major avg `-0.0239` n `8`; equity avg `0.2374` n `67`; fx avg `0.0341` n `6`; index avg `0.1421` n `23`; metal avg `-0.2197` n `18`; unknown avg `0.9607` n `417`
- 24h: commodity avg `0.8158` n `12`; crypto_alt avg `-0.706` n `228`; crypto_major avg `-1.4054` n `8`; equity avg `-0.4534` n `67`; fx avg `-0.08` n `6`; index avg `0.035` n `23`; metal avg `-0.8801` n `18`; unknown avg `0.6682` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
