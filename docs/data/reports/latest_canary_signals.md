# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T13:07:12.936915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `-0.0739` n `228`; crypto_major avg `-0.1179` n `8`; equity avg `-0.0042` n `65`; fx avg `-0.0009` n `5`; index avg `-0.0037` n `23`; metal avg `0.0027` n `18`; unknown avg `-0.074` n `383`
- 1h: commodity avg `0.0576` n `12`; crypto_alt avg `-0.131` n `228`; crypto_major avg `0.0965` n `8`; equity avg `0.073` n `65`; fx avg `0.0` n `5`; index avg `0.0048` n `23`; metal avg `0.0111` n `18`; unknown avg `-0.0435` n `383`
- 4h: commodity avg `0.0217` n `12`; crypto_alt avg `-0.1523` n `228`; crypto_major avg `0.4113` n `8`; equity avg `0.328` n `65`; fx avg `-0.0165` n `5`; index avg `0.1318` n `23`; metal avg `-0.0119` n `18`; unknown avg `-0.0457` n `383`
- 24h: commodity avg `1.812` n `12`; crypto_alt avg `-9.0965` n `228`; crypto_major avg `-2.1938` n `8`; equity avg `-2.5272` n `65`; fx avg `-0.1861` n `5`; index avg `-1.649` n `23`; metal avg `-5.8395` n `18`; unknown avg `550.083` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
