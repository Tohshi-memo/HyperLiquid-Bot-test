# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T02:52:17.616824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2284` n `12`; crypto_alt avg `0.0205` n `228`; crypto_major avg `0.1411` n `8`; equity avg `-0.0577` n `67`; fx avg `0.0114` n `6`; index avg `-0.066` n `23`; metal avg `-0.2296` n `18`; unknown avg `0.0274` n `419`
- 1h: commodity avg `0.2003` n `12`; crypto_alt avg `0.1172` n `228`; crypto_major avg `0.0079` n `8`; equity avg `-0.3008` n `67`; fx avg `-0.016` n `6`; index avg `-0.1503` n `23`; metal avg `-0.2634` n `18`; unknown avg `-0.0208` n `419`
- 4h: commodity avg `0.473` n `12`; crypto_alt avg `-0.4955` n `228`; crypto_major avg `-0.4639` n `8`; equity avg `-0.62` n `67`; fx avg `0.0042` n `6`; index avg `-0.2861` n `23`; metal avg `-1.1998` n `18`; unknown avg `0.629` n `419`
- 24h: commodity avg `-0.2862` n `12`; crypto_alt avg `-2.1656` n `228`; crypto_major avg `-1.8013` n `8`; equity avg `-1.0761` n `67`; fx avg `-0.0224` n `6`; index avg `-0.9677` n `23`; metal avg `-2.3654` n `18`; unknown avg `-0.7739` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
