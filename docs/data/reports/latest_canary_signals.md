# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T10:37:20.442104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.1359` n `228`; crypto_major avg `0.0351` n `8`; equity avg `-0.014` n `65`; fx avg `0.0` n `5`; index avg `-0.0047` n `23`; metal avg `-0.0108` n `18`; unknown avg `0.0158` n `376`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.0574` n `228`; crypto_major avg `-0.1439` n `8`; equity avg `-0.0107` n `65`; fx avg `0.0` n `5`; index avg `-0.0015` n `23`; metal avg `-0.0052` n `18`; unknown avg `-0.01` n `376`
- 4h: commodity avg `-0.1333` n `12`; crypto_alt avg `0.4965` n `228`; crypto_major avg `0.1753` n `8`; equity avg `0.0008` n `65`; fx avg `0.0102` n `5`; index avg `0.0176` n `23`; metal avg `-0.0455` n `18`; unknown avg `0.2202` n `376`
- 24h: commodity avg `0.049` n `12`; crypto_alt avg `-0.0224` n `228`; crypto_major avg `-0.0824` n `8`; equity avg `0.8523` n `65`; fx avg `-0.0193` n `5`; index avg `0.2852` n `23`; metal avg `0.4067` n `18`; unknown avg `0.0178` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
