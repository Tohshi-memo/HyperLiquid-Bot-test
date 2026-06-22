# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T20:52:29.230723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `-0.1405` n `228`; crypto_major avg `-0.1631` n `8`; equity avg `0.0047` n `85`; fx avg `0.0068` n `6`; index avg `0.0001` n `23`; metal avg `0.0134` n `20`; unknown avg `-0.0112` n `717`
- 1h: commodity avg `-0.0623` n `12`; crypto_alt avg `0.099` n `228`; crypto_major avg `-0.04` n `8`; equity avg `0.0337` n `85`; fx avg `0.005` n `6`; index avg `0.0118` n `23`; metal avg `0.0491` n `20`; unknown avg `-0.1782` n `709`
- 4h: commodity avg `-0.1128` n `12`; crypto_alt avg `-0.6916` n `228`; crypto_major avg `-0.316` n `8`; equity avg `-0.0914` n `85`; fx avg `0.0099` n `6`; index avg `-0.0473` n `23`; metal avg `0.0188` n `20`; unknown avg `-0.211` n `709`
- 24h: commodity avg `-0.9814` n `12`; crypto_alt avg `-0.3813` n `228`; crypto_major avg `-0.1052` n `8`; equity avg `-0.5324` n `85`; fx avg `0.1259` n `6`; index avg `0.1003` n `23`; metal avg `0.352` n `18`; unknown avg `0.6632` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
