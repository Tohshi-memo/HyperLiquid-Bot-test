# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T08:22:17.851360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1276` n `12`; crypto_alt avg `0.1239` n `228`; crypto_major avg `0.0158` n `8`; equity avg `0.0809` n `67`; fx avg `0.0104` n `6`; index avg `-0.0142` n `23`; metal avg `-0.0561` n `18`; unknown avg `-0.1094` n `417`
- 1h: commodity avg `0.2359` n `12`; crypto_alt avg `0.342` n `228`; crypto_major avg `0.1057` n `8`; equity avg `0.1226` n `67`; fx avg `0.0367` n `6`; index avg `-0.0154` n `23`; metal avg `0.0755` n `18`; unknown avg `-0.06` n `417`
- 4h: commodity avg `0.5926` n `12`; crypto_alt avg `0.6604` n `228`; crypto_major avg `0.2961` n `8`; equity avg `-0.1151` n `67`; fx avg `-0.0123` n `6`; index avg `-0.0791` n `23`; metal avg `-0.2351` n `18`; unknown avg `0.4051` n `397`
- 24h: commodity avg `0.6791` n `12`; crypto_alt avg `-0.5532` n `228`; crypto_major avg `-1.5186` n `8`; equity avg `-0.6113` n `67`; fx avg `-0.1053` n `6`; index avg `-0.1126` n `23`; metal avg `-0.469` n `18`; unknown avg `0.1054` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
