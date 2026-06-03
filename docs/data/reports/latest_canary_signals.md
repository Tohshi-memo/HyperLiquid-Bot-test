# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T23:37:24.041523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6046` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `0.066` n `228`; crypto_major avg `0.0203` n `8`; equity avg `-0.1105` n `73`; fx avg `-0.0047` n `6`; index avg `0.0465` n `23`; metal avg `0.0983` n `18`; unknown avg `-0.0277` n `419`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.5044` n `228`; crypto_major avg `-0.5574` n `8`; equity avg `-0.562` n `73`; fx avg `-0.0029` n `6`; index avg `-0.0876` n `23`; metal avg `0.2855` n `18`; unknown avg `-0.2123` n `419`
- 4h: commodity avg `-0.2407` n `12`; crypto_alt avg `-0.5437` n `228`; crypto_major avg `-0.4471` n `8`; equity avg `-2.0517` n `73`; fx avg `-0.0452` n `6`; index avg `-0.6022` n `23`; metal avg `-0.039` n `18`; unknown avg `0.1467` n `419`
- 24h: commodity avg `0.0205` n `12`; crypto_alt avg `2.7813` n `228`; crypto_major avg `-0.468` n `8`; equity avg `-3.6316` n `72`; fx avg `0.0777` n `6`; index avg `-0.8404` n `23`; metal avg `-1.5028` n `18`; unknown avg `1.1325` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
