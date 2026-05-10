# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T10:41:43.577871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0945` n `12`; crypto_alt avg `0.1287` n `228`; crypto_major avg `0.0196` n `8`; equity avg `0.0194` n `65`; fx avg `0.0` n `5`; index avg `-0.0033` n `23`; metal avg `0.0046` n `18`; unknown avg `0.0151` n `376`
- 1h: commodity avg `0.0837` n `12`; crypto_alt avg `-0.0648` n `228`; crypto_major avg `-0.1593` n `8`; equity avg `0.0227` n `65`; fx avg `0.0` n `5`; index avg `-0.0001` n `23`; metal avg `0.0102` n `18`; unknown avg `-0.0105` n `376`
- 4h: commodity avg `-0.0453` n `12`; crypto_alt avg `0.4891` n `228`; crypto_major avg `0.1598` n `8`; equity avg `0.0338` n `65`; fx avg `0.0102` n `5`; index avg `0.0191` n `23`; metal avg `-0.0301` n `18`; unknown avg `0.2198` n `376`
- 24h: commodity avg `0.1367` n `12`; crypto_alt avg `-0.0325` n `228`; crypto_major avg `-0.098` n `8`; equity avg `0.8876` n `65`; fx avg `-0.0193` n `5`; index avg `0.2866` n `23`; metal avg `0.4223` n `18`; unknown avg `0.0143` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
