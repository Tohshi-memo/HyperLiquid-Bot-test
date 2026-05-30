# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T02:52:20.138961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `0.0587` n `228`; crypto_major avg `0.0465` n `8`; equity avg `0.0099` n `69`; fx avg `0.0031` n `6`; index avg `-0.0177` n `23`; metal avg `0.0512` n `18`; unknown avg `-0.021` n `419`
- 1h: commodity avg `-0.1913` n `12`; crypto_alt avg `0.4521` n `228`; crypto_major avg `0.2307` n `8`; equity avg `0.0553` n `69`; fx avg `-0.0031` n `6`; index avg `-0.0182` n `23`; metal avg `0.0731` n `18`; unknown avg `-0.2616` n `419`
- 4h: commodity avg `0.0248` n `12`; crypto_alt avg `1.8782` n `228`; crypto_major avg `1.3548` n `8`; equity avg `0.2999` n `69`; fx avg `-0.0096` n `6`; index avg `-0.0321` n `23`; metal avg `0.0903` n `18`; unknown avg `-0.2552` n `419`
- 24h: commodity avg `-0.2336` n `12`; crypto_alt avg `2.6165` n `228`; crypto_major avg `2.5557` n `8`; equity avg `1.3737` n `69`; fx avg `0.1107` n `6`; index avg `0.1678` n `23`; metal avg `0.0398` n `18`; unknown avg `0.7462` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
