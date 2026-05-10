# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T07:37:06.813686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.062` n `228`; crypto_major avg `0.0362` n `8`; equity avg `0.0327` n `65`; fx avg `0.0002` n `5`; index avg `-0.0024` n `23`; metal avg `-0.0204` n `18`; unknown avg `-0.216` n `376`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `0.3819` n `228`; crypto_major avg `0.1926` n `8`; equity avg `0.0624` n `65`; fx avg `0.0015` n `5`; index avg `0.0107` n `23`; metal avg `-0.0796` n `18`; unknown avg `-0.0403` n `376`
- 4h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.4081` n `228`; crypto_major avg `0.2229` n `8`; equity avg `0.1445` n `65`; fx avg `0.0026` n `5`; index avg `0.0248` n `23`; metal avg `0.0731` n `18`; unknown avg `-0.1541` n `366`
- 24h: commodity avg `0.1557` n `12`; crypto_alt avg `-0.7184` n `228`; crypto_major avg `-0.3646` n `8`; equity avg `1.0499` n `65`; fx avg `-0.024` n `5`; index avg `0.2656` n `23`; metal avg `0.3199` n `18`; unknown avg `-0.3066` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
